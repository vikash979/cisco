from datetime import datetime, timedelta
from cal_setup import get_calendar_service


def createevent():
   # creates one hour event tomorrow 10 AM IST
   service = get_calendar_service()

   d = datetime.now().date()
   tomorrow = datetime(d.year, d.month, d.day, 15)+timedelta(days=6)
   start = tomorrow.isoformat()
   end = (tomorrow + timedelta(hours=1)).isoformat()
   event_result = service.events().insert(calendarId='primary',
       body={
           "summary": 'chhat Puja',
           "description": 'This is a tutorial example of automating google calendar with python',
           "start": {"dateTime": start, "timeZone": 'Asia/Kolkata'},
           "end": {"dateTime": end, "timeZone": 'Asia/Kolkata'},
       }
   ).execute()
   print("summary: ", event_result['summary'])
   print("id: ", event_result['id'])
   print("starts at: ", event_result['start']['dateTime'])
   print("ends at: ", event_result['end']['dateTime'])



createevent()
