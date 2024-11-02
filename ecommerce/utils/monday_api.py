import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

MONDAY_API_KEY = os.getenv("MONDAY_API_KEY")
MONDAY_API_URL = "https://api.monday.com/v2"
BOARD_ID = os.getenv("MONDAY_BOARD_ID")  #  Board ID

def add_user_to_board(username, email, registration_date):
    headers = {
        "Authorization": MONDAY_API_KEY,
        "Content-Type": "application/json",
    }

    query = '''
    mutation ($boardId: ID!, $itemName: String!, $columnValues: JSON!) {
        create_item (board_id: $boardId, item_name: $itemName, column_values: $columnValues) {
            id
        }
    }
    '''
    
    # Use the correct structure for each column type
    variables = {
        "boardId": BOARD_ID,
        "itemName": f"Registration - {username}",  # Set the item name in the "Task" column
        "columnValues": json.dumps({
            "text6": username,                        # Text column with raw text
            "email": {"email": email, "text": username},  # Email column with both email and display text
            "date8": {"date": registration_date}      # Date column with date format
        })
    }

    response = requests.post(
        MONDAY_API_URL,
        json={"query": query, "variables": variables},
        headers=headers
    )

    if response.status_code == 200:
        print("User added to board successfully:", response.json())
        return response.json()
    else:
        print("Failed to add user to board:", response.status_code, response.text)
        return None
