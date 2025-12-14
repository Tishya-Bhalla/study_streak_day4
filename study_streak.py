import json
import os
from datetime import date, timedelta

# Windows-only beep (safe for you)
try:
    import winsound
    def beep():
        winsound.Beep(1000, 500)  # frequency, duration
except ImportError:
    def beep():
        pass

DATA_FILE = "study_data.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"sessions": []}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def calculate_streak(sessions):
    if not sessions:
        return 0

    dates = sorted({date.fromisoformat(s["date"]) for s in sessions})
    streak = 1
    for i in range(len(dates) - 1, 0, -1):
        if dates[i] - dates[i - 1] == timedelta(days=1):
            streak += 1
        else:
            break
    return streak

def summary(data):
    total_minutes = sum(s["minutes"] for s in data["sessions"])
    streak = calculate_streak(data["sessions"])

    print("\n📊 Summary")
    print(f"Total sessions logged: {len(data['sessions'])}")
    print(f"Total study time: {total_minutes} minutes")
    print(f"Current streak: {streak} day(s)")
    print(f"Data saved in: {os.path.abspath(DATA_FILE)}")

def main():
    print("📚 Study Streak Tracker — Day 4")
    minutes = input("How many minutes did you study today? ").strip()

    if not minutes.isdigit() or int(minutes) <= 0:
        print("Please enter a valid positive number.")
        return

    minutes = int(minutes)
    today = date.today().isoformat()

    data = load_data()
    data["sessions"].append({
        "date": today,
        "minutes": minutes
    })
    save_data(data)

    beep()
    print("✅ Session logged successfully!")
    summary(data)

if __name__ == "__main__":
    main()
