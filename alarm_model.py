from datetime import datetime, timedelta
import os

ALLOWED_AUDIO_EXTS = {".mp3", ".wav", ".m4a", ".aac", ".ogg"}

class Alarm:
    def __init__(self, time, voice_file_path, repeat, label):
        self.time = time
        self.voice_file_path = voice_file_path
        self.repeat = repeat          # "none", "daily", "weekdays"
        self.label = label
        self.active = True

        self._validate_voice_file(self.voice_file_path)

    def _validate_voice_file(self, path):
        _, ext = os.path.splitext(str(path))
        if ext.lower() not in ALLOWED_AUDIO_EXTS:
            raise ValueError(
                f"File must be one of {sorted(ALLOWED_AUDIO_EXTS)} — got {ext}"
            )

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
