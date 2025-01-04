import requests
from bs4 import BeautifulSoup

url = "https://courses.analyticsvidhya.com/courses/"

response = requests.get(url)
response.raise_for_status()  

soup = BeautifulSoup(response.text, 'html.parser')

course_links = []
for link in soup.find_all('a', href=True):
    href = link['href']
    if href.startswith('/courses/'):  
        full_link = f"https://courses.analyticsvidhya.com{href}"
        if full_link not in course_links:
            course_links.append(full_link)

with open("data/av-free-course-data.txt", "w") as file:
    for link in course_links:
        file.write(f"{link}\n")

print(f"Scraped {len(course_links)} course links successfully!")
