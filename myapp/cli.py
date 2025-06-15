from .base import main as gen_mdm_data  # local run change .base to base only and then run > uv run .\myapp\cli.py --number 10 --print N
import argparse
import sys
# Hardcoded version information
VERSION = "1.1.0"

# Hardcoded usage information
EXAMPLE = """
From CLI you can run the following command to generate mock data: Print Y/N for selecting user preference to print results on screen.
Example:
mockdatagen --number 10 --print N
"""

def main():
    print(">>> ✅ MockDataGen CLI loaded")
    parser = argparse.ArgumentParser(description='MockDataGen CLI Tool')
    parser.add_argument('--version', action='version', version=f'MockDataGen {VERSION}')
    parser.add_argument('--example', action='store_true', help='Show sample code syntax')
    parser.add_argument('--number', type=int, help='input number of records to generate', default=20)
    parser.add_argument('--print', type=str, help='Y/N for selecting user preferance to print results on screen', default='Y')
   
    args = parser.parse_args()

    if args.example:
        print("Usage Information:\n")
        print(EXAMPLE)

    if args.number:
        if not args.print:
            print("--print option is required for --number option")
            sys.exit(1) 
        gen_mdm_data(args.number, args.print) 
        sys.exit(0)

if __name__ == '__main__':
    main()
