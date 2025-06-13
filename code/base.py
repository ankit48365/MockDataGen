from faker import Faker
from tabulate import tabulate
import pandas as pd

fake = Faker()

def main():
    pass


def generate_user_data(num_of_records: int) -> pd.DataFrame:
    
    user_data = [{
        "first_name": fake.first_name(),
        "middle_name": fake.first_name(),
        "last_name": fake.last_name(),
        "address": fake.street_address(),
        "city": fake.city(),
        "state": fake.state(),
        "zip_code": fake.zipcode(),
        "phone": fake.phone_number(),
        "email": fake.email()
    } for _ in range(num_of_records)
    ]

    user_df = pd.DataFrame(user_data)

    return user_df

def print_user_data(records_to_print: int) -> None:
    user_df = generate_user_data(records_to_print)
    print(tabulate(user_df, headers='keys', tablefmt='psql', showindex=False)) # grid


if __name__ == "__main__":

    num_of_records = int(input("Enter the number of records to generate: "))
    print_user_data(num_of_records)










# def generate_address_variations(base_address):
#     variations = [
#         base_address,
#         base_address.replace("Street", "St."),
#         base_address.replace("Avenue", "Ave."),
#         base_address.replace("Road", "Rd."),
#         base_address.replace("Boulevard", "Blvd."),
#         base_address.lower().title(),  # Capitalize properly

# does fake has street address2?
