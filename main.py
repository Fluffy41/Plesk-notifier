import os
import requests
import dotenv

# Load environment variables from .env file
dotenv.load_dotenv()

# Plesk API URL and API key
plesk_api_url = os.getenv('PLESK_API_URL')
plesk_api_key = os.getenv('PLESK_API_KEY')

# Check if environment variables are set
print(f"Plesk API URL: {plesk_api_url}")
print(f"Plesk API KEY: {plesk_api_key}")

headers = {
    'KEY': plesk_api_key,
    'Content-Type': 'text/xml',
    'Accept': 'text/xml',
    'HTTP_PRETTY_PRINT': 'TRUE'
}

# XML request to retrieve mail logs
xml_request = """
<packet>
    <mail>
        <log>
            <filter>
                <limit>10</limit>
            </filter>
        </log>
    </mail>
</packet>
"""

response = requests.post(f"{plesk_api_url}/enterprise/control/agent.php", headers=headers, data=xml_request, verify=False)

# Output response
print(f"Status Code: {response.status_code}")
try:
    print(response.text)
except Exception as e:
    print(f"Error: {e}")