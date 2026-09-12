from typing import Any


class UserKeyError(Exception):
    pass

class RecordManager:
    def __init__(self):
        self.records: list[dict] = []

    def add_record(
            self, 
            user_id: str, 
            name: str, 
            email: str, 
            department: str, 
            active: bool
            ) -> str:
        """
        Adds a user record if it does not exist.

        Args:
            user_id: The user id of the user.
            name: The name of the user.
            email: The email of the user.
            department: The department of the user.
            active: The active status of the user in True or False

        Returns:
            A message that the user is added if no duplicate
            record found.

        Raises:
            ValueError: If the user record already exist.
        """
        user_record = self.get_record(user_id)

        if user_record is not None:
            raise ValueError(
                f"Record with user_id {user_id} already exists."
                )
        
        record = {
            "user_id": user_id,
            "name": name,
            "email": email,
            "department": department,
            "active": active
        }

        self.records.append(record)
        return f"Record with user_id {user_id} added."

    def get_record(self, user_id: str) -> dict | None:
        """
        Receives an user id and returns the record of the user id
        if exists, otherwise returns None.

        Args:
            user_id: The user id for which to get the record.

        Returns:
            The record for the user id if found.
        """
        for record in self.records:
            if record["user_id"] == user_id:
                return record
        return None

    def update_records(self, **kwargs: Any) -> str:
        """
        Receives a dictionary containing fields to be updated 
        for a record, and updates the dictionary if User ID
        found.

        Args:
            **kwargs: The dictionary containing the updated 
            fields.

        Returns:
            A message that the record has been updated if 
            record found.

        Raises:
            UserKeyError: If record not found with the user_id.
        """
        fetch_record = self.get_record(kwargs['user_id'])
        if fetch_record is None:
            raise UserKeyError(
                f"User ID: {kwargs['user_id']} not found."
                )
        for key in fetch_record:
            if key in kwargs:
                fetch_record[key] = kwargs[key]
        return (
            f"Record with ID {kwargs['user_id']} "
            f"updated."
            )

    def get_active_users(self) -> list[dict]:
        """
        Provides all active users if found else returns empty
        list.

        Returns:
            The records if active users found else returns 
            empty list.
        """
        active_users: list[dict] = []
        for record in self.records:
            if record["active"]:
                active_users.append(record)
        return active_users

    def get_users_by_dept(self, dept: str) -> list[dict]:
        """
        Returns all records by department. Returns empty list 
        if no records found.

        Args:
            dept: The department name by which records are to 
            to be provided.

        Returns:
            The list of records for the department.
        """
        users_in_dept: list[dict] = []
        for record in self.records:
            if record['department'] == dept:
                users_in_dept.append(record)
        return users_in_dept

            


user = RecordManager()
result = user.add_record(
        "001", "Subir", "ss@aol.com", "Developer", True
        )

result2 = user.add_record(
        "002", "gray2", "ss@aol.com", "Tester", False
        )
result3 = user.add_record(
        "003", "gray3", "ss@aol.com", "Developer", False
        )
result4 = user.add_record(
        "004", "gray4", "ss@aol.com", "Developer", False
        )
print(user.get_users_by_dept("Developer"))

    