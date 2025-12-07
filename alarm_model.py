from datetime import datetime, timedelta
import os
from pydantic import BaseModel
from typing import Optional
from uuid import uuid4

ALLOWED_AUDIO_EXTS = {".mp3", ".wav", ".m4a", ".aac", ".ogg"}

class Alarm():
    def __init__(self, time, voice_level, repeat, label):
        self.id = str(uuid4())
        self.time = time
        self.voice_level = voice_level
        self.repeat = repeat          # "none", "daily", "weekdays"
        self.label = label
        self.active = True

    def show_info(self):
        return {
            "label": self.label,
            "time": self.time.isoformat(),
            "voice_file": self.voice_file_path,
            "repeat": self.repeat,
            "active": self.active
        }

    def snooze(self, minutes):
        self.time = self.time + timedelta(minutes=minutes)

    def dismiss(self):
        self.active = False

    # ✅ FIXED INDENTATION — proper to_dict()
    def to_dict(self):
        return {
            "label": self.label,
            "time": self.time.isoformat(),
            "voice_file_path": self.voice_file_path,
            "repeat": self.repeat,
            "active": self.active,
        }
