from enum import Enum


class Permission(Enum):
    """Permissions supported by the application."""

    READ = "read"
    WRITE = "write"
    DELETE = "delete"
    ADMIN = "admin"


class UserPermissionError(Exception):
    """Raised when a permission operation is not valid for a user."""


class User:
    """Represent a user and the permissions currently granted to them."""

    def __init__(self, user_name: str):
        """Create a user with READ permission by default."""
        self.user = user_name
        self.permissions: set[Permission] = {Permission.READ}
        self.data: list[str] = []

    def add_permission(self, permission: Permission) -> str:
        """Grant a permission and its lower-level permissions."""
        if permission in self.permissions:
            raise UserPermissionError(
                f"{permission.value} permission already exists for {self.user}."
            )

        if permission == Permission.WRITE:
            self.permissions.add(Permission.WRITE)
        elif permission == Permission.DELETE:
            self.permissions.update({Permission.WRITE, Permission.DELETE})
        elif permission == Permission.ADMIN:
            self.permissions.update(
                {Permission.WRITE, Permission.DELETE, Permission.ADMIN}
            )
        elif permission == Permission.READ:
            self.permissions.add(Permission.READ)

        return f"{permission.value} permission granted to {self.user}."

    def remove_permission(self, permission: Permission) -> str:
        """Remove a permission and any higher permissions that depend on it."""
        if permission not in self.permissions:
            raise UserPermissionError(
                f"{permission.value} permission not found for {self.user}."
            )

        if permission == Permission.READ:
            self.permissions.clear()
        elif permission == Permission.WRITE:
            self.permissions.difference_update(
                {Permission.WRITE, Permission.DELETE, Permission.ADMIN}
            )
        else:
            self.permissions.remove(permission)

        return f"{permission.value} permission removed from {self.user}."

    def check_permission(self, permission: Permission) -> None:
        """Raise an error when the user cannot perform the requested action."""
        if permission not in self.permissions and Permission.ADMIN not in self.permissions:
            raise UserPermissionError(
                f"{permission.value} permission not found for {self.user}."
            )

    def access_me(self) -> str:
        """Return a readable summary of the user's current access level."""
        if Permission.ADMIN in self.permissions:
            return f"{self.user} has FULL permission."
        if Permission.DELETE in self.permissions:
            return f"{self.user} has READ, WRITE and DELETE permission."
        if Permission.WRITE in self.permissions:
            return f"{self.user} has READ and WRITE permission."
        if Permission.READ in self.permissions:
            return f"{self.user} has READ permission."
        return f"{self.user} has NO permission."

    def read_list(self) -> list[str]:
        """Return a copy of the list when READ permission is available."""
        self.check_permission(Permission.READ)
        return self.data.copy()

    def append_item(self, item: str) -> str:
        """Append an item when WRITE permission is available."""
        self.check_permission(Permission.WRITE)
        self.data.append(item)
        return f"Appended '{item}' to list."

    def clear_list(self) -> str:
        """Clear the list when DELETE permission is available."""
        self.check_permission(Permission.DELETE)
        self.data.clear()
        return "List cleared."

    def full_access_reset(self, new_data: list[str]) -> str:
        """Replace the complete list when ADMIN permission is available."""
        self.check_permission(Permission.ADMIN)
        self.data = new_data.copy()
        return "Full list overwrite successful."


class AllUsers:
    """Manage multiple User objects."""

    def __init__(self):
        """Create an empty user collection."""
        self.save_users: list[User] = []

    def add_user(self, user: User) -> str:
        """Store a User object in the collection."""
        self.save_users.append(user)
        return f"User {user.user} added."

    def find_user(self, user_name: str) -> User:
        """Return the stored User object with the requested name."""
        for user in self.save_users:
            if user.user == user_name:
                return user
        raise UserPermissionError(f"User {user_name} not found.")


def run_operation(user: User) -> None:
    """Run all list operations and show which ones are allowed or rejected."""
    print(f"\n--- Operations for {user.user} ---")

    try:
        print(f"[SUCCESS] READ: {user.read_list()}")
    except UserPermissionError as error:
        print(f"[REJECTED] READ: {error}")

    try:
        print(f"[SUCCESS] WRITE: {user.append_item('New Item')}")
    except UserPermissionError as error:
        print(f"[REJECTED] WRITE: {error}")

    try:
        print(f"[SUCCESS] DELETE: {user.clear_list()}")
    except UserPermissionError as error:
        print(f"[REJECTED] DELETE: {error}")

    try:
        print(
            f"[SUCCESS] ADMIN: "
            f"{user.full_access_reset(['Admin Data 1', 'Admin Data 2'])}"
        )
    except UserPermissionError as error:
        print(f"[REJECTED] ADMIN: {error}")


user_1 = User("Subir")
users = AllUsers()
users.add_user(user_1)

run_operation(users.find_user("Subir"))

print(user_1.add_permission(Permission.ADMIN))
run_operation(user_1)
