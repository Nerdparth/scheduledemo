from ninja import Router
from .schemas import EventSchema
import httpx

router = Router()


@router.post("/schedule-event")
def schedule_event(request, data: EventSchema):
    url = "https://api.calendly.com/scheduled_events"

    headers = {
        "Authorization": "Bearer YOUR_CALENDLY_API_KEY",
        "Content-Type": "application/json",
    }

    body = {
        "event_type": "One-on-one",
        "invitee": {"name": data.name, "email": data.email},
        "start_time": data.start_time,
        "end_time": data.end_time,
    }

    response = httpx.post(url, headers=headers, json=body)

    if response.status_code == 201:
        return {"message": "Event scheduled successfully", "data": response.json()}
    else:
        return {"message": "Failed to schedule event", "error": response.text}
