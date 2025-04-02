import requests
import json
from langchain_core.tools import tool


@tool
def get_holding_report(service_provider_account_number:str):
    """Call the holding report function with the given serviceProviderAccountNumber"""
    url = "https://10.149.25.224:443/holdingsreporting_wealth/_search"

    # Dynamically set the serviceProviderAccountNumber in the query
    payload = json.dumps({
        "query": {
            "match": {
                "serviceProviderAccountNumber": service_provider_account_number
            }
        }
    })

    headers = {
        'Content-Type': 'application/json'
    }

    try:
        # Make the GET request
        response = requests.request("GET", url, headers=headers, data=payload)

        # Check for successful response
        if response.status_code == 200:
            return response.json()  # Returning the JSON data from the response
        else:
            return {"error": "Failed to fetch data", "status_code": response.status_code}

    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
