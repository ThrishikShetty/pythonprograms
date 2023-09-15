import requests
import os
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = 'https://xkcd.com'

if not os.path.exists('xkcd_comics'):
    os.makedirs('xkcd_comics')

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
comic_elem = soup.find_all('img')

for comic in comic_elem:
    comic_url = urljoin(url, comic['src'])
    img_response = requests.get(comic_url)
    image_filename = os.path.join('xkcd_comics', os.path.basename(comic_url))

    with open(image_filename, 'wb') as img_file:
        img_file.write(img_response.content)

    print("Downloaded: {}".format(image_filename))

print("All XKCD comics downloaded successfully!")