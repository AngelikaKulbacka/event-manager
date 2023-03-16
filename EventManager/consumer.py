import asyncio
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "EventManager.settings")

import django
django.setup()

from django.core.management import call_command

import faust
from datetime import datetime
from events.models import Event

app = faust.App('event-consumer', broker='kafka://localhost:9092')
events_topic = app.topic('events')

class FaustEvent(faust.Record):
    name: str
    uuid: str
    source: str
    created_at: datetime
    updated_at: datetime
    description: str

@app.agent(events_topic)
async def process_events(events):
    async for event_data in events:
        event = Event(
            name=event_data['name'],
            uuid=event_data['uuid'],
            source=event_data['source'],
            created_at=datetime.strptime(event_data['created_at'], '%Y-%m-%d %H:%M:%S.%f %z'),
            updated_at=datetime.strptime(event_data['updated_at'], '%Y-%m-%d %H:%M:%S.%f %z') if event_data['updated_at'] else None,
            description=event_data['description']
        )

        event.save()

async def consume_events():
    async with app:
        await app.start()
        try:
            await app.wait_for_stopped()
        except asyncio.CancelledError:
            pass

if __name__ == '__main__':
    try:
        asyncio.run(consume_events())
    except KeyboardInterrupt:
        print('Shutting down gracefully...')