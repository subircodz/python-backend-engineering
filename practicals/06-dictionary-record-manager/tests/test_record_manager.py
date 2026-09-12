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

def test_get_active_users():
    user = RecordManager()
    user.add_record(
            "001", "Subir", "ss@aol.com", "Developer", True
            )
    user.add_record(
            "002", "Subir1", "ss1@aol.com", "Developer", False
            )
    user.add_record(
            "003", "Subir2", "ss2@aol.com", "Developer", True
            )

    # expected 2 records
    assert len(user.get_active_users()) == 2

def test_get_users_by_dept():
    user = RecordManager()
    user.add_record(
            "001", "Subir", "ss@aol.com", "Developer", True
            )

    user.add_record(
            "002", "gray2", "ss@aol.com", "Tester", False
            )
    user.add_record(
            "003", "gray3", "ss@aol.com", "Developer", False
            )
    user.add_record(
            "004", "gray4", "ss@aol.com", "Developer", False
            )
    # expected 3
    users = user.get_users_by_dept("Developer")
    assert len(users) == 3
    assert all(record["department"] == "Developer" for record in users)

def test_remove_user():
    user = RecordManager()
    user.add_record(
            "001", "Subir", "ss@aol.com", "Developer", True
            )

    user.add_record(
            "002", "gray2", "ss@aol.com", "Tester", False
            )
    user.add_record(
            "003", "gray3", "ss@aol.com", "Developer", False
            )
    user.add_record(
            "004", "gray4", "ss@aol.com", "Developer", False
            )
    check = user.remove_user("003")
    assert check == "User ID: 003 removed."

def test_summary():
    user = RecordManager()
    user.add_record(
            "001", "Subir", "ss@aol.com", "Developer", True
            )
    user.add_record(
            "002", "gray2", "ss@aol.com", "Tester", False
            )
    user.add_record(
            "003", "gray3", "ss@aol.com", "Developer", False
            )
    user.add_record(
            "004", "gray4", "ss@aol.com", "Developer", False
            )
    test_result = user.summary()
    assert test_result == (
            "Total Users   : 4"
            "\nActive Users  : 1"
        )


