import sys
import requests
import re

def download_url_and_get_all_hrefs(url):
    hrefs = []
    response = requests.get(url)
    
    if response.status_code == 200:
        # Najde všechny href="..." uvnitř tagů <a ...>
        hrefs = re.findall(r'<a[^>]+href=["\'](.*?)["\']', response.text)
        
    return hrefs

if __name__ == "__main__":
    try:
        url = sys.argv[1]
        odkazy = download_url_and_get_all_hrefs(url)
        print(odkazy)
    except IndexError:
        print("Chyba: Zadejte URL jako argument programu.")
    except Exception as e:
        print(f"Program skoncil chybou: {e}")