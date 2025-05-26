# bs4-requests
fetch_sites.py :	Contains logic to send HTTP requests and retrieve HTML content from target websites. This is the entry point for downloading raw HTML pages.
parse_html.py : Responsible for parsing HTML using BeautifulSoup and extracting meaningful data from web pages. Works in tandem with fetch_sites.py.
practice_soup.py: A script used for learning and testing BeautifulSoup methods and HTML traversal on dummy/static HTML content. Great for beginners practicing tag navigation, searching, etc.
pagination.py: Demonstrates how to handle pagination in web scraping. It loops through multiple pages of a website and extracts data consistently across pages.
quotes.csv : Stores scraped data (e.g., quotes, authors, tags) in CSV format for easy access, analysis, or sharing. Generated from pagination.py

🚀 How to Run
Clone this repo:
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

=============================================================================================================================================================================================

Install Dependencies:
These scripts use requests and beautifulsoup4. Install them with pip:
pip install -r requirements.txt

=============================================================================================================================================================================================

Run Individual Scripts:

Run scraping:
python fetch_sites.py

=============================================================================================================================================================================================

Parse HTML:

python parse_html.py

=============================================================================================================================================================================================

Practice BS4 functions:

python practice_soup.py

=============================================================================================================================================================================================

Handle pagination and export CSV:

python pagination.py
