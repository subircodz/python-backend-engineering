# Practical 06 — Dictionary Record Manager

## Scenario

Build a small in-memory record manager for a backend service.

The service receives user records as dictionaries. Each record contains:

- `user_id`
- `name`
- `email`
- `department`
- `active`

The manager must keep records in memory and provide operations to:

1. Add a new user record.
2. Prevent duplicate `user_id` values.
3. Find a user by `user_id`.
4. Update selected fields of an existing user.
5. Return all active users.
6. Return users grouped by department.
7. Remove a user by `user_id`.
8. Return a useful summary containing the total number of users and the number of active users.

## Rules

- Use dictionaries as the main data structure.
- Do not use a database, files, HTTP, or external libraries.
- The manager should retain the records; callers should not have to maintain a second copy of the data.
- Unknown users must be handled cleanly.
- Invalid records must not partially modify the stored data.
- Updating a user may change only the fields supplied by the caller.
- Duplicate users must not be created.
- Choose the internal dictionary structure yourself.
- Use classes where they make sense.
- Use exceptions where they make sense.

## Design questions

Before coding, decide:

1. What should the main dictionary key be?
2. What should one stored record look like?
3. Who owns the records?
4. How will duplicate `user_id` values be detected?
5. How will partial updates work?
6. When should `get()` be useful, and when should `[]` be useful?
7. How will grouping by department work?
8. What should happen when a requested user does not exist?
9. How will you make sure an invalid record does not leave a half-updated state?
10. What should public methods return: the stored dictionary, a new dictionary, a list, a count, or a message?

## Expected focus

This practical is the final checkpoint for the Dictionary track.

The main goal is not to build a large system. The goal is to show that dictionary operations can be combined to solve a small backend data-management problem cleanly.

Do not add database, API, framework, typing, logging, or advanced architecture unless needed for the solution.
