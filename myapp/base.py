from faker import Faker
from tabulate import tabulate
import pandas as pd

fake = Faker()


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

def print_user_data(records_to_process: int) -> None:
    user_df = generate_user_data(records_to_process)
    print(tabulate(user_df, headers='keys', tablefmt='psql', showindex=False)) # grid

def csv_user_data(records_to_process: int, filename: str = "user_data.csv") -> pd.DataFrame:
    user_df = generate_user_data(records_to_process)
    user_df.to_csv(filename, index=False)
    print(f"User data saved to {filename}")
    return user_df

def mdm_split_data_set(records_to_process: int) -> None:
    user_df = csv_user_data(records_to_process)
    df_20 = user_df.sample(frac=0.2, random_state=42)  # Pick 20% randomly
    df_80 = user_df.drop(df_20.index)  # Remaining 80%  , droping the one used in df_20
    df_20.to_csv("user_data_20.csv", index=False)
    df_80.to_csv("user_data_80.csv", index=False)


if __name__ == "__main__":

    num_of_records = int(input("Enter the number of records to generate: "))
    print_user_data(num_of_records)
    mdm_split_data_set(num_of_records)










# def generate_address_variations(base_address):
#     variations = [
#         base_address,
#         base_address.replace("Street", "St."),
#         base_address.replace("Avenue", "Ave."),
#         base_address.replace("Road", "Rd."),
#         base_address.replace("Boulevard", "Blvd."),
#         base_address.lower().title(),  # Capitalize properly

# does fake has street address2?
