from bs4 import BeautifulSoup
import requests

url = 'https://www.ai-expo.net/europe/'


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
    print(soup.title.text)

    target_div = soup.find("div", class_='elementor-element-43cc35b6')

    if target_div:
        description = target_div.get_text(strip=True)
        print("Event Description:")
        print(description)
    else:
        print("Target div not found.")
