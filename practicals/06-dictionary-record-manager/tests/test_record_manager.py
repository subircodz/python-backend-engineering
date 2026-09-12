import pytest
from record_manager import RecordManager


def test_add_record():
    user = RecordManager()
    result = user.add_record(
        "001", "Subir", "ss@aol.com", "Developer", True
        )
    assert result == "Record with user_id 001 added."
    record = user.get_record("001")
    assert record == {'user_id': '001', 'name': 'Subir', 'email': 'ss@aol.com', 'department': 'Developer', 'active': True}


def test_update_record():
    user = RecordManager()
    user.add_record(
        "001", "Subir", "ss@aol.com", "Developer", True
        )
    update = user.update_records(
    user_id="001",
    name="gray",
    email="foo@spam.com"
    )
    assert update == "Record with ID 001 updated."

