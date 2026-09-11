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
        self.permissions: list[Permission] = [Permission.READ]

    def add_permission(self, permission: Permission) -> str:
        """Grant a permission and its lower-level permissions to the user."""
        if permission in self.permissions:
            raise UserPermissionError(
                f"{permission.value} permission already exists "
                f"for {self.user}."
            )

        if permission == Permission.WRITE:
            self.permissions.append(Permission.WRITE)

        elif permission == Permission.DELETE:
            self.permissions.extend(
                [Permission.WRITE, Permission.DELETE]
            )

        elif permission == Permission.ADMIN:
            self.permissions.extend(
                [
                    Permission.WRITE,
                    Permission.DELETE,
                    Permission.ADMIN,
                ]
            )

        return (
            f"{permission.value} permission granted "
            f"to {self.user}."
        )

    def remove_permission(self, permission: Permission) -> str:
        """Remove a permission and any higher permissions that depend on it."""
        if permission not in self.permissions:
            raise UserPermissionError(
                f"{permission.value} permission not found "
                f"for {self.user}."
            )

        if permission == Permission.READ:
            self.permissions.clear()

        elif permission == Permission.WRITE:
            self.permissions = [
                existing_permission
                for existing_permission in self.permissions
                if existing_permission not in (
                    Permission.WRITE,
                    Permission.DELETE,
                    Permission.ADMIN,
                )
            ]

        elif permission == Permission.DELETE:
            self.permissions.remove(Permission.DELETE)

        elif permission == Permission.ADMIN:
            self.permissions.remove(Permission.ADMIN)

        return (
            f"{permission.value} permission removed "
            f"from {self.user}."
        )

    def check_permission(self, permission: Permission) -> str:
        """Check whether the user currently has the requested permission."""
        if permission in self.permissions:
            return (
                f"{self.user} has "
                f"{permission.value} permission."
            )

        raise UserPermissionError(
            f"{permission.value} permission not found "
            f"for {self.user}."
        )

    def access_me(self) -> str:
        """Return a readable summary of the user's current access level."""
        if Permission.ADMIN in self.permissions:
            return f"{self.user} has FULL permission."

        if Permission.DELETE in self.permissions:
            return (
                f"{self.user} has "
                f"READ, WRITE and DELETE permission."
            )

        if Permission.WRITE in self.permissions:
            return f"{self.user} has READ and WRITE permission."

        if Permission.READ in self.permissions:
            return f"{self.user} has READ permission."

        return f"{self.user} has NO permission."


user_1 = User("Subir")

print(user_1.permissions)
print(user_1.add_permission(Permission.WRITE))
print(user_1.add_permission(Permission.DELETE))
print(user_1.permissions)
print(user_1.access_me())
print(user_1.remove_permission(Permission.DELETE))
print(user_1.permissions)
print(user_1.access_me())
