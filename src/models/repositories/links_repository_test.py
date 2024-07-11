import pytest
import uuid
from src.models.settings.db_connection_hander import db_connection_handler
from .links_repository import LinksRepository

db_connection_handler.connect()

trip_id  = str(uuid.uuid4())
link_id  = str(uuid.uuid4())

@pytest.mark.skip(reason="Interação com o banco")
def test_registry_link():
    conn = db_connection_handler.get_connection()
    links_infos = LinksRepository(conn)
    

    links_trips_infos = {
        "id": link_id,
        "trip_id": trip_id,
        "link": "https://youtube.com",
        "title":"Viagem para a Orlando"
    }

    links_infos.registry_link(links_trips_infos)

@pytest.mark.skip(reason="Interação com o banco")
def test_find_links_from_trip():
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)

    links = links_repository.find_links_from_trip(trip_id)
    print()
    print(links)

    assert isinstance(links, list)
    assert isinstance(links[0], tuple)
