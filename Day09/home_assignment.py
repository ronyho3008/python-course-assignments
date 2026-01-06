from datetime import datetime
from collections import defaultdict, Counter
from pathlib import Path
import matplotlib.pyplot as plt
import re

## Deadlines (from README)
DEADLINES = {
    "Day01": "2025-11-01T22:00:00",
    "Day02": "2025-11-09T22:00:00",
    "Day03": "2025-11-16T22:00:00",
    "Day04": "2025-11-23T22:00:00",
    "Day05": "2025-11-29T22:00:00",
    "Day06": "2025-12-06T22:00:00",
    "Day08": "2025-12-30T22:00:00",
    "Day09": "2026-01-10T22:00:00",
    "Final Project proposal": "2026-01-11T22:00:00",
}


##data loading
def load_submissions(path: Path):
    submissions = []

    with open(path, encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split("\t")
            if len(parts) < 5:
                continue

            _, _, title, _, timestamp = parts

            if " by " not in title:
                continue

            assignment, student = title.rsplit(" by ", 1)
            assignment = normalize_assignment_name(assignment)

            submissions.append({
                "student": student.strip(),
                "assignment": assignment,
                "time": datetime.fromisoformat(timestamp.replace("Z", ""))
            })

    return submissions


##Analysis
def normalize_assignment_name(name: str) -> str:
    name = name.strip()

    match = re.match(r"day\s*0*(\d+)", name, re.IGNORECASE)
    if match:
        day_number = int(match.group(1))
        return f"Day{day_number:02d}"

    return name
def assignment_popularity(submissions):
    return Counter(s["assignment"] for s in submissions)


def find_missing_submissions(submissions):
    students = {s["student"] for s in submissions}
    submitted = defaultdict(set)

    for s in submissions:
        submitted[s["student"]].add(s["assignment"])

    missing = defaultdict(list)
    for student in students:
        for assignment in DEADLINES:
            if assignment not in submitted[student]:
                missing[student].append(assignment)

    return missing


def find_late_submissions(submissions):
    late = []

    for s in submissions:
        if s["assignment"] not in DEADLINES:
            continue

        deadline = datetime.fromisoformat(DEADLINES[s["assignment"]])
        if s["time"] > deadline:
            hours_late = (s["time"] - deadline).total_seconds() / 3600
            late.append((s["student"], s["assignment"], hours_late))

    return late


def late_count_per_assignment(submissions):
    counter = Counter()

    for s in submissions:
        if s["assignment"] not in DEADLINES:
            continue

        deadline = datetime.fromisoformat(DEADLINES[s["assignment"]])
        if s["time"] > deadline:
            counter[s["assignment"]] += 1

    return counter


def submission_time_deltas(submissions):
    deltas = []

    for s in submissions:
        if s["assignment"] not in DEADLINES:
            continue

        deadline = datetime.fromisoformat(DEADLINES[s["assignment"]])
        delta_hours = (s["time"] - deadline).total_seconds() / 3600
        deltas.append(delta_hours)

    return deltas


def students_fastest_multiple_times(submissions):
    earliest = {}

    for s in submissions:
        if s["assignment"] not in DEADLINES:
            continue

        if s["assignment"] not in earliest or s["time"] < earliest[s["assignment"]]["time"]:
            earliest[s["assignment"]] = s

    counter = Counter(s["student"] for s in earliest.values())
    return counter


def fastest_submission_times(submissions):
    fastest = {}

    for s in submissions:
        if s["assignment"] not in DEADLINES:
            continue

        deadline = datetime.fromisoformat(DEADLINES[s["assignment"]])

        if s["assignment"] not in fastest or s["time"] < fastest[s["assignment"]]["time"]:
            fastest[s["assignment"]] = {
                "student": s["student"],
                "hours_before": (deadline - s["time"]).total_seconds() / 3600
            }

    return fastest



##Main
def main():
    base_dir = Path(__file__).parent
    subjects_path = base_dir / "subjects.txt"

    if not subjects_path.exists():
        print(f"ERROR: {subjects_path} not found")
        return

    submissions = load_submissions(subjects_path)

    # -------- Textual reports --------
    print("\n=== Assignment Popularity ===")
    popularity = assignment_popularity(submissions)
    for a, c in popularity.most_common():
        print(f"{a}: {c}")

    print("\n=== Late Submissions ===")
    late = find_late_submissions(submissions)
    for student, assignment, hours in late:
        print(f"{student} - {assignment}: {hours:.1f} hours late")

    print("\n=== Students Missing Assignments (sample) ===")
    missing = find_missing_submissions(submissions)
    for student, tasks in list(missing.items())[:5]:
        print(f"{student}: {', '.join(tasks)}")

    # -------- Graph 1: Popularity --------
    plt.figure()
    plt.bar(popularity.keys(), popularity.values(), color='magenta')
    plt.title("Assignment popularity")
    plt.xlabel("Assignment")
    plt.ylabel("Submissions")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.yticks(range(0, max(popularity.values()) + 1))
    plt.show()

    # -------- Graph 2: Late submissions per assignment --------
    late_counts = late_count_per_assignment(submissions)

    plt.figure()
    plt.bar(late_counts.keys(), late_counts.values(),  color='lightcoral')
    plt.title("Late submissions per assignment")
    plt.xlabel("Assignment")
    plt.ylabel("Late submissions")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # -------- Graph 3: Submission timing distribution --------
    deltas = submission_time_deltas(submissions)

    plt.figure()
    plt.hist(deltas, bins=30,  color='lightseagreen')
    plt.axvline(0)
    plt.title("Submission time relative to deadline")
    plt.xlabel("Hours (negative = early)")
    plt.ylabel("Number of submissions")
    plt.tight_layout()
    plt.show()

    # -------- Graph 4: Fastest students --------
    fastest_students = students_fastest_multiple_times(submissions)

    plt.figure()
    plt.bar(fastest_students.keys(), fastest_students.values(),  color='lightsteelblue')
    plt.title("Students who submitted first")
    plt.xlabel("Student")
    plt.ylabel("Times fastest")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
