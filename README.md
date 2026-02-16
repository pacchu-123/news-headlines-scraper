# News Headlines Web Scraper

##  Project Overview
This project is a simple Python web scraper that collects top news headlines 
from a public news website using web scraping techniques.

The headlines are saved automatically into a text file.

##  Technologies Used
- Python
- Requests library
- BeautifulSoup (bs4)
- VS Code
- GitHub

---

##  How It Works
1. Sends HTTP request to news website.
2. Extracts HTML content.
3. Parses headlines using BeautifulSoup.
4. Saves headlines into a text file (head_lines.txt).

---

##  Project Files
- `news_scraper.py` → Python scraper code  
- `head_lines.txt` → Output headlines file  
- `README.md` → Project documentation  

---

## How to Run
```bash
pip install requests beautifulsoup4
python news_scraper.py

##  Output Screenshot

![Output Screenshot](output.png)
