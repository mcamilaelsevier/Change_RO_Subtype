import requests
import pandas as pd

# Define the API endpoint base and headers
api_endpoint_base = "https://YOUR-URL.elsevierpure.com/ws/api/research-outputs/"
headers = {
    "api-key": "Your-API-Key",  # Replace with your actual API key
    "Content-Type": "application/json"
}

# Define the JSON payload to update the research output type
update_payload = {
    "type": {
        "uri": "/dk/atira/pure/researchoutput/researchoutputtypes/contributiontojournal/abstract",
        "term": {
            "en_US": "Meeting abstract"
        }
    }
}

# Function to read Research Output UUIDs from an Excel file
def read_uuids_from_excel(file_path):
    df = pd.read_excel(file_path)
    return df['UUID'].tolist()

# Function to update the sub-type of a Research Output
def update_research_output_subtype(uuid):
    endpoint = f"{api_endpoint_base}{uuid}"
    response = requests.put(endpoint, headers=headers, json=update_payload)
    if response.status_code == 200:
        print(f"Successfully updated Research Output {uuid}")
        return response.json()
    else:
        print(f"Failed to update Research Output {uuid}: {response.status_code}")
        print(response.text)
        return None

# Main function to process and update Research Outputs
def main():
    excel_file_path = "research_output_uuids.xlsx"  # Replace with the path to your Excel file
    uuids = read_uuids_from_excel(excel_file_path)

    for uuid in uuids:
        update_research_output_subtype(uuid)

if __name__ == "__main__":
    main()
