events = [
    {"id": 1, "name": "Event 1", "date": "2024-06-22"},
    {"id": 2, "name": "Event 2", "date": "2024-07-15"},
    {"id": 3, "name": "Event 3", "date": "2024-08-30"}
]

def get_event_by_id(event_id):
    for event in events:
        if event['id'] == event_id:
            return event
    return None

event_id = 2
event = get_event_by_id(event_id)
if event:
    print(f"Event found: {event}")
else:
    print("Event not found")
