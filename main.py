from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from reminder_model import Reminder
from alarm_model import Alarm
from sorting import quicksort
from storage import Repository  
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from fastapi import HTTPException
from fastapi.responses import FileResponse

app = FastAPI()
# Mount static audio folder
BASE_DIR = Path(__file__).parent
audio_path = BASE_DIR / "audio"
app.mount("/audio", StaticFiles(directory=audio_path), name="audio")
@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <html>
      <head><title>Alarm & Reminder Backend</title></head>
      <body>
        <h1>Alarm & Reminder Backend</h1>
        <p>The backend is running correctly.</p>
        <p>Use the <a href="/docs">interactive API interface</a> to test endpoints.</p>
      </body>
    </html>
    """
# -----------------------------------------
# LOAD SAVED DATA FROM JSON AT STARTUP
# -----------------------------------------
repo = Repository("data.json")
alarms, reminders = repo.load(Alarm, Reminder)

# --------------------------
# REMINDERS
# --------------------------

class ReminderRequest(BaseModel):
    title: str
    description: str
    due_date: str
    priority: int

@app.get("/status")
def status():
    return {"status": "Wethan backend running!"}

@app.post("/createReminder")
def create_reminder(data: ReminderRequest):
    due_date = datetime.strptime(data.due_date, "%Y-%m-%d %H:%M")

    reminder = Reminder(
        title=data.title,
        description=data.description,
        due_date=due_date,
        priority=data.priority
    )

    # SAVE NEW REMINDER
    reminders.append(reminder)
    repo.save(alarms, reminders)   # ← ADD THIS

    return {
        "status": "success",
        "reminder": reminder.show_info()
    }


@app.get("/allReminders")
def get_all():
    return [r.show_info() for r in reminders]

# --------------------------
# ALARMS
# --------------------------

VOICE_FILES = {
    1: "funny.mp4",          
    2: "Serious.m4a",        
    3: "Motivational 2.m4a"   
}

class AlarmRequest(BaseModel):
    time: str               # ISO string
    voice_level: int
    repeat: str
    label: str

@app.post("/createAlarm")
def create_alarm(data: AlarmRequest):
    alarm = Alarm(
        time=datetime.fromisoformat(data.time),
        voice_level=data.voice_level,
        repeat=data.repeat,
        label=data.label
    )

    alarms.append(alarm)
    repo.save(alarms, reminders)
    return {
        "status": "success",
        "alarm": {
            "label": alarm.label,
            "time": alarm.time.isoformat(),
            "voice_level": alarm.voice_level,
            "repeat": alarm.repeat,
            "active": alarm.active
        }
    }


@app.get("/playAlarm/{alarm_id}")
def play_alarm(alarm_id: int):
    for alarm in alarms:
        if getattr(alarm, "id", None) == alarm_id:
            file_name = VOICE_FILES.get(alarm.voice_level)
            if not file_name:
                raise HTTPException(status_code=400, detail="Invalid voice level")
            return FileResponse(path=audio_path / file_name, media_type="audio/mp4")
    raise HTTPException(status_code=404, detail="Alarm not found")

@app.get("/allAlarms")
def get_alarms():
    return {"alarms": [a.to_dict() for a in alarms]}





@app.get("/sortedReminders")
def get_sorted():
    sorted_list = quicksort(reminders)
    return [
        {
            "title": r.title,
            "description": r.description,
            "due_date": r.due_date.isoformat(),
            "priority": r.priority,
            "completed": r.completed
        }
        for r in sorted_list
    ]
