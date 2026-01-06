# 📊 Day 09 – Assignment Submission Analysis

## 🧠 Overview

This project analyzes assignment submission data from `subjects.txt` and produces both **textual reports** and **visual insights** 📈.  
All analyses are based on GitHub issue submission timestamps and official course deadlines.

---

## 🗂 Project Structure

```text
Day09/
├── home_assignment.py
├── subjects.txt
└── README.md
````

* 🐍 **home_assignment.py** – Main analysis script
* 📄 **subjects.txt** – Raw submission data
* 📝 **README.md** – Project documentation

---

## 🧹 Data Cleaning & Normalization

### 🔄 Assignment Name Normalization

Submission titles are not always consistent
(e.g. `day1`, `Day01`, `DAY 1`).

To avoid duplicate or misleading statistics:

* All `dayX` variants are normalized to **`DayXX`**

  * `day1` → `Day01`
  * `day9` → `Day09`
* Non-day assignments (e.g. **Final Project proposal**) remain unchanged

✅ This ensures accurate aggregation and fair comparisons.

---

## 🔍 Analyses Performed

### 📌 1. Assignment Popularity

* Counts how many submissions were made per assignment
* Displayed as:

  * 🖨 Text output
  * 📊 Bar chart
* The Y-axis contains **only integer values** (no such thing as half a submission!)

---

### ⏱ 2. Late Submissions

* Identifies submissions submitted **after the deadline**
* Reports:

  * Who was late
  * For which assignment
  * How many hours late
* Also visualized as:

  * 📊 Number of late submissions per assignment

---

### ❌ 3. Missing Submissions

* Detects students who did **not submit certain assignments**
* Prints a short sample list for quick inspection

---

### 📈 4. Submission Timing Distribution

* Calculates the time difference (in hours) between submission and deadline
* Visualized as a histogram:

  * 🟢 Negative values → early submissions
  * 🔴 Positive values → late submissions

---

### 🚀 5. Fastest Submissions

* Finds the **earliest submission** for each assignment
* Counts how many times each student submitted first
* Visualized as a bar chart highlighting the most consistent early submitters

---

## 🎨 Visualizations

The script generates the following graphs using `matplotlib`:

1. 📊 Assignment popularity
2. ⚠️ Late submissions per assignment
3. ⏰ Submission timing relative to deadline
4. 🏆 Students who submitted first (frequency)

Each graph uses distinct colors for clarity and readability while keeping a clean, academic style.

---

## ▶️ How to Run

From the project root directory:

```bash
python Day09/home_assignment.py
```

What happens next?

* 📂 The script loads `subjects.txt` automatically
* 🖨 Textual reports are printed to the terminal
* 📈 Graphs open in separate windows

---

## 🧩 Dependencies

* 🐍 Python 3.9+
* 📦 Standard library:

  * `datetime`
  * `collections`
  * `pathlib`
  * `re`
* 📊 External library:

  * `matplotlib`

---

## 📝 Notes

* Deadlines are hard-coded based on the official course README
* All results are **deterministic and reproducible**
* The code is structured to clearly separate:

  * Data loading
  * Analysis logic
  * Visualization



