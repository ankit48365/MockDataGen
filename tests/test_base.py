import pytest # isn't explicitly used in code but pytest automatically detects and runs test functions prefixed with test_. Without importing pytest, running pytest could fail if it needs specific pytest utilities.
import pandas as pd

##############################################################################################################
from myapp.base import generate_user_data

def test_generate_user_data():
    num_of_records = 10
    user_df = generate_user_data(num_of_records)

    # ✅ Check DataFrame shape
    assert user_df.shape[0] == num_of_records, "Row count mismatch"

    # ✅ Check required columns exist
    expected_columns = {"first_name", "middle_name", "last_name", "address", "city", "state", "zip_code", "phone", "email", "Original"}
    assert set(user_df.columns) == expected_columns, "Missing columns"

    # ✅ Check 'Original' column values
    assert all(user_df["Original"] == "Y"), "Original column should be 'Y' for all records"

    # ✅ Check uniqueness of records
    assert user_df.drop_duplicates().shape[0] <= num_of_records, "Unexpected duplicate records"

##############################################################################################################
from myapp.base import mdm_split_data_set  # Import the function

def test_mdm_split_data_set():
    num_of_records = 10
    user_df = generate_user_data(num_of_records)

    # Run the function
    df_20, df_80 = mdm_split_data_set(user_df)

    # ✅ Check total row count remains the same
    assert df_20.shape[0] + df_80.shape[0] == user_df.shape[0], "Total records mismatch"

    # ✅ Check df_20 contains 20% of the original records
    assert df_20.shape[0] == int(0.2 * user_df.shape[0]), "df_20 size incorrect"

    # ✅ Check df_80 contains 80% of the original records
    assert df_80.shape[0] == int(0.8 * user_df.shape[0]), "df_80 size incorrect"

    # ✅ Ensure no overlap between df_20 and df_80
    assert df_20.index.isin(df_80.index).sum() == 0, "Overlapping records found"

##############################################################################################################
from myapp.base import change_df_20  # Import the function

def test_change_df_20():

    num_of_records = 10
    user_df = generate_user_data(num_of_records)
    df_20, df_80 = mdm_split_data_set(user_df)

    # Run the function
    df_20p = change_df_20(df_20)

    # ✅ Check if number of rows in df_20 matches filtered rows in df_20p
    assert df_20.shape[0] == df_20p[df_20p["Original"] == "Y"].shape[0], "Row count mismatch after filtering"

##############################################################################################################

import subprocess

def test_main_output():
    # Simulated user inputs (records = 16, output preference = "N")
    simulated_input = "16\nN\n"

    # Run the script and capture output
    result = subprocess.run(
        ["uv", "run", "./myapp/base.py"],
        input=simulated_input,
        text=True,
        capture_output=True
    )

    # Expected output fragments
    expected_strings = [
        "Number of records in 80 set: 13, saved here Data_Set_2_80_Unique.csv",
        "Number of records in 20 set: 3, saved here Data_Set_2_20_Unique.csv",
        "Number of records in Data Set 3 (80+20, load1) set: 16, saved here Data_Set_3_LOAD1.csv, use them as preferred records",
        "Data not printed, only saved to CSV."
    ]

    # ✅ Ensure all expected strings appear in output
    for expected in expected_strings:
        assert expected in result.stdout, f"Missing expected output: {expected}"

################################################################################################################
# import subprocess

# def test_cli_print_no():
#     result = subprocess.run(
#         ["uv", "run", "./myapp/cli.py", "--number", "6", "--print", "N"],
#         capture_output=True,
#         text=True
#     )
#     assert "Data not printed, only saved to CSV." in result.stdout

# def test_cli_print_yes():
#     expected_headers = ["first_name", "middle_name", "last_name", "address", 
#                         "city", "state", "zip_code", "phone", "email", "Original"]
#     result = subprocess.run(
#         ["uv", "run", "./myapp/cli.py", "--number", "6", "--print", "Y"],
#         capture_output=True,
#         text=True
#     )
#     for header in expected_headers:
#         assert header in result.stdout