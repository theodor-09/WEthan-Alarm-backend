# storage.py
# Simple JSON storage for Alarm and Reminder objects.
# Uses ISO timestamps because JSON can't store datetime objects directly.

from alarm_model import Alarm    # only if you have an alarm class
from reminder_model import Reminder



from datetime import datetime
import json, os

# ---------- Alarm helpers ----------

def _serialize_alarm(a):
    return {
        "time": a.time.isoformat(),
        "voice_file_path": a.voice_file_path,
        "repeat": a.repeat,
        "label": a.label,
        "active": a.active,
    }

def _deserialize_alarm(d, AlarmClass):
    a = AlarmClass(
        time=datetime.fromisoformat(d["time"]),
        voice_file_path=d["voice_file_path"],
        repeat=d["repeat"],
        label=d["label"],
    )
    a.active = d.get("active", True)
    return a

# ---------- Reminder helpers ----------

def _serialize_reminder(r):
    return {
        "title": r.title,
        "description": r.description,
        "due_date": r.due_date.isoformat(),
        "priority": r.priority,
        "completed": r.completed,
        "created_at": r.created_at.isoformat(),
    }

def _deserialize_reminder(d, ReminderClass):
    r = ReminderClass(
        title=d["title"],
        description=d["description"],
        due_date=datetime.fromisoformat(d["due_date"]),
        priority=d["priority"],
    )
    r.completed = d.get("completed", False)
    # keep original created_at if present
    if "created_at" in d:
        r.created_at = datetime.fromisoformat(d["created_at"])
    return r

# ---------- Repository ----------

class Repository:
    def __init__(self, path="data.json"):
        self.path = path

    def save(self, alarms, reminders):
        data = {
            "alarms": [_serialize_alarm(a) for a in alarms],
            "reminders": [_serialize_reminder(r) for r in reminders],
        }
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        print(f"[SAVE] {len(alarms)} alarms, {len(reminders)} reminders -> {self.path}")

    def load(self, AlarmClass, ReminderClass):
        if not os.path.exists(self.path):
            print(f"[LOAD] {self.path} not found. Returning empty lists.")
            return [], []
        with open(self.path, "r", encoding="utf-8") as f:
            data = json.load(f)
        alarms = [_deserialize_alarm(d, AlarmClass) for d in data.get("alarms", [])]
        reminders = [_deserialize_reminder(d, ReminderClass) for d in data.get("reminders", [])]
        print(f"[LOAD] {len(alarms)} alarms, {len(reminders)} reminders <- {self.path}")
        return alarms, reminders
