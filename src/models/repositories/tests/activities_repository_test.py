import pytest
import uuid
from src.models.settings.db_connection_hander import db_connection_handler
from ..activities_repository import ActivitiesRepository
from datetime import datetime

db_connection_handler.connect()

activity_id  = str(uuid.uuid4())
trip_id  = str(uuid.uuid4())


def test_registry_activity():
    conn = db_connection_handler.get_connection()
    activities_repository = ActivitiesRepository(conn)
    

    activity_infos = {
        "id": activity_id,
        "trip_id": trip_id,
        "title": "Passeio de Canoa por Canoa Quebrada",
        "occurs_at": datetime.strptime("02-01-2026", "%d-%m-%Y")
    }

    activities_repository.registry_activity(activity_infos)


def test_find_emails_from_trip():
    conn = db_connection_handler.get_connection()
    activities_repository = ActivitiesRepository(conn)

    activities = activities_repository.find_activities_from_trip(trip_id)
    print()
    print(activities)