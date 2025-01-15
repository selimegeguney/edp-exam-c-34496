class University:
    def __init__(self, name, address, phone_number, email, event_queue):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.event_queue = event_queue
    
    def handle_application(self, event):
        print(f"Received application for Candidate: {event.payload['passport_number']} on {event.payload['date']}")

class Student:
    def __init__(self, first_name, last_name, day_of_birth, gpa, phone_number, passport_number, event_queue):
        self.first_name = first_name
        self.last_name = last_name
        self.day_of_birth = day_of_birth
        self.gpa = gpa
        self.phone_number = phone_number
        self.passport_number = passport_number
        self.event_queue = event_queue

    def university_application(self, date):
        event = UniversityApplicationEvent(self.passport_number, date)
        self.event_queue.append(event)
        print('Event', event.name, 'emmitted!')

class Event:
    def __init__(self, name, payload):
        self.name = name
        self.payload = payload



class UniversityApplicationEvent(Event):
    def __init__(self, passport_number, date):
        super().__init__("application_confirmation", {"passport_number": passport_number, "date": date})

class UniversityApplicationResultEvent(Event):
    def __init__(self, passport_number, is_accepted):
        super().__init__("application_confirmation", {"passport_number": passport_number, "is_accepted": is_accepted})

