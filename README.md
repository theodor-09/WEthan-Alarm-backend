# WEthan Alarm and Reminder Backend (Python)
This folder contains the **Python backend** for our Alarm & Reminder MVP project, developed for the **Algorithms & Data Structures** course.

The backend provides:

- A simple **HTML homepage**
- A fully interactive **API interface** at `/docs` (Swagger UI)
- Functionality to create and store **reminders** and **alarms**
- A **custom Quicksort algorithm** to sort reminders by urgency
- Automatic persistence using `data.json`
- Audio playback capabilities
---

#  Features

##  Alarms
- Create alarms with:
  - Time (ISO format)
  - Label
  - Repeat mode (`none`, `daily`, `weekdays`)
  - Voice intensity level (1 = funny, 2 = serious, 3 = motivational)
  - Activation flag
- View all alarms in JSON format.
- Play a voice alarm based on its intensity level (funny, serious, motivational)

##  Reminders
- Create reminders with:
  - Title  
  - Description  
  - Due date (`YYYY-MM-DD HH:MM`)  
  - Priority (1–5)
- View all reminders
- View reminders **sorted by urgency** using our custom **Quicksort algorithm**.

##  Data Storage
All reminders and alarms are saved in data.json.
This file is automatically loaded at startup and updated after every change.

---

## 1. Custom Quicksort Algorithm (Divide & Conquer + Recursion)

**File:** `sorting.py`  
**Used in endpoint:** `/sortedReminders`

Our Quicksort implementation:

- Selects a random **pivot**
- Partitions items into `less` and `greater` lists based on urgency
- Recursively sorts both halves
- Combines them into a sorted list

### Time Complexity
- **O(n log n)** average  
- **O(n²)** worst case  
- Demonstrates recursive **Divide & Conquer**

## 2. Hash Table (Python `dict`)

Inside quicksort we compute urgency using:
u_cache = {id(t): urgency(t) for t in tasks}

## Installation & Execution
## Instalation
 - Extract the ZIP folder
     - Open the Expoapp_Python folder
     - Install dependencies (first time only)
         - Open a terminal inside this folder(right click inside folder) and run: pip install -r requirements.txt
           -![install req](https://github.com/theodor-09/WEthan-Alarm-backend/blob/main/Screenshot%202025-12-01%20151707.png)
           -It should look like this:
           -![install_out](https://github.com/theodor-09/WEthan-Alarm-backend/blob/main/Screenshot%202025-12-01%20151731.png)
     - Start the backend
        - run_backend.py by double click
           -It should look like this:
           -![running](https://github.com/theodor-09/WEthan-Alarm-backend/blob/main/Screenshot%202025-12-01%20152914.png)
        - you should see Uvicorn running on http://127.0.0.1:8000
           - open the aplication on http://127.0.0.1:8000/
             -![opened](https://github.com/theodor-09/WEthan-Alarm-backend/blob/main/Screenshot%202025-11-30%20205300.png)
           - press Interactive API Interface (front-end)
             -![API](https://github.com/theodor-09/WEthan-Alarm-backend/blob/main/Screenshot%202025-11-30%20203240.png)
  ## How to use the API
  - Check backend status: GET /status, Try it out, Execute
      - expected response body : {"status": "Wethan backend running!"}
  - Create a reminder
     - open: POST /createReminder
     - Example input: {"title": "Study","description": "ADS topics","due_date": "2025-12-01 14:00", "priority": 3}
   - View all reminders
       - open: GET /allReminders
   - Create an Alarm
       - open: POST /createAlarm
       - Example input: {"time": "2025-12-08T07:00:00","voice_level": 2,"repeat": "weekdays","label": "Morning Motivation"}
       - Play an alarm
         - open: GET /playAlarm
         - Copy the returned "id" value from createAlarm or allAlarms and play
       - View all alarms
         - open: GET /allAlarms
         - This lists all stored alarms.
      
## Further Improvements
  - Implement snooze and skip states for alarms
  - Import class schedules (ICS)
  - Upgrade JSON storage to SQLite
  - Authentication system
  - More advanced front-end

## Credits
 - Team Members: MÁTÉ ANTAL, THEODOR-GABRIEL DAVID,ETHAN BENJAMIN ARTHUR JESSUP, BARTOLOMÉ MARÍA URDA, DAVID HYEON PARRAGA, MAXIMILIAN BIATTURI
 - Course: Algorithms and Data Structure
 - Professor: ANTONIO LÓPEZ ROSELL

## Bibliography
 - FastAPI Documentation – https://fastapi.tiangolo.com
 - Python Documentation – https://docs.python.org
 - ADS Course Slides – Recursion, Divide & Conquer, Sorting
 - Uvicorn ASGI Server – https://www.uvicorn.org


