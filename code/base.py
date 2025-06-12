from faker import Faker
import pandas as pd

fake = Faker()

for _ in range(10):
    
    user_data = {
        "first_name": fake.first_name(),
        "middle_name": fake.first_name(),
        "last_name": fake.last_name(),
        "address_line1": fake.street_address(),
        "city": fake.city(),
        "state": fake.state(),
        "zip_code": fake.zipcode(),
        "phone": fake.phone_number(),
        "email": fake.email()
    }

    # print(user_data)

    # append each row to a DataFrame
    user_df = pd.DataFrame([user_data])
    if 'user_df' in locals():
        user_df = pd.concat([user_df, user_df], ignore_index=True)
    else:
        user_df = user_df

print(user_df)