from datetime import datetime


class Reminder:
   def __init__(self, title, description, due_date, priority):
       # Basic information for the reminder
       self.title = title                  # short title (example: "Study for exam")
       self.description = description      # extra details or notes
       self.due_date = due_date            # when it needs to be done
       self.priority = priority            # 1-5
       self.completed = False              # starts as not done
       self.created_at = datetime.now()    # when the reminder was made


   def show_info(self):
       return {
        "title": self.title,
        "description": self.description,
        "due_date": self.due_date.isoformat(),
        "priority": self.priority,
        "completed": self.completed
        }


   def mark_complete(self):
       # Mark this reminder as completed
       self.completed = True
       print(f"Reminder '{self.title}' marked as done!")


   def edit_reminder(self, new_title=None, new_description=None, new_due_date=None, new_priority=None):
       # Allow the user to change the reminder details
       if new_title:
           self.title = new_title
       if new_description:
           self.description = new_description
       if new_due_date:
           self.due_date = new_due_date
       if new_priority:
           self.priority = new_priority
       print(f"Reminder '{self.title}' updated!")


   def is_overdue(self):
       # Check if the due date has already passed
       now = datetime.now()
       return now > self.due_date