# Mock Data Gen

Code to generate synthetic Customer data, usefull to feed into a MDM system for validation.

<h4>High Level Conceptual Data Flow Diagram:</h4>

![The Idea!!](diagram/version1.png "Data Flow Overview")


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
