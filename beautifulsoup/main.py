import requests
from bs4 import BeautifulSoup

def main():
  page = requests.get("https://stice05icedevsev001.z16.web.core.windows.net/")
  if page.status_code == 200:
    soup = BeautifulSoup(page.content, 'html.parser')
    for script_or_style in soup(["script", "style"]):
      script_or_style.extract()
    text = soup.get_text()
    print(text)
if __name__ == "__main__":
  main()