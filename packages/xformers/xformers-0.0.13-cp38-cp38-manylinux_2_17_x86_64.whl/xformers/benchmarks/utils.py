# Copyright (c) Facebook, Inc. and its affiliates. All rights reserved.
#
# This source code is licensed under the BSD license found in the
# LICENSE file in the root directory of this source tree.

import argparse
import contextlib
import glob
import logging
import os
import pickle
import pprint
import tempfile
from collections import defaultdict, namedtuple
from dataclasses import replace
from typing import Any, Dict, Generator, List

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import torch
import tqdm
from torch.utils import benchmark

sns.set()

TestCase = namedtuple("TestCase", ["function", "name"])


_triton_is_available = torch.cuda.is_available()
if _triton_is_available:
    try:
        import triton
    except ImportError as e:
        logging.warning(f"Triton is not available: {e}.\nbench_functions")
        _triton_is_available = False


def pretty_print(results, title, units):
    """Printout the contents of a dict as a human-readable and Markdown compatible array"""
    print(title)
    header = " Units: {:<45}".format(units)
    print("| " + header + "|" + "".join("{0:<20}|".format(k) for k in results.keys()))

    offset = len(header)
    print(
        "|-{}|".format("-" * offset)
        + "".join("{}|".format("-" * 20) for _ in results.keys())
    )

    workloads: Dict[str, Any] = {k: [] for v in results.values() for k in v.keys()}
    for v in results.values():
        for k in v.keys():
            workloads[k].append(v[k])

    for k, w in workloads.items():
        print(
            "| {0:<{offset}}|".format(k, offset=offset)
            + "".join("{:<20}|".format(v) for v in w)
        )

    print("")


def pretty_plot(
    results, title, units: str, filename=None, dash_key="", legend_loc="lower right"
):
    """Graph out the contents of a dict.
    Dash key means that if the result label has this key, then it will be displayed with a dash"""

    if not filename:
        filename = title + ".png"

    # Sanitize the filename
    filename = (
        filename.replace(" ", "_").replace("/", "_").replace("-", "_").replace(":", "")
    )

    # Gather all the results in "collumns"
    workloads: Dict[str, Any] = {k: [] for v in results.values() for k in v.keys()}
    for v in results.values():
        for k in v.keys():
            workloads[k].append(float(v[k]))

    # Make sure that the plot is big enough
    f = plt.figure()
    f.set_figwidth(6)
    f.set_figheight(6)

    # Display the collections
    for k, v in workloads.items():
        if dash_key and dash_key in k:
            plt.plot(list(results.keys()), v, "--")
        else:
            plt.plot(list(results.keys()), v)

    plt.title(title)
    plt.legend(list(workloads.keys()), loc=legend_loc)
    plt.ylabel(units)
    plt.xticks(rotation=45)

    plt.savefig(filename, bbox_inches="tight")
    plt.close(f)


if _triton_is_available:

    def bench_functions(
        test_cases: List[TestCase], shapes, metric_transform, unit, title=""
    ):
        device = torch.device("cuda")

        for dtype in [torch.float16, torch.float32]:
            results: Dict[str, Any] = {}

            for B, M, K in shapes:
                a = torch.rand(B, M, K, device=device, dtype=dtype, requires_grad=True)

                for testcase in test_cases:
                    time = triton.testing.do_bench(lambda: testcase.function(a))[0]

                    metric = metric_transform(a, time)

                    key = f"B={B}, M={M}, K={K}"
                    if key not in results:
                        results[key] = {}

                    results[key][testcase.name] = f"{metric:.1f}"

            pretty_print(
                results,
                title=" ------------- Type: {} ------------- ".format(dtype),
                units=unit,
            )
            _type = " fp16" if dtype == torch.float16 else " fp32"
            pretty_plot(results, title + _type, unit, dash_key="pytorch")


def pretty_barplot(results, title, units: str, filename=None, dash_key=""):
    """Graph out the contents of a dict.
    Dash key means that if the result label has this key, then it will be displayed with a dash"""

    if not filename:
        filename = title + ".png"

    # Sanitize the filename
    filename = (
        filename.replace(" ", "_").replace("/", "_").replace("-", "_").replace(":", "")
    )

    xlabels = list(results.keys())
    # Gather all the results in "collumns"
    workloads: Dict[str, Any] = {k: [] for v in results.values() for k in v.keys()}
    for v in results.values():
        for k in v.keys():
            workloads[k].append(float(v[k]))

    options = list(workloads.keys())
    group_len = len(options)
    for key in workloads.keys():
        num_groups = len(workloads[key])
        break
    group_width = group_len + 1

    # Make sure that the plot is big enough
    f = plt.figure()
    f.set_figwidth(6)
    f.set_figheight(6)

    for idx in range(group_len):
        option = options[idx]
        values = workloads[option]
        xloc = np.arange(1 + idx, group_width * num_groups, group_width)
        plt.bar(xloc, values, width=1, edgecolor="black")

    plt.title(title)
    plt.legend(list(workloads.keys()), loc="upper right")
    plt.ylabel(units)

    ax = plt.gca()
    xticks_loc = np.arange(
        1 + (group_len - 1) / 2.0, group_width * num_groups, group_width
    )
    ax.set_xticks(xticks_loc, xlabels)
    plt.xticks(rotation=45)

    plt.setp(ax.xaxis.get_majorticklabels(), ha="right")
    ax.set_axisbelow(True)
    ax.yaxis.grid(color="gray", linestyle="dashed")
    ax.xaxis.grid(color="gray", linestyle="dashed")

    plt.savefig(filename, bbox_inches="tight")
    plt.close(f)


def rmf(filename: str) -> None:
    """Remove a file like rm -f."""
    try:
        os.remove(filename)
    except FileNotFoundError:
        pass


@contextlib.contextmanager
def temp_files_ctx(num: int) -> Generator:
    """A context to get tempfiles and ensure they are cleaned up."""
    files = [tempfile.mkstemp()[1] for _ in range(num)]

    yield tuple(files)

    # temp files could have been removed, so we use rmf.
    for name in files:
        rmf(name)


def benchmark_main_helper(
    benchmark_fn, cases: List[Dict[str, Any]], *, min_run_time: int = 2
) -> None:
    """
    Helper function to run benchmarks.
    Supports loading previous results for comparison, and saving current results to file.
    """
    SKIP_VANILLA_TASKS_IF_ALREADY_DONE = True

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--fn", default=None, type=str, help="Only benchmark this function"
    )
    parser.add_argument(
        "--label", default=None, type=str, help="Store results to a file"
    )
    parser.add_argument(
        "--compare",
        default=None,
        type=str,
        help="Compare to previously stored benchmarks (coma separated)",
    )
    args = parser.parse_args()

    if args.fn is not None and args.fn != benchmark_fn.__name__:
        print(f'Skipping benchmark "{benchmark_fn.__name__}"')
        return

    results_compare_to = []
    results = []
    mem_use: Dict[str, Dict[str, float]] = defaultdict(dict)

    store_results_folder = os.path.expanduser(
        os.path.join("~", ".cache", "xformers", "benchmarks", benchmark_fn.__name__)
    )
    optimized_label = "optimized" if args.label is None else args.label

    try:
        env = (
            torch.cuda.get_device_name(torch.cuda.current_device())
            .replace(" ", "_")
            .replace("-", "_")
        )
    except RuntimeError:  # No GPU
        env = "cpu"

    if args.compare is not None or args.label is not None:
        os.makedirs(store_results_folder, exist_ok=True)

    # Load runs that we want to compare to
    skip_vanilla_tasks = set()
    if args.compare is not None:
        for name in args.compare.split(","):
            for filename in glob.glob(
                os.path.join(store_results_folder, f"{name}.*.pkl")
            ):
                with open(filename, "rb") as fd:
                    for r in pickle.load(fd):
                        spec = r.task_spec
                        if r.task_spec.description != "vanilla":
                            # (in case the file was renamed)
                            r.task_spec = replace(r.task_spec, description=name)
                        elif spec.env == env:
                            if SKIP_VANILLA_TASKS_IF_ALREADY_DONE:
                                skip_vanilla_tasks.add(
                                    (spec.sub_label, spec.num_threads)
                                )
                            else:
                                continue
                        results_compare_to.append(r)

    pbar = tqdm.tqdm(cases, leave=False)
    for case in pbar:
        # pbar.set_description(str(case))
        pbar.write(f"====== {str(case)} ======")
        try:
            benchmarks_generator = benchmark_fn(**case)
        except NotImplementedError:
            # pbar.write(f"Skipped (NotImplementedError)")
            continue

        name = None
        for benchmark_object, is_optimized in zip(benchmarks_generator, [True, False]):
            if benchmark_object is None:
                continue
            if is_optimized:
                benchmark_object._task_spec = replace(
                    benchmark_object._task_spec, description=optimized_label
                )
            elif (
                benchmark_object._task_spec.sub_label,
                benchmark_object._task_spec.num_threads,
            ) in skip_vanilla_tasks:
                continue

            torch.cuda.synchronize()
            torch.cuda.reset_peak_memory_stats()
            benchmark_object._task_spec = replace(benchmark_object._task_spec, env=env)
            measurement = benchmark_object.blocked_autorange(min_run_time=min_run_time)
            del benchmark_object
            torch.cuda.synchronize()
            results.append(measurement)
            name = measurement.task_spec.description
            memory = torch.cuda.max_memory_allocated() / 2**20
            mem_use[name][measurement.task_spec.sub_label] = memory
            pbar.write(f"{name}: memory used: {memory} MB")
        # Display results for benchmarks we just calculated
        if name is not None:

            def matches_current(r):
                return (
                    r.task_spec.sub_label == results[-1].task_spec.sub_label
                    and r.task_spec.label == results[-1].task_spec.label
                )

            pbar.write(
                str(
                    benchmark.Compare(
                        list(filter(matches_current, results))
                        + list(filter(matches_current, results_compare_to))
                    )
                )
            )

    pprint.pprint(mem_use)
    benchmark.Compare(results + results_compare_to).print()

    # Save runs to a file
    if args.label is not None:
        write_to_path = os.path.join(
            store_results_folder, f"{optimized_label}.{env}.pkl"
        )
        with open(write_to_path, "wb+") as fd:
            pickle.dump(results, fd)
        print(f"Saved results to {write_to_path}")
