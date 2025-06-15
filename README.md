![coverage](https://img.shields.io/badge/coverage-72.64%25-blue)
![pylint](https://img.shields.io/badge/pylint-5.66-green)
![Latest Release](https://img.shields.io/badge/release-v1.1.0-blue)
[![PyPi Deployment](https://github.com/ankit48365/MockDataGen/actions/workflows/pypi-publish.yml/badge.svg)](https://github.com/ankit48365/MockDataGen/actions/workflows/pypi-publish.yml)

<h4>Description</h4>

Code to generate synthetic Customer data, usefull to feed into a MDM system for test & validation.

<h4>Usage</h4>

```
mockdatagen --help
mockdatagen --number 10 --print N {generate 10 records and dont print on screen}
```

<h4>Release history</h4>

```
Version 1.0.0 - Date 6/14/2025 { Run CLI Command like mockdatagen --number 10 --print N }
Version 1.1.0 - Date 6/15/2025 { Added Unit test cases, Pylint for quality and github actions}
```

<h4><a href="https://pypi.org/project/mockdatagen/">PyPi.org Link</a></h4>

<h4>Update Badge</h4>

Dynamically update pylint and Test Coverage Badge - Run pylint_badge.sh

<h4>High Level Conceptual Data Flow Diagram:</h4>

![The Idea!!](diagram/version1.png "Data Flow Overview")

<h4>Test Coverage Details:</h4>

[View Coverage Report](htmlcov/function_index.html)

<h4>Draw Project Directory</h4>

```tree /F /A > tree_output.txt```

<h4>Faker Package - Attributes</h4>

```
The Faker library provides a wide range of attributes for generating synthetic data. Here are some commonly used ones:
Personal Information
- fake.name() – Full name
- fake.first_name() – First name
- fake.last_name() – Last name
- fake.prefix() – Name prefix (e.g., Mr., Ms.)
- fake.suffix() – Name suffix (e.g., Jr., Sr.)

Address Details
- fake.address() – Full address (street, city, state, ZIP)
- fake.street_address() – Street address
- fake.city() – City name
- fake.state() – State name
- fake.zipcode() – ZIP code
- fake.country() – Country name
- fake.latitude() – Latitude coordinate
- fake.longitude() – Longitude coordinate

Contact Information
- fake.phone_number() – Phone number
- fake.email() – Email address
- fake.domain_name() – Domain name
- fake.url() – Website URL

Business & Finance
- fake.company() – Company name
- fake.job() – Job title
- fake.credit_card_number() – Credit card number
- fake.currency_code() – Currency code (e.g., USD, EUR)

Miscellaneous
- fake.date_of_birth() – Random date of birth
- fake.ssn() – Social Security Number
- fake.ipv4() – IPv4 address
- fake.ipv6() – IPv6 address
- fake.uuid4() – Unique identifier (UUID)

You can explore more attributes in the official Faker documentation or GeeksforGeeks guide. Let me know if you need specific examples!
```