from record_manager import RecordManager


def test_add_record():
    user = RecordManager()
    result = user.add_record(
        "001", "Subir", "ss@aol.com", "Developer", True
        )
    assert result == "Record with user_id 001 added."
    # user.get_record("001")
