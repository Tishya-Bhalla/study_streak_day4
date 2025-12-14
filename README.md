# Study Streak Tracker — Day 4 

Day 4 

This project introduces **data persistence and feedback**, a tool that **remembers progress across runs**.
It logs daily study sessions, tracks streaks, and provides simple audio feedback
to make the experience feel more real.

---

##  What this app does
- Logs daily study sessions (date + minutes)
- Stores data in a local file so progress is remembered
- Calculates:
  - total study time
  - number of sessions
  - current day streak
- Plays a short **beep sound** when a session is successfully logged
- Displays a clear summary after each run

---

## Concepts practiced
- File I/O (`read` / `write`)
- JSON data persistence
- Dates and streak logic
- Basic analytics from stored data
- User feedback via audio
- Building systems that persist across runs

---

##  How to run
```bash
python study_streak.py

## Author- Tishya Bhalla
