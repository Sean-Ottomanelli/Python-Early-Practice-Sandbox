#this code can be accessed by typing "python meeting.py" into the command line

attendees = ["Ken", "Alena", "Treasure"]
attendees.append("Ashley")
attendees.extend(["James", "Guil"])
optional_invitees = ["Ben J", "Dave"]
potential_attendees = attendees + optional_invitees
print("There are", len(potential_attendees), "attendees currently")