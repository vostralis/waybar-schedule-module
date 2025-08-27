from bs4 import BeautifulSoup
from dotenv import load_dotenv
from typing import Dict, List

import json
import os
import requests


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5"
}

def fetch_schedule(url: str) -> Dict[str, List[str]]:
    schedule = dict()

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise requests.exceptions.ConnectionError(f"Failed to fetch data from {url}")
    
    soup = BeautifulSoup(response.text, "lxml")
    days = soup.find_all("div", class_="block-index")

    for day in days:
        date = day.find("h2").text.split()[0] # dd.mm.yy
        lessons = list()

        for lesson in day.find_all("div", class_='list-group-item'):
            lessons.append(format_lesson(clear_string(lesson.text)))

        schedule[date] = '\n'.join(lessons)

    return schedule

def clear_string(string: str) -> str:
    string = string.replace('\n', ' ').replace('\u2009', ' ').strip()
    while '  ' in string:
        string = string.replace('  ', ' ')
    
    return string

def format_lesson(lesson: str) -> str:
    lesson = lesson.replace("подгруппа ", "").replace("(ф.)", "")
    time, rest = lesson.split(' ', 1)
    return f"{time} {"\n\t".join(rest.split(' - ', 1))}"

def main() -> int:
    load_dotenv()

    url = os.getenv("URL")

    if url is None:
        raise RuntimeError("Schedule url is not specified in .env")
    else:
        schedule = fetch_schedule(url)
        with open("./schedule.json", "w", encoding="utf-8") as f:
            f.write(json.dumps(schedule, indent=4, ensure_ascii=False))

    return 0


if __name__ == "__main__":
    main()