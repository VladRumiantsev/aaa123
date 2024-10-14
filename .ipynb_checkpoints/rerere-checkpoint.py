import requests
import re
import os
url = "https://gsom.spbu.ru/en/"
response = requests.get(url)
if response.status_code == 200:
    content = str(response.text)
    png_count = content.lower().count('png')
    print(f"PNG links: {png_count}")
    first_png_match = re.search(r'https?://[^\s]+?\.png', content, re.IGNORECASE)
    if first_png_match:
        first_png_url = first_png_match.group(0)
        print(f"first PNG link: {first_png_url}")
        img_response = requests.get("https://gsom.spbu.ru/images/cms/sad/11.jpg")
        if img_response.status_code == 200:
            if not os.path.exists('images'):
                os.makedirs('images')
            img_path = os.path.join('images', 'downloaded_image.png')
            with open(img_path, 'wb') as img_file:
                img_file.write(img_response.content)
            print(f"saved as: {img_path}")