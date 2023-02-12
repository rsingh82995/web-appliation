import requests
from bs4 import BeautifulSoup
import csv

search_parameters = {
    "primary_category": "Medical Journal",
    "secondary_category": "Orthopedic",
    "geography": "India",
    "date_range": "2022",
}

search_url = (
    f"https://www.google.com/search?q="
    f"{search_parameters['primary_category']} "
    f"{search_parameters['secondary_category']} "
    f"{search_parameters['geography']} "
    f"{search_parameters['date_range']}"
)

response = requests.get(search_url)
soup = BeautifulSoup(response.text, "html.parser")

url_list = []
for h3 in soup.find_all("h3"):
    a = h3.find("a")
    if a:
        url = a.get("href")
        url_list.append(url)

with open("output.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(url_list)