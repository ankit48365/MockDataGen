from faker import Faker
from tabulate import tabulate
import pandas as pd
import random


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
    print(f"Number of records in main set: {user_df.shape[0]}")
    print(f"Number of Unique Records in main set: {user_df.drop_duplicates().shape[0]}")
    user_df["Original"] = "Y" # Mark original records, this helps us later to identify the original records
    user_df.to_csv("Data_Set_1.csv", index=False)
    print(f"User data saved to {"Data_Set_1.csv"}")
    if show_output == "Y":
        print(tabulate(user_df, headers='keys', tablefmt='psql', showindex=False)) # grid
    else:
        print("Data not printed, only saved to CSV.")
    return user_df

# def print_user_data(records_to_process: int) -> None:
#     user_df = generate_user_data(records_to_process)
#     print(tabulate(user_df, headers='keys', tablefmt='psql', showindex=False)) # grid

# def csv_user_data(records_to_process: int, show_output: str, filename: str = "Data_Set_1.csv") -> pd.DataFrame:
#     user_df["Original"] = "Y" # Mark original records, this helps us later to identify the original records
#     user_df.to_csv(filename, index=False)
#     print(f"User data saved to {filename}")
#     # if show_output == "Y":
#     #     print(tabulate(user_df, headers='keys', tablefmt='psql', showindex=False)) # grid
#     # else:
#     #     print("Data not printed, only saved to CSV.")
#     return user_df

def mdm_split_data_set(records_to_process: int, show_output: str) -> tuple[pd.DataFrame, int]:
    user_df = generate_user_data(records_to_process)

    # user_df = csv_user_data(records_to_process, show_output)

    df_20 = user_df.sample(frac=0.2, random_state=42)  # Pick 20% randomly
    df_80 = user_df.drop(df_20.index)  # Remaining 80%  , droping the one used in df_20
    df_20.to_csv("Data_Set_2_20_Unique.csv", index=False)
    df20_num_records = df_20.shape[0]
    # print(f"Number of records in 20 set: {df20_num_records}")
    df_80.to_csv("Data_Set_2_80_Unique.csv", index=False)
    df80_num_records = df_80.shape[0]
    print(f"Number of records in 80 set: {df80_num_records}")
    return df_20, df20_num_records

# def change_df_20(user_df: pd.DataFrame) -> pd.DataFrame:
def change_df_20(records_to_process: int, show_output: str) -> pd.DataFrame:
    df_20,df20_num_records = mdm_split_data_set(records_to_process, show_output)
    print(f"Number of records in 20 set: {df20_num_records}")

    # Store original rows to avoid index issues when DataFrame grows
    original_rows = df_20.copy()

    name_map = {
    "Alexander": "Alex",
    "Alexandra": "Alex",
    "Andrew": "Andy",
    "Anthony": "Tony",
    "Allison": "Allie",
    "Amanda": "Mandy",
    "Ashley": "Ash",
    "Barbara": "Barb",
    "Benjamin": "Ben",
    "Becky": "Rebecca",
    "Brittany": "Britt",
    "Catherine": "Cathy",
    "Christina": "Chris",
    "Christopher": "Chris",
    "Cynthia": "Cyn",
    "Daniel": "Dan",
    "David": "Dave",
    "Derrick": "Derr",
    "Donald": "Don",
    "Edward": "Ed",
    "Elizabeth": "Liz",
    "Emily": "Em",
    "Gregory": "Greg",
    "Jacqueline": "Jackie",
    "James": "Jim",
    "Jennifer": "Jen",
    "Jessica": "Jess",
    "Jonathan": "Jon",
    "Joseph": "Joe",
    "Joshua": "Josh",
    "Justin": "Jus",
    "Karen": "Kare",
    "Katherine": "Kate",
    "Kenneth": "Ken",
    "Kimberly": "Kim",   
    "Kevin": "Kev",
    "Margaret": "Maggie",
    "Matthew": "Matt",
    "Michael": "Mike",
    "Nathan": "Nate",
    "Natalie": "Nat",
    "Nicholas": "Nick",
    "Olivia": "Liv",
    "Patricia": "Pat",
    "Rebecca": "Becky",
    "Richard": "Rich",
    "Robert": "Rob",
    "Ryan": "Ry",
    "Samantha": "Sam",
    "Sarah": "Sally",
    "Stephanie": "Steph",
    "Tiffany": "Tiff",
    "Theodore": "Theo",
    "Timothy": "Tim",
    "Victoria": "Vicky",
    "Whitney": "Whit",
    "William": "Will"
    }

    for index, row in original_rows.iterrows():
        iterations = random.randint(0, 2)  # Randomly select 0, 1, or 2 iterations
        for _ in range(iterations):
            new_row = row.copy()  # Copy the current row directly
            # want to update the middle_name field and original field to value blank
            new_row["Original"] = "N"  # Mark as modified
            # new_row["middle_name"] = ""   # Modify the name
            # new_row["middle_name"] = random.choice(["", new_row["middle_name"][0]])

            # Modify first name field based on dictionary
            # if new_row["first_name"] in name_map:
            #     new_row["first_name"] = random.choice([new_row["first_name"], name_map[new_row["first_name"]]])

            # if new_row["first_name"] in name_map:
            #     new_row["first_name"] = name_map[new_row["first_name"]]

            if new_row["first_name"] in name_map:
                new_row["first_name"] = random.choice([name_map[new_row["first_name"]], new_row["first_name"]])

            if new_row["middle_name"] in name_map:
                new_row["middle_name"] = random.choice([name_map[new_row["middle_name"]], new_row["middle_name"], new_row["middle_name"][0]])

            # new_row["first_name"] = random.choice([
            #     name_map.get(new_row["first_name"], new_row["first_name"]),  # Use original if not found
            #     new_row["middle_name"],
            #     new_row["middle_name"][0] if new_row["middle_name"] else ""
            # ])

            new_row["phone"] = random.choice([new_row["phone"], "", fake.phone_number()])
            new_row["email"] = random.choice([new_row["email"], "", fake.email()])
            # Address string modifications
            if "Apt." in new_row["address"]:
                new_row["address"] = random.choice([new_row["address"].replace("Apt.", "APT"), new_row["address"].replace("Apt.", "#"), new_row["address"].replace("Apt.", "Apartment")])
            if "Ave." in new_row["address"]:
                new_row["address"] = random.choice([new_row["address"].replace("Ave.", "Avenue"), new_row["address"].replace("Ave.", "AV")])
            if "Street" in new_row["address"]:
                new_row["address"] = random.choice([new_row["address"].replace("Street", "St."), new_row["address"].replace("Street", "ST")])
            if "Suite" in new_row["address"]:
                new_row["address"] = random.choice([new_row["address"].replace("Suite", "STE"), new_row["address"].replace("Suite", "Suit")])
            if "Drives" in new_row["address"]:
                new_row["address"] = random.choice([new_row["address"].replace("Drives", "Dr."), new_row["address"].replace("Drives", "Drive")])    

            df_20 = pd.concat([df_20, pd.DataFrame([new_row])], ignore_index=True)

    # Save the modified DataFrame
    df_20.to_csv("Data_Set_2_20_modified.csv", index=False)
    print(f"Modified 20% dataset saved with {df_20.shape[0]} total records")
    
    if show_output == "Y":
        print(tabulate(df_20, headers='keys', tablefmt='psql', showindex=False)) # grid
    else:
        print("Data not printed, only saved to CSV.")
    
    return df_20



# def u_middle_name(a, b):
#     operation = random.choice(["+", "-", "*"])
#     if operation == "+":
#         return a + b
#     elif operation == "-":
#         return a - b
#     else:  # Multiplication
#         return a * b

# def u_middlename(user_df, middle_name_value, original_value):

#     user_df["middle_name"] = middle_name_value
#     user_df["Original"] = original_value
#     return user_df



if __name__ == "__main__":

    num_of_records = int(input("Enter the number of records to generate: "))
    show_output = "Y"
    # print_user_data(num_of_records)
    change_df_20(num_of_records, show_output)


# def generate_address_variations(base_address):
#     variations = [
#         base_address,
#         base_address.replace("Street", "St."),
#         base_address.replace("Avenue", "Ave."),
#         base_address.replace("Road", "Rd."),
#         base_address.replace("Boulevard", "Blvd."),
#         base_address.lower().title(),  # Capitalize properly

# does fake has street address2?
