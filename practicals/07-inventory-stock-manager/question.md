# Practical 07 — Inventory Stock Manager

## Scenario

Build a small in-memory inventory manager for an application that keeps track of products and their stock.

Each product record contains:

- `product_id`
- `name`
- `category`
- `price`
- `stock`
- `active`

The manager must keep products in memory and provide operations to:

1. Add a new product.
2. Prevent duplicate `product_id` values.
3. Find a product by `product_id`.
4. Increase or decrease the stock of an existing product.
5. Return all products whose stock is at or below a requested threshold.
6. Return products grouped by category.
7. Deactivate a product so it is no longer considered available for sale.
8. Return a summary containing total products, active products, and total units in stock.
9. Remove a product by `product_id`.

## Rules

- Use dictionaries as the main data structure.
- You may use lists and sets where they make sense.
- Do not use a database, files, HTTP, or external libraries.
- The manager should retain the product records.
- Unknown products must be handled cleanly.
- Duplicate products must not be created.
- Stock updates must affect the existing product record.
- A product cannot have negative stock.
- Deactivated products remain stored but are not considered active products.
- Choose the internal storage structure yourself.
- Use classes where they make sense.
- Use exceptions where they make sense.
- Do not use comprehensions, `all()`, or `any()`; those will be introduced later in the learning track.

## Design Questions

Before coding, decide:

1. What should the internal storage structure be, and why?
2. What should one stored product record look like?
3. How will duplicate `product_id` values be detected?
4. How will stock be increased and decreased?
5. What should happen when a stock decrease would make stock negative?
6. How will low-stock products be selected without changing the stored records?
7. How will products be grouped by category?
8. What should happen when an unknown product is requested?
9. Should deactivation delete the product or change its stored state? Why?
10. What should each public method return?
11. Which operations should mutate existing records, and which should build new result collections?

## Expected Focus

This practical is an additional practice problem after completing the Dictionary track.

The goal is to reinforce dictionary-based records, nested data handling, iteration, filtering, mutation, grouping, list/set usage, classes, exceptions, and clean method design in a new scenario.

Do not add database, API, framework, typing, logging, comprehensions, `all()`, `any()`, or advanced architecture. The solution should use only concepts already taught in the learning track.
