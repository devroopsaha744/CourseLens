import requests
from bs4 import BeautifulSoup
import csv
import time
from urllib.parse import urlparse

def extract_text_from_url(url):
    try:
        # Add headers to mimic browser request
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(url.strip(), headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Remove script and style elements
        for script in soup(['script', 'style']):
            script.decompose()
            
        # Get text content
        text = soup.get_text(separator=' ', strip=True)
        return text
    except Exception as e:
        return f"Error: {str(e)}"

def process_links(input_file, output_file):
    with open(input_file, 'r') as f:
        urls = f.readlines()
    
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['URL', 'Content'])
        
        for url in urls:
            url = url.strip()
            if url:
                print(f"Processing: {url}")
                domain = urlparse(url).netloc
                content = extract_text_from_url(url)
                writer.writerow([url, domain, content])
                time.sleep(1)  # Polite delay between requests

# Usage
input_file = 'data/av-free-course-data.txt'  # Your input file with URLs
output_file = 'data/extracted_content.csv'
process_links(input_file, output_file)