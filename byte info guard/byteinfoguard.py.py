# ========================================================
# BYTE OSINT TOOL - Full Working Version
# ========================================================

import requests

# ===================== ASCII HEADER =====================
ascii_header = r"""
██████╗ ██╗   ██╗████████╗███████╗    ██╗███╗   ██╗███████╗ ██████╗      ██████╗ ██╗   ██╗ █████╗ ██████╗ ██████╗ 
██╔══██╗╚██╗ ██╔╝╚══██╔══╝██╔════╝    ██║████╗  ██║██╔════╝██╔═══██╗    ██╔════╝ ██║   ██║██╔══██╗██╔══██╗██╔══██╗
██████╔╝ ╚████╔╝    ██║   █████╗      ██║██╔██╗ ██║█████╗  ██║   ██║    ██║  ███╗██║   ██║███████║██████╔╝██║  ██║
██╔══██╗  ╚██╔╝     ██║   ██╔══╝      ██║██║╚██╗██║██╔══╝  ██║   ██║    ██║   ██║██║   ██║██╔══██║██╔══██╗██║  ██║
██████╔╝   ██║      ██║   ███████╗    ██║██║ ╚████║██║     ╚██████╔╝    ╚██████╔╝╚██████╔╝██║  ██║██║  ██║██████╔╝
╚═════╝    ╚═╝      ╚═╝   ╚══════╝    ╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝      ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ 
"""

print(ascii_header)

# ===================== CONFIGURATION =====================
API_URL = "https://users-xinfo-admin-six.vercel.app/api"
API_KEY = "qwertyuioplk847isuhnsiandj"

# ===================== FUNCTIONS =====================
def get_phone_info(phone_number):
    """
    Queries the BYTE OSINT TOOL API for information about the given phone number.
    """
    params = {
        "key": API_KEY,
        "type": "mobile",
        "term": phone_number
    }

    try:
        response = requests.get(API_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def print_record(record, index):
    """
    Prints a single record neatly.
    """
    print(f"\n--- Record #{index + 1} ---")
    print(f"Name       : {record.get('NAME') or 'N/A'}")
    print(f"First Name : {record.get('fname') or 'N/A'}")
    print(f"Mobile     : {record.get('MOBILE') or 'N/A'}")
    print(f"Address    : {record.get('ADDRESS') or 'N/A'}")
    print(f"Circle     : {record.get('circle') or 'N/A'}")
    print(f"Email      : {record.get('email') or 'N/A'}")
    print(f"Alt        : {record.get('alt') or 'N/A'}")
    print(f"ID         : {record.get('id') or 'N/A'}")

# ===================== MAIN PROGRAM =====================
def main():
    phone_number = input("Enter phone number (with country code, e.g., +1234567890): ").strip()

    result = get_phone_info(phone_number)

    if result and result.get("success"):
        data_list = result.get("result", {}).get("data", [])
        total_records = result.get("result", {}).get("total_records", 0)
        print(f"\nTotal Records Found: {total_records}")

        for idx, record in enumerate(data_list):
            print_record(record, idx)

        tag = result.get("result", {}).get("tag")
        if tag:
            print(f"\nTag: {tag}")
    else:
        print("No data found or an error occurred.")

if __name__ == "__main__":
    main()
