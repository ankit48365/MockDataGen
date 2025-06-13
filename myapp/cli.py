from .base import generate_user_data, print_user_data
import argparse

# Hardcoded version information
VERSION = "0.0.3"

# Hardcoded usage information
EXAMPLE = """
TBD
"""

def main():
    print(">>> ✅ MockDataGen CLI loaded")
    parser = argparse.ArgumentParser(description='MockDataGen CLI Tool')
    parser.add_argument('--version', action='version', version=f'MockDataGen {VERSION}')
    parser.add_argument('--example', action='store_true', help='Show sample code syntax')
    parser.add_argument('--number', type=int, help='input number of records to generate', default=5)
   
    args = parser.parse_args()

    if args.example:
        print("Usage Information:\n")
        print(EXAMPLE)

    if args.number:
        print_user_data(args.number)

if __name__ == '__main__':
    main()
