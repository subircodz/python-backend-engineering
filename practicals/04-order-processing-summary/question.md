# Practical 04 — Order Processing Summary

Design and implement a small order-processing component for an application.

The application receives order records from an upstream service. Each order contains an order ID, customer ID, status, and item information. The component must process these records and produce useful summaries for another part of the application.

## Requirements

1. Each order has a unique order ID.
2. Each order belongs to a customer.
3. Each order has a status such as `pending`, `paid`, or `cancelled`.
4. Each order contains one or more product entries with a product name and quantity.
5. The input may contain repeated customer IDs because one customer can have multiple orders.
6. Produce a summary of orders grouped by customer.
7. Produce a count of orders for each status.
8. The component must be able to add another batch of orders to the existing processed data.
9. Missing optional fields should not unnecessarily break processing, but required fields should be treated differently from optional fields.
10. The original input records should not be modified while producing the summaries.
11. Handle duplicate order IDs appropriately.
12. Keep the design simple. Do not add a database, file handling, HTTP calls, or framework code.
13. Use only Python concepts that have been taught so far.

## Design Questions

- What objects or functions are needed?
- What should own the processed order information?
- Which data structures should be used for the different summaries, and why?
- How should repeated customer IDs be handled?
- How should missing optional information differ from a missing required field?
- What should happen when the same order ID appears again?
- Which operations mutate existing data, and which should create new data?
- How should another batch be merged into the existing processed information?
- Where would automatic default creation be useful, if at all?
- How will you make sure the source records are not changed?

## Constraint

Do **not** assume that a particular dictionary type, method, class, or data structure is the expected answer. Choose the design yourself and explain why it fits the problem.
