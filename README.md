
# Drink Partners API

REST API responsible for managing partners

# Install dependencies

1. Create virtualenv:
    virtualenv drink_partner -p python3

2. Install dependencies using `pip`

```bash
 make requirements-dev
```

## Tests

1. To run all suite tests:

```bash
make test
```

2. To execute specific tests:

```bash
make test-matching Q=[test_name_or_test_class_name] 
```

3. To execute test coverage:

```bash
make coverage
```
