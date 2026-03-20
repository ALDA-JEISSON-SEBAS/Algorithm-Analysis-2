# Searching Algorithms - Empirical Complexity Analysis

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg?style=for-the-badge&logo=python)]
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas)]
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange?style=for-the-badge)]
[![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plots-green?style=for-the-badge)]
[![License](https://img.shields.io/badge/License-MIT-black?style=for-the-badge)]

---

## Project Overview

This project presents an empirical performance evaluation of four classical searching algorithms:

- Binary Search
- Jump Search
- Interpolation Search
- Exponential Search

The objective is to experimentally compare their behavior under:

- Best Case
- Average Case
- Worst Case

All algorithms are evaluated on previously sorted input arrays so the benchmark measures search performance directly.

---

## Theoretical Complexity Comparison

| Algorithm            | Best Case | Average Case | Worst Case |
|----------------------|-----------|--------------|------------|
| Binary Search        | O(1)      | O(log n)     | O(log n)   |
| Jump Search          | O(1)      | O(sqrt(n))   | O(sqrt(n)) |
| Interpolation Search | O(1)      | O(log log n)*| O(n)       |
| Exponential Search   | O(1)      | O(log n)     | O(log n)   |

\* Interpolation Search assumes uniformly distributed data.

---

## Analysis Workflow

Algorithm Implementation
-> Sorted Input Generation
-> Target Selection (Best / Average / Worst)
-> Benchmark Execution
-> Execution Time Measurement (`time.perf_counter()`)
-> Statistical Aggregation
-> Visualization and Ranking
-> Scalability Interpretation

---

## Core Components

### 1. Algorithm Implementation

All searching algorithms are implemented from scratch in Python:

- `binary_search.py`
- `jump_search.py`
- `interpolation_search.py`
- `exponential_search.py`

### 2. Benchmarking System

The benchmark module:

- Generates sorted input sizes from `1000` to `10000`
- Creates three search scenarios:
  - Best Case -> target at the first position
  - Average Case -> target in the middle position
  - Worst Case -> target at the last position
- Repeats executions for averaging
- Measures time using `time.perf_counter()`
- Exports results to CSV for analysis

### 3. Experimental Analysis

The Jupyter Notebook performs:

- Mean execution time computation
- Case comparison visualization
- Worst-case analysis
- Algorithm ranking
- Growth rate analysis
- Percentage growth comparison
- Empirical validation of search complexity

---

## Getting Started

### Prerequisites

- Python 3.11
- pip

## Installation

```bash
git clone https://github.com/your-username/searching-algorithms-analysis.git
cd searching-algorithms-analysis
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

---

## Running the Benchmark

From the project root:

```bash
python -m experiments.benchmark
```

This generates:

```text
experiments/benchmark_results.csv
```

---

## Running the Analysis

Open the notebook:

```bash
jupyter notebook notebook/experimental_analysis.ipynb
```

---

## Project Structure

```text
algorithms/
|-- __init__.py
|-- binary_search.py
|-- jump_search.py
|-- interpolation_search.py
`-- exponential_search.py

experiments/
|-- benchmark.py
`-- benchmark_results.csv

notebook/
`-- experimental_analysis.ipynb

tests/
|-- __init__.py
|-- binary_search_test.py
|-- jump_search_test.py
|-- interpolation_search_test.py
|-- exponential_search_test.py
`-- linear_search_test.py

README.md
```

---

## Key Experimental Findings

- Binary Search shows the best overall average performance in the benchmark.
- Exponential Search remains efficient, although it is usually slightly slower than Binary Search.
- Interpolation Search can be highly competitive when the data distribution is favorable.
- Jump Search grows faster than the logarithmic alternatives as input size increases.

---

## Academic Context

Developed as part of an Algorithm Analysis course to validate theoretical behavior through controlled experimental benchmarking and visualization.

---

## License

This project is licensed under the MIT License.

---

## Authors

[![GitHub](https://img.shields.io/badge/GitHub-JeissonS02-181717?style=for-the-badge&logo=github)](https://github.com/JeissonS02)
[![GitHub](https://img.shields.io/badge/GitHub-SebastianAlbarracinSilva-181717?style=for-the-badge&logo=github)](https://github.com/SebastianAlbarracinSilva)
