import random
import time
import pandas as pd
import os

from algorithms.linear_search import linear_search
from algorithms.binary_search import binary_search
from algorithms.jump_search import jump_search
from algorithms.interpolation_search import interpolation_search
from algorithms.exponential_search import exponential_search


# Input sizes to test
SIZES = [100, 500, 800]

# Number of repetitions
REPETITIONS = 5

# Types of cases for searching
CASES = ["Best", "Average", "Worst"]


def measure_time(algorithm, data, target):
    start = time.perf_counter()
    algorithm(data, target)
    end = time.perf_counter()
    return end - start


def generate_data(size):
    """
    Generates a sorted array for search algorithms.
    """
    return sorted(random.sample(range(size * 3), size))


def select_target(data, case_type):
    """
    Selects target depending on case type.
    """
    if case_type == "Best":
        return data[0]  # First element

    elif case_type == "Worst":
        return data[-1]  # Last element

    else:  # Average
        return data[len(data) // 2]


def run_benchmark():
    results = []

    algorithms = {
        "Linear Search": linear_search,
        "Binary Search": binary_search,
        "Jump Search": jump_search,
        "Interpolation Search": interpolation_search,
        "Exponential Search": exponential_search
    }

    for size in SIZES:
        for case in CASES:
            for _ in range(REPETITIONS):

                base_data = generate_data(size)
                target = select_target(base_data, case)

                for name, algorithm in algorithms.items():
                    elapsed_time = measure_time(algorithm, base_data, target)

                    results.append({
                        "Algorithm": name,
                        "Input Size": size,
                        "Case": case,
                        "Time (seconds)": elapsed_time
                    })

    return pd.DataFrame(results)


if __name__ == "__main__":
    df = run_benchmark()
    output_path = os.path.join(os.path.dirname(__file__), "benchmark_results.csv")
    df.to_csv(output_path, index=False)
    print("Benchmark completed. Results saved to benchmark_results.csv")