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
    # print(f"Number of records in main set: {user_df.shape[0]}")
    # print(f"Number of Unique Records in main set: {user_df.drop_duplicates().shape[0]}")
    user_df["Original"] = "Y" # Mark original records, this helps us later to identify the original records

    return user_df


# def mdm_split_data_set(records_to_process: int, show_output: str, user_df ) -> tuple[pd.DataFrame, pd.DataFrame]:
def mdm_split_data_set(user_df) -> tuple[pd.DataFrame, pd.DataFrame]:

    # user_df = generate_user_data(records_to_process)
    df_20 = user_df.sample(frac=0.2, random_state=42)  # Pick 20% randomly
    df_80 = user_df.drop(df_20.index)  # Remaining 80%  , droping the one used in df_20
    return df_20, df_80

def change_df_20(df_20p: pd.DataFrame) -> pd.DataFrame:
# def change_df_20(records_to_process: int, show_output: str) -> pd.DataFrame:
    # df_20,df20_num_records = mdm_split_data_set(records_to_process, show_output)
    # print(f"Number of records in 20 set: {df20_num_records}")

    # Store original rows to avoid index issues when DataFrame grows
    original_rows = df_20p.copy()

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

            if new_row["first_name"] in name_map:
                new_row["first_name"] = random.choice([name_map[new_row["first_name"]], new_row["first_name"]])

            if new_row["middle_name"] in name_map:
                new_row["middle_name"] = random.choice([name_map[new_row["middle_name"]], new_row["middle_name"], new_row["middle_name"][0]])


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

            df_20p = pd.concat([df_20p, pd.DataFrame([new_row])], ignore_index=True)

            return df_20p


def main():
    num_of_records = int(input("Enter the number of records to generate: "))
    show_output = input("Do you want to print the output? (Y/N): ").strip().upper()

    ##############################################################################################
    # Step 1 - Generate user data
    print("\n####################################### STEP 1 ######################################\n")
    user_df = generate_user_data(num_of_records)
    user_df.to_csv("Data_Set_1_100.csv", index=False)
    user_df_num_records = user_df.shape[0]
    print(f"Number of records Full Data Set: {user_df_num_records} & Unique records as {user_df.drop_duplicates().shape[0]}, saved here {"Data_Set_1_100.csv"}")

    if show_output == "Y":
        print(tabulate(user_df, headers='keys', tablefmt='psql', showindex=False)) # grid
    else:
        print("Data not printed, only saved to CSV.")
    
    ###############################################################################################
    # Step 2 - Split dataset in two data set 20 & 80
    print("\n####################################### STEP 2 #######################################\n")
    df_20, df_80 = mdm_split_data_set(user_df)
    df_20.to_csv("Data_Set_2_20_Unique.csv", index=False)
    df_80.to_csv("Data_Set_2_80_Unique.csv", index=False)
    df20_num_records = df_20.shape[0]
    df80_num_records = df_80.shape[0]
    print(f"Number of records in 80 set: {df80_num_records}, saved here {"Data_Set_2_80_Unique.csv"}")
    print(f"Number of records in 20 set: {df20_num_records}, saved here {"Data_Set_2_20_Unique.csv"}")

    ###############################################################################################
    # Step 3 - Create Data Set 20 with bad data added (it will have more then 20% of data)
    print("\n####################################### STEP 3 #######################################\n")
    df_20p = change_df_20(df_20)
    df_20p.to_csv("Data_Set_2_20_modified.csv", index=False)
    df_20p_num_records = df_20p.shape[0]
    print(f"Number of records in Modified 20 set: {df_20p_num_records}, saved here {"Data_Set_2_20_modified.csv"}")

    if show_output == "Y":
        print(tabulate(df_20p, headers='keys', tablefmt='psql', showindex=False)) # grid
    else:
        print("Data not printed, only saved to CSV.")

if __name__ == "__main__":
    main()

    # num_of_records = int(input("Enter the number of records to generate: "))
    # show_output = "N"
    # # print_user_data(num_of_records)
    # change_df_20(num_of_records, show_output)

