""" This script generates a synthetic dataset of user records, splits it into two parts"""
import random
from faker import Faker
from tabulate import tabulate
import pandas as pd

fake = Faker()
def generate_user_data(num_of_records: int) -> pd.DataFrame:
    """Generate a DataFrame with synthetic user data."""

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
    # Mark original records, this helps us later to identify the original records
    user_df["Original"] = "Y"

    return user_df

def mdm_split_data_set(user_df) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Split the user DataFrame into two parts: 20% and 80%."""
    df_20 = user_df.sample(frac=0.2, random_state=42)  # Pick 20% randomly
    df_80 = user_df.drop(df_20.index)  # Remaining 80%  , droping the one used in df_20
    return df_20, df_80

def change_df_20(df_20p: pd.DataFrame) -> pd.DataFrame:
    """Modify the 20% DataFrame to add bad data."""
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
    "Frederick": "Fred",
    "Gabriel": "Gabe",
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
    "Kevin": "Kev",
    "Kimberly": "Kim",
    "Kristopher": "Chris",  
    "Margaret": "Maggie",
    "Matthew": "Matt",
    "Melissa": "Mel",
    "Michael": "Mike",
    "Nathan": "Nate",
    "Natalie": "Nat",
    "Nicholas": "Nick",
    "Olivia": "Liv",
    "Patricia": "Pat",
    "Philip": "Phil",
    "Rachel": "Rach",
    "Rebecca": "Becky",
    "Richard": "Rich",
    "Robert": "Rob",
    "Ryan": "Ry",
    "Samantha": "Sam",
    "Sarah": "Sally",
    "Stephanie": "Steph",
    "Taylor": "Tay",
    "Thomas": "Tom",
    "Tiffany": "Tiff",
    "Theodore": "Theo",
    "Timothy": "Tim",
    "Victoria": "Vicky",
    "Whitney": "Whit",
    "William": "Will"
    }

    for index, row in original_rows.iterrows(): # pylint: disable=unused-variable

        iterations = random.randint(0, 3)  # Randomly select 0, 1, 2 or 3 iterations
        for _ in range(iterations):
            new_row = row.copy()  # Copy the current row directly
            new_row["Original"] = "N"  # Mark as modified

            if new_row["first_name"] in name_map:
                new_row["first_name"] = random.choice([name_map[new_row["first_name"]],
                                                       new_row["first_name"]])

            if new_row["middle_name"] in name_map:
                new_row["middle_name"] = random.choice([name_map[new_row["middle_name"]],
                                                        new_row["middle_name"], new_row["middle_name"][0]]) # pylint: disable=line-too-long

            new_row["phone"] = random.choice([new_row["phone"], "",
                                              fake.phone_number()])
            new_row["email"] = random.choice([new_row["email"], "",
                                              fake.email()]) + " "
            new_row["city"] = random.choice([new_row["city"], ""])
            new_row["state"] = random.choice([new_row["state"], "",
                                              fake.state()])
            new_row["zip_code"] = random.choice([new_row["zip_code"], ""])


            # Address string modifications
            if "Apt." in new_row["address"]:
                new_row["address"] = random.choice([new_row["address"].replace("Apt.", "APT"),
                                                    new_row["address"].replace("Apt.", "#"),
                                                    new_row["address"].replace("Apt.", "Apartment")]) # pylint: disable=line-too-long

            if "Ave." in new_row["address"]:
                new_row["address"] = random.choice([new_row["address"].replace("Ave.", "Avenue"),
                                                    new_row["address"].replace("Ave.", "AV")])
            if "Street" in new_row["address"]:
                new_row["address"] = random.choice([new_row["address"].replace("Street", "St."),
                                                    new_row["address"].replace("Street", "ST")])
            if "Suite" in new_row["address"]:
                new_row["address"] = random.choice([new_row["address"].replace("Suite", "STE"),
                                                    new_row["address"].replace("Suite", "Suit")])
            if "Drives" in new_row["address"]:
                new_row["address"] = random.choice([new_row["address"].replace("Drives", "Dr."),
                                                    new_row["address"].replace("Drives", "Drive")])

            df_20p = pd.concat([df_20p, pd.DataFrame([new_row])], ignore_index=True)
            # print(df_20p.shape[0])

    return df_20p

def main(num_of_records: int, show_output: str) -> None:
    """Main function to generate and process user data."""
    ##################################################################################
    # Step 1 - Generate user data
    print("\n####################### STEP 1 - GENERATE FULL SET ######################\n")
    user_df = generate_user_data(num_of_records)
    user_df.to_csv("Data_Set_1_FULL.csv", index=False)
    user_df_num_records = user_df.shape[0]
    print(f"""Number of records Full Data Set: {user_df_num_records} &
          Unique records as {user_df.drop_duplicates().shape[0]},
          saved here {"Data_Set_1_FULL.csv"}""")

    if show_output == "Y":
        print(tabulate(user_df, headers='keys', tablefmt='psql', showindex=False)) # grid
    else:
        print("Data not printed, only saved to CSV.")
    ##############################################################################
    # Step 2 - Split dataset in two data set 20 & 80
    print("\n##################### STEP 2 - SPLIT 80:20 RATIO #######################\n")
    df_20, df_80 = mdm_split_data_set(user_df)
    df_20.to_csv("Data_Set_2_20_Unique.csv", index=False)
    df_80.to_csv("Data_Set_2_80_Unique.csv", index=False)
    df20_num_records = df_20.shape[0]
    df80_num_records = df_80.shape[0]
    print(f"Records ~80 set: {df80_num_records}, saved~ {"Data_Set_2_80_Unique.csv"}")
    print(f"Records ~20 set: {df20_num_records}, saved~ {"Data_Set_2_20_Unique.csv"}")

    ###################################################################################
    # Step 3 - Create Data Set 20 with bad data added (it will have more then 20% of data)
    print("\n################### STEP 3 - ADD ITERATED REC. IN 20 SET ###############\n")
    df_20p = change_df_20(df_20)
    df_20p.to_csv("Data_Set_2_20_modified.csv", index=False)
    df_20p_num_records = df_20p.shape[0]
    print(f"Records Modified 20 set: {df_20p_num_records}, saved~ {"Data_Set_2_20_modified.csv"}")

    if show_output == "Y":
        print(tabulate(df_20p, headers='keys', tablefmt='psql', showindex=False)) # grid
    else:
        print("Data not printed, only saved to CSV.")

    ############################################################################
    # Step 4 - Merge the two data sets {Data_Set_2_20_Unique.csv,
    # Data_Set_2_80_Unique.csv} to use as Load 1
    print("\n############### STEP 4 - CREATE LOAD 1 SET ############################\n")
    load_good_df = pd.concat([df_20, df_80], ignore_index=True)
    load_good_df.to_csv("Data_Set_3_LOAD1.csv", index=False)
    load_good_num_records = load_good_df.shape[0]
    print(f"(80+20, load 1), #ofrecords: {load_good_num_records}, saved~ {'Data_Set_3_LOAD1.csv'}")
    print("use them as preferred records\n")

    #####################################################################################
    # Step 5 - Data set of only Original = N records
    # in Data_Set_2_20_modified.csv to use as Load 2
    print("\n############## STEP 5 - CREATE LOAD 2 SET #############################\n")

    load_later_df = df_20p[df_20p["Original"] == "N"].copy()
    load_later_df.to_csv("Data_Set_3_LOAD2.csv", index=False)
    load_later_num_records = load_later_df.shape[0]
    print(f"(Modiefied load 2) #ofrecords: {load_later_num_records}, saved ~{"Data_Set_3_LOAD2.csv"}") # pylint: disable=line-too-long

    print("use them as questionable records\n")


if __name__ == "__main__":
    numofrecords = int(input("Enter the number of records to generate: "))
    showoutput = input("Do you want to print the output? (Y/N): ").strip().upper()
    main(numofrecords, showoutput)
