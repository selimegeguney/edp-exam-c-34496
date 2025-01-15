class University:
    def __init__(self, name, address, phone_number, email, event_queue):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.event_queue = event_queue
    
    def handle_application(self, event):
        print(f"Received application for Candidate: {event.payload['passport_number']} on {event.payload['date']}")
        result_event = UniversityApplicationResultEvent(event.payload["passport_number"], is_accepted=True)
        self.event_queue.append(result_event)
        print('Event', result_event.name, "emitted")

class Student:
    def __init__(self, first_name, last_name, day_of_birth, phone_number, passport_number, event_queue):
        self.first_name = first_name
        self.last_name = last_name
        self.day_of_birth = day_of_birth
        self.phone_number = phone_number
        self.passport_number = passport_number
        self.event_queue = event_queue

    def university_application(self, date):
        event = UniversityApplicationEvent(self.passport_number, date)
        self.event_queue.append(event)
        print('Event', event.name, 'emitted!')

    def handle_application_result(self, event):
        if event.payload['is_accepted']:
            print("You have Aceepted to our University")
        else:
            print("You have rejected!")
    
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

event_queue = []

student1 = Student("Selim", "Güney", "15.03.2004", "5435361508", "U23456789", event_queue)
university = University("ATA", "Warsaw Olszewszka", "1234567899", "dziekanat@wseiz.edu.pl", event_queue)

student1.university_application("15.01.2025")

while event_queue:
    event = event_queue.pop(0)

    if isinstance(event, UniversityApplicationEvent):
        university.handle_application(event)

    elif isinstance(event, UniversityApplicationResultEvent):
        student1.handle_application_result(event)