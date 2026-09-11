# Practical Engineering Questions

This file contains **questions only** for scenario-based engineering practice.

Solutions are intentionally kept outside this file. Once a practical is submitted and reviewed, the question heading can link directly to the submitted solution file.

---

## Practical 01 — Shopping Cart

[Reviewed solution](01-shopping-cart/submitted.py)

Design and implement a small shopping-cart system for an online store.

### Requirements

1. A `Product` should have a name and a price.
2. A `Cart` should be able to hold multiple products.
3. The same product should be allowed to appear multiple times in the cart.
4. Provide a way to add a product to the cart.
5. Provide a way to remove a product from the cart.
6. Provide a way to calculate the total price of the cart.
7. Provide a way to clear the cart completely.
8. Decide what data structure the cart should use and justify the decision in your code design.
9. Handle reasonable invalid operations appropriately.
10. Do not use dictionaries; use only concepts that have already been taught.
11. Use classes where they make sense.
12. Keep the design simple and extensible rather than adding unnecessary abstractions.

### Design Questions

- What objects/classes are needed?
- Which object should own the cart's products?
- Should the cart store `Product` objects, product names, tuples, or something else? Why?
- Which operations should mutate existing objects?
- What should each public method return?
- How should removing a product behave if the product is not in the cart?

---

## Practical 02 — Server Health Monitor

[Reviewed solution](02-server-health-monitor/submitted.py)

Design and implement a small server-health monitoring system.

### Requirements

1. A server should have a name and a health status.
2. Supported statuses are `UP`, `DOWN`, and `MAINTENANCE`.
3. A monitor should manage multiple servers.
4. Provide a way to add a server.
5. Server names must not be duplicated.
6. Provide a way to mark a server as `UP`.
7. Provide a way to mark a server as `DOWN`.
8. Provide a way to find all currently `DOWN` servers.
9. Decide what data structure should be used to store the servers.
10. Do not use dictionaries; use only concepts that have already been taught.
11. Use classes and an enum where appropriate.
12. Keep the design suitable for extending later with additional monitoring behaviour.

### Design Questions

- What objects/classes are needed?
- Which object should own the collection of servers?
- How will duplicate server names be prevented without using a dictionary?
- Should the monitor store server objects directly?
- Which operations should mutate the server or monitor?
- What should happen when an unknown server is marked `UP` or `DOWN`?

---

## Practical 03 — Notification System

Design and implement a small notification system for an application.

### Requirements

1. The application can send notifications through `EMAIL`, `SMS`, and `PUSH`.
2. Use an enum for notification types.
3. A user/application should be able to support multiple notification types.
4. Provide a way to add a notification method.
5. Provide a way to remove a notification method.
6. Provide a way to check whether a notification method is enabled.
7. Do not send notifications through a disabled method.
8. Do not use dictionaries; use only concepts that have already been taught.
9. Use classes where appropriate.
10. Keep the design open to adding another notification type later without rewriting unrelated code.

### Design Questions

- What objects/classes are needed?
- Should notification types be represented as strings or enum members?
- What data structure should hold multiple enabled notification types?
- Which class should be responsible for deciding whether a notification method is enabled?
- What should happen if the caller tries to remove a method that is not enabled?
- How can the design remain simple while still allowing another notification type to be added later?

---

## Practical 04 — Order Processing Summary

**Status: PARKED — prerequisite concept needed before implementation.**

[Scenario details](04-order-processing-summary/question.md)

This practical was intentionally parked after identifying that its duplicate-order requirement depends on idempotent processing. Idempotency has not yet been taught in this learning path, so implementation should resume only after that concept has been covered.

The practical remains available for later completion. No solution is implied by this note.

---

## Practical 05 — Access Permission Manager

[Reviewed solution](05-access-permission-manager/submitted.py)

Design and implement a small access-permission system for an application.

### Requirements

1. A user can have multiple permissions.
2. Supported permissions are `READ`, `WRITE`, `DELETE`, and `ADMIN`.
3. A new user should have `READ` permission by default.
4. `WRITE` includes `READ` access.
5. `DELETE` includes `READ` and `WRITE` access.
6. `ADMIN` includes all permissions.
7. Provide a way to add a permission.
8. Prevent duplicate permissions.
9. Provide a way to remove a permission.
10. Removing `READ` removes all current permissions.
11. Removing `WRITE` removes `WRITE` and any higher permissions that depend on it.
12. Provide a way to check whether a user has a particular permission.
13. Provide a way to view the user's current access level.
14. Handle invalid permission operations with an appropriate custom exception.
15. Use classes and an enum where they make sense.
16. Do not use a database, files, HTTP, or external services.
17. Keep the design simple and suitable for adding another permission later.

### Design Questions

- What objects/classes are needed?
- Which object should own a user's permissions?
- What data structure should hold multiple permissions?
- How should duplicate permissions be prevented?
- Which object should check whether a permission is available?
- What should happen when an unknown permission is requested?
- What should happen when a permission is removed?
- Where should the permission hierarchy rules live?
