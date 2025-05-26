import requests
import json

# Step 1: Define query parameters
params = {
    "name": "Mayank",
    "city": "Jaipur"
}

# Step 2: Add custom headers (Bonus)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/113.0.0.0 Safari/537.36",
    "Referer": "https://www.google.com"
}

# Step 3: Send GET request with params and headers
response = requests.get("https://httpbin.org/get", params=params, headers=headers)

# Step 4: Print the returned JSON response (nicely formatted)
data = response.json()

print("Formatted JSON Response:")
print(json.dumps(data, indent=4))  # pretty print
