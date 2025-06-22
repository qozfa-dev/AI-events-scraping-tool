from bs4 import BeautifulSoup
import requests

url = 'https://devpost.com/hackathons'


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Referer": "https://www.google.com/",
    "Connection": "keep-alive",
}

response = requests.get(url, headers=headers)

print(response.status_code)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all hackathon blocks
    hackathons = soup.find_all("div", class_="hackathon-tile")

    for hackathon in hackathons:
        title = hackathon.find("h3").text.strip()
        link = "https://devpost.com" + \
            hackathon.find("a", class_="tile-anchor")["href"]
        dates = hackathon.find("div", class_="submission-period").text.strip()
        location_span = hackathon.find("i", class_="fas fa-globe")
        location = location_span.find_next(
            "span").text.strip() if location_span else "Unknown"

        print(f"Title: {title}")
        print(f"Dates: {dates}")
        print(f"Location: {location}")
        print(f"Link: {link}")
        print("-" * 50)

else:
    print("Scraping did not work.")
