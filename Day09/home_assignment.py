from datetime import datetime
from collections import defaultdict, Counter
import matplotlib.pyplot as plt


# =========================
# Deadlines (from README)
# =========================
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


# =========================
# Load and parse data
# =========================
def load_submissions(path: str):
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

            submissions.append({
                "student": student.strip(),
                "assignment": assignment.strip(),
                "time": datetime.fromisoformat(timestamp.replace("Z", ""))
            })

    return submissions


# =========================
# Analysis functions
# =========================
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
        assignment = s["assignment"]
        if assignment not in DEADLINES:
            continue

        deadline = datetime.fromisoformat(DEADLINES[assignment])
        if s["time"] > deadline:
            hours_late = (s["time"] - deadline).total_seconds() / 3600
            late.append((s["student"], assignment, hours_late))

    return late


def submission_time_deltas(submissions):
    deltas = []

    for s in submissions:
        assignment = s["assignment"]
        if assignment not in DEADLINES:
            continue

        deadline = datetime.fromisoformat(DEADLINES[assignment])
        delta_hours = (s["time"] - deadline).total_seconds() / 3600
        deltas.append(delta_hours)

    return deltas


def assignment_popularity(submissions):
    return Counter(s["assignment"] for s in submissions)


# =========================
# Main report
# =========================
def main():
    submissions = load_submissions("subjects.txt")

    print("\n=== Assignment Popularity ===")
    popularity = assignment_popularity(submissions)
    for assignment, count in popularity.most_common():
        print(f"{assignment}: {count} submissions")

    print("\n=== Late Submissions ===")
    late = find_late_submissions(submissions)
    if not late:
        print("No late submissions 🎉")
    else:
        for student, assignment, hours in late:
            print(f"{student} - {assignment}: {hours:.1f} hours late")

    print("\n=== Students Missing Assignments (sample) ===")
    missing = find_missing_submissions(submissions)
    for student, tasks in list(missing.items())[:5]:
        print(f"{student}: missing {', '.join(tasks)}")

    # =========================
    # Plot: submission timing
    # =========================
    deltas = submission_time_deltas(submissions)

    plt.figure()
    plt.hist(deltas, bins=30)
    plt.axvline(0)
    plt.xlabel("Hours relative to deadline")
    plt.ylabel("Number of submissions")
    plt.title("Submission time distribution relative to deadline")
    plt.show()


if __name__ == "__main__":
    main()
