import requests

def fetch_data(url):
    headers = {
        'Accept': 'application/vnd.sdmx.structure+json;version=1.0'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
        data = response.json()
        return data
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request exception occurred: {req_err}")
    except requests.exceptions.JSONDecodeError as json_err:
        print(f"JSON decoding error occurred: {json_err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage for the first API endpoint
url = 'https://api.statcan.gc.ca/census-recensement/profile/sdmx/rest/codelist/STC_CP/CL_GEO_CMACA/latest'
data = fetch_data(url)

if data is not None:
    print(data)
