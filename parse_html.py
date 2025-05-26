import requests
from bs4 import BeautifulSoup

url = "https://httpbin.org/html"
response = requests.get(url)

# Step 2: Parse the HTML using BeautifulSoup
soup = BeautifulSoup(response.text, "lxml")

# Step 3: Print the entire HTML (for reference)
print("HTML Content:\n", soup.prettify())

# Step 4: Extract <h1> tag
h1_tag = soup.find("h1")
print("\n<h1> Tag Text:", h1_tag.text)

# Step 5: Extract <p> tag
p_tag = soup.find("p")
print("\n<p> Tag Text:", p_tag.text)