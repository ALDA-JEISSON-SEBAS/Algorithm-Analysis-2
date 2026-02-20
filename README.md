# 🔎 Searching Algorithms — Empirical Complexity Analysis  

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg?style=for-the-badge&logo=python)]  
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas)]  
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange?style=for-the-badge)]  
[![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plots-green?style=for-the-badge)]  
[![License](https://img.shields.io/badge/License-MIT-black?style=for-the-badge)]  

---

## 📌 Project Overview  

This project presents an empirical performance evaluation of five classical **searching algorithms**:

- Linear Search  
- Binary Search  
- Jump Search  
- Interpolation Search  
- Exponential Search  

The objective is to experimentally validate their theoretical time complexity under:

- **Best Case**
- **Average Case**
- **Worst Case**

The study combines benchmarking, statistical aggregation, visualization, ranking, and scalability analysis to evaluate real-world performance and compare it against asymptotic theory.

---

## 🧠 Theoretical Complexity Comparison  

| Algorithm              | Best Case | Average Case | Worst Case |
|------------------------|-----------|--------------|------------|
| Linear Search          | O(1)      | O(n)         | O(n)       |
| Binary Search          | O(1)      | O(log n)     | O(log n)   |
| Jump Search            | O(1)      | O(√n)        | O(√n)      |
| Interpolation Search   | O(1)      | O(log log n)*| O(n)       |
| Exponential Search     | O(1)      | O(log n)     | O(log n)   |

\*Interpolation Search assumes uniformly distributed data.

---

## 🏗 Analysis Workflow  

Algorithm Implementation  
↓  
Sorted Input Generation  
↓  
Target Selection (Best / Average / Worst)  
↓  
Benchmark Execution  
↓  
Execution Time Measurement (`time.perf_counter()`)  
↓  
Statistical Aggregation  
↓  
Visualization & Ranking  
↓  
Scalability Interpretation  

---

## 🧩 Core Components  

### 1️⃣ Algorithm Implementation  

All searching algorithms are implemented from scratch in Python.

> ⚠ Note:  
> Binary, Jump, Interpolation, and Exponential Search require **sorted input arrays**.

---

### 2️⃣ Benchmarking System  

The benchmark module:

- Generates controlled input sizes
- Creates three search scenarios:
  - **Best Case** → target at first position
  - **Average Case** → target at random position
  - **Worst Case** → target at last position or not present
- Repeats executions for averaging
- Measures time using `time.perf_counter()`
- Exports results to CSV for analysis

---

### 3️⃣ Experimental Analysis  

The Jupyter Notebook performs:

- Mean execution time computation  
- Case comparison visualization  
- Worst-case degradation analysis  
- Algorithm ranking  
- Growth rate analysis  
- Percentage scalability comparison  
- Empirical validation of asymptotic complexity  

---

## 🚀 Getting Started  

### 📦 Prerequisites  

- Python 3.11  
- pip  

---

## ⚙️ Installation  

```bash
git clone https://github.com/your-username/searching-algorithms-analysis.git
cd searching-algorithms-analysis
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

---

## ▶️ Running the Benchmark  

From the project root:

```bash
python -m experiments.search_benchmark
```

This generates:

```
search_benchmark_results.csv
```

---

## ▶️ Running the Analysis  

Launch Jupyter:

```bash
jupyter notebook notebook/search_experimental_analysis.ipynb
```

---

## 📁 Project Structure  

```
├── algorithms/
│   ├── linear_search.py
│   ├── binary_search.py
│   ├── jump_search.py
│   ├── interpolation_search.py
│   └── exponential_search.py
│
├── experiments/
│   ├── search_benchmark.py
│   └── search_benchmark_results.csv
│
├── notebook/
│   └── search_experimental_analysis.ipynb
│
├── tests/
│
├── requirements.txt
└── README.md
```

---

## 📈 Key Experimental Findings  

- **Linear Search** exhibits linear growth O(n) and becomes inefficient for large datasets.
- **Jump Search** reduces complexity to O(√n) but remains slower than logarithmic approaches.
- **Binary Search** and **Exponential Search** demonstrate highly scalable O(log n) behavior.
- **Interpolation Search** can outperform others under uniform distribution but may degrade otherwise.
- Empirical results strongly align with theoretical time complexity.

---

## 🎓 Academic Context  

Developed as part of an **Algorithm Analysis** course to validate theoretical time complexity through controlled experimental benchmarking and visualization.

---

## 📜 License  

This project is licensed under the MIT License.

---

## 👨‍💻 Authors  

[![GitHub](https://img.shields.io/badge/GitHub-JeissonS02-181717?style=for-the-badge&logo=github)](https://github.com/JeissonS02)  
[![GitHub](https://img.shields.io/badge/GitHub-SebastianAlbarracinSilva-181717?style=for-the-badge&logo=github)](https://github.com/SebastianAlbarracinSilva)  