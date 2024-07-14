import pytest
import uuid
from ..participants_repository import ParticipantsRepository
from src.models.settings.db_connection_hander import db_connection_handler

db_connection_handler.connect()
participant_id  = str(uuid.uuid4())
trip_id  = str(uuid.uuid4())

@pytest.mark.skip(reason="Interação com o banco")
def test_create_participants():
    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn)

    participant_infos = {
        "id": participant_id,
        "trip_id": trip_id,
        "emails_to_invite_id":str(uuid.uuid4()),
        "name": "Jonas"
    }

    participants_repository.registry_participants(participant_infos)

@pytest.mark.skip(reason="Interação com o banco")
def test_find_participants_from_trip():
    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn)

    participants = participants_repository.find_participants_from_trip(trip_id)
    print()
    print(participants)