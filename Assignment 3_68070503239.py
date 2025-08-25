# %% [markdown]
# 
# # Assignment 2: Gradebook & Log Analyzer
# 
# **Covers:** Conditionals & Loops • File I/O • Dictionaries, Tuples & Methods  
# **Estimated time:** ~2–3 hours
# 
# ## Learning outcomes
# By completing this assignment, you will be able to:
# 1. Use conditionals and loops to implement program logic.
# 2. Read from and write to text/CSV files safely.
# 3. Model data with dictionaries and tuples; use built-in methods effectively.
# 4. Build a small, menu-driven CLI program that ties everything together.
# 

# %% [markdown]
# 
# ## Instructions
# - Work in this notebook. Replace each `# TODO` with your code.
# - Do **not** change the function names or signatures unless asked.
# - Run the provided tests (asserts) to self-check. Passing tests ≠ perfect score.
# - When you finish, **restart & run all** to ensure it executes cleanly top-to-bottom.
# - Submit the exported `.ipynb` (and any generated `.txt`/`.csv` files).

# %%

# --- Setup: create tiny sample datasets (run once) ---
from pathlib import Path
import csv

data_dir = Path("data")
data_dir.mkdir(exist_ok=True)

# Sample scores.csv: student_id,name,quiz1,quiz2,quiz3
scores_path = data_dir / "scores.csv"
if not scores_path.exists():
    with scores_path.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["student_id", "name", "quiz1", "quiz2", "quiz3"])
        writer.writerows([
            ["S001", "Aye", 8, 9, 10],
            ["S002", "Khin", 7, 6, 9],
            ["S003", "Ryan", 10, 10, 9],
            ["S004", "Hugo", 5, 7, 6],
            ["S005", "Thiri", 9, 8, 8],
        ])

# Sample access.log: username,action,timestamp (ISO-like, simplified)
log_path = data_dir / "access.log"
if not log_path.exists():
    log_path.write_text(
        "aye,login,2025-08-01T09:00\n"
        "aye,submit,2025-08-01T09:10\n"
        "khin,login,2025-08-01T09:05\n"
        "ryan,login,2025-08-01T09:07\n"
        "ryan,download,2025-08-01T09:20\n"
        "ryan,submit,2025-08-01T09:35\n"
        "hugo,login,2025-08-01T09:40\n"
        "thiri,login,2025-08-01T09:41\n"
        "aye,download,2025-08-01T09:50\n"
    )
print("Sample data ready at:", data_dir.resolve())


# %% [markdown]
# 
# ---
# ## Part A — Warm‑ups (Conditionals, Loops, Tuples)
# 
# ### A1. `letter_grade(avg)`
# Write a function that converts a numeric average (0–10) to a letter grade:
# - `>= 9.0` → **A**
# - `>= 8.0` → **B**
# - `>= 7.0` → **C**
# - `>= 6.0` → **D**
# - else → **F**
# 
# Edge cases: floor to one decimal place before comparing (e.g., `8.96 → 8.9`).
# 
# ### A2. `count_vowels(s)`
# Return a dictionary mapping vowel → count for the string `s`. Treat `'aeiou'` as vowels and ignore case.
# 
# ### A3. `rotate_tuple(t)`
# Given a non-empty tuple `t`, return a **new** tuple where the last element moves to the front. Example: `(1,2,3) → (3,1,2)`.
# 

# %%

# TODO: A1
def letter_grade(avg: float) -> str:

 if avg >= 9.0:
    return 'A'
 elif avg >= 8.0:
    return 'B'
 elif avg >= 7.0:
    return 'C'
 elif avg >= 6.0:
    return 'D'
 else:
    return 'F'

letter_grade



# %%

# TODO: A2
def count_vowels(s: str) -> dict:
    d = {}
    vowels = "aeiou"
    for char in s.lower():
        if char in vowels:
            d[char] = d.get(char, 0) + 1
    return d
count_vowels


# %%

# TODO: A3
def rotate_tuple(t: tuple) -> tuple:
    return(t[-1],)+ t[0:-1]


# %%

# --- Tests for Part A ---
assert letter_grade(9.0) == "A"
assert letter_grade(8.0) == "B"
assert letter_grade(6.0) == "D"

assert count_vowels("Aye") == {'a': 1, 'e': 1}
assert count_vowels("Beautiful day") == {'a': 2, 'e': 1, 'i': 1, 'o': 0, 'u': 2} or        sum(count_vowels("Beautiful day").values()) == 6  # lenient check

assert rotate_tuple((1,2,3)) == (3,1,2)
assert rotate_tuple(("a",)) == ("a",)
print("Part A tests passed (if no AssertionError).")


# %% [markdown]
# 
# ---
# ## Part B — Gradebook (Files, Dicts, Methods)
# 
# You are given `data/scores.csv` with columns: `student_id,name,quiz1,quiz2,quiz3`.
# 
# ### B1. `read_scores_csv(path)`
# Read the CSV and return a list of dictionaries, one per student. Convert quiz scores to `int`.
# 
# ### B2. `compute_averages(records)`
# Given the list from B1, return a **new** list where each dict has added keys:
# - `"avg"`: average of quizzes (float)
# - `"grade"`: result of `letter_grade(avg)`
# 
# ### B3. `write_report(records, out_path="report.txt")`
# Write a simple text report with one line per student:
# `S001 Aye -> avg=9.0 grade=A`
# 
# **Note:** Use `with open(...)` to handle files safely.
# 

# %%

# TODO: B1
import csv

def read_scores_csv(path: str) -> list[dict]:
    
    records = []
    
    with open(path, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            row['quiz1'] = int(row['quiz1'])
            row['quiz2'] = int(row['quiz2'])
            row['quiz3'] = int(row['quiz3'])
            
            records.append(row)
            
    return records
read_scores_csv

# %%

# TODO: B2
def compute_averages(records: list[dict]) -> list[dict]:
    new_records = []
    
    for record in records:
        quiz_avg = (record['quiz1'] + record['quiz2'] + record['quiz3']) / 3
        
        record['avg'] = quiz_avg
        
        record['grade'] = letter_grade(quiz_avg)
        
        new_records.append(record)
        
    return new_records

compute_averages


# %%

# TODO: B3
from pathlib import Path

def write_report(records: list[dict], out_path: str = "report.txt") -> None:
    with open(out_path, 'w') as out_file:
        for record in records:
            line = f"{record['student_id']} {record['name']} -> avg={record['avg']:.1f} grade={record['grade']}\n"
            out_file.write(line)

write_report


# %%

# --- Tests for Part B ---
recs = read_scores_csv("data/scores.csv")
assert isinstance(recs, list) and len(recs) >= 5
assert all(isinstance(r, dict) for r in recs)
assert set(recs[0].keys()) >= {"student_id","name","quiz1","quiz2","quiz3"}
assert all(isinstance(r["quiz1"], int) for r in recs)

recs2 = compute_averages(recs)
assert "avg" in recs2[0] and "grade" in recs2[0]

out_file = "report.txt"
write_report(recs2, out_file)
p = Path(out_file)
assert p.exists() and p.stat().st_size > 0
print("Part B tests passed (if no AssertionError).")


# %% [markdown]
# 
# ---
# ## Part C — Simple Log Analysis (Files, Dicts)
# 
# You are given `data/access.log` with lines: `username,action,timestamp`.
# 
# ### C1. `parse_log(path)`
# Return a list of tuples `(username, action, timestamp_str)`.
# 
# ### C2. `action_counts(parsed)`
# Return a dict `{action: count}` across all lines.
# 
# ### C3. `most_active_user(parsed)`
# Return a tuple `(username, count)` for the user with the most actions. Break ties by lexicographic username (smallest first).
# 

# %%

# TODO: C1
def parse_log(path: str) -> list[tuple]:
    parsed_records = []
    with open(path, 'r', newline='') as logfile:
        reader = csv.reader(logfile)
        for line in reader:
            parsed_records.append(tuple(line))
    return parsed_records

parse_log


# %%

# TODO: C2
def action_counts(parsed: list[tuple]) -> dict:
    counts = {}
    for record in parsed:
        action = record[1]
        counts[action] = counts.get(action, 0) + 1
    return counts
action_counts


# %%

# TODO: C3
def most_active_user(parsed: list[tuple]) -> tuple[str,int]:
    user_counts = {}
    for record in parsed:
        user = record[0]
        user_counts[user] = user_counts.get(user, 0) + 1

    most_active_user = ""
    max_count = -1
    
    for user, count in user_counts.items():
        if count > max_count:
            max_count = count
            most_active_user = user
        elif count == max_count and user < most_active_user:
            most_active_user = user
            
    return (most_active_user, max_count)
most_active_user


# %%

# --- Tests for Part C ---
parsed = parse_log("data/access.log")
assert isinstance(parsed, list) and len(parsed) >= 5
assert all(isinstance(t, tuple) and len(t) == 3 for t in parsed)

counts = action_counts(parsed)
assert isinstance(counts, dict) and sum(counts.values()) == len(parsed)

user, cnt = most_active_user(parsed)
assert isinstance(user, str) and isinstance(cnt, int) and cnt >= 1
print("Part C tests passed (if no AssertionError).")


# %% [markdown]
# 
# ---
# ## Part D — Menu‑Driven CLI (Loops, Conditionals, Methods)
# 
# Write a loop that repeatedly shows this menu until the user chooses Quit:
# 
# ```
# 1) Show top student(s) by average
# 2) Show action counts from access.log
# 3) Export a CSV of student_id,name,avg,grade to data/gradebook_out.csv
# 4) Quit
# ```
# 
# Implement as `main()` that returns `None`. For (1), if multiple students tie for top average, print them all.
# 

# %%

# TODO: D — menu CLI
def main() -> None:
    def main():
     while True:
        print("\n--- Main Menu ---")
        print("1) Show top student(s) by average")
        print("2) Show action counts from access.log")
        print("3) Export a CSV of student,name,avg,grade")
        print("4) Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            # Logic for option 1 goes here
            pass
        elif choice == '2':
            # Logic for option 2 goes here
            pass
        elif choice == '3':
            # Logic for option 3 goes here
            pass
        elif choice == '4':
            print("Quitting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

# %% [markdown]
# 
# ---
# ## Submission checklist
# - [ ] All TODOs completed
# - [ ] Notebook runs top-to-bottom without errors
# - [ ] `report.txt` generated
# - [ ] (Optional) `data/gradebook_out.csv` generated via menu option 3


