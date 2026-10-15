
import requests
from bs4 import BeautifulSoup

# URL website latihan scraping
url = "https://books.toscrape.com/"

# Mengambil halaman website
response = requests.get(url, timeout=15)

# Memeriksa apakah halaman berhasil diakses
response.raise_for_status()

# Membaca struktur HTML
soup = BeautifulSoup(response.text, "html.parser")

# Mengambil data buku
books = soup.find_all("article", class_="product_pod")

print("HASIL WEB SCRAPING DATA BUKU")
print("=" * 40)

for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").get_text(strip=True)

    print("Judul Buku:", title)
    print("Harga:", price)
    print("-" * 40)

print("Scraping selesai!")

