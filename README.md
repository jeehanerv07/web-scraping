# Web Scraping - Pertemuan 9

## Deskripsi
Project ini dibuat untuk memenuhi tugas Pertemuan 9 pada mata kuliah Social Media Analysis, dengan materi teknik web scraping menggunakan Python, Requests, dan BeautifulSoup4.

## Tujuan
Memahami proses pengambilan data dari website, parsing HTML, ekstraksi informasi, dan penyimpanan hasil ke dalam format CSV.

## Tools dan Library
- Python
- Requests
- BeautifulSoup4
- CSV
- Visual Studio Code

## Website Sumber
https://www.pythonscraping.com/pages/page1.html

## Cara Menjalankan
1. Buat dan aktifkan virtual environment.
2. Install library menggunakan `pip install -r requirements.txt`.
3. Jalankan `python scraping.py`.
4. Periksa file `hasil_scraping.csv` untuk melihat hasil ekstraksi.

## Struktur Project
- `scraping.py`: program scraping.
- `requirements.txt`: daftar library.
- `README.md`: dokumentasi project.
- `hasil_scraping.csv`: hasil scraping setelah program dijalankan.

## Kesimpulan
Requests digunakan untuk mengambil HTML dari website, sedangkan BeautifulSoup4 digunakan untuk membaca struktur HTML dan mengekstrak informasi yang diperlukan. Data hasil scraping kemudian disimpan ke dalam file CSV.