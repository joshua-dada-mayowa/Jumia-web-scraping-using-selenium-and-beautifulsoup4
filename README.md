# Jumia Web Scraping using Selenium and BeautifulSoup4

This Python project utilizes Selenium and BeautifulSoup4 to scrape data from the Jumia website. The script is designed to fetch information about flash sales for various categories on Jumia and store the data in a CSV file.

## Project Repository
[https://github.com/joshua-dada-mayowa/Jumia-web-scraping-using-selenium-and-beautifulsoup4/](https://github.com/joshua-dada-mayowa/Jumia-web-scraping-using-selenium-and-beautifulsoup4/)

## Files
- **main.py**: Python script for web scraping
- **dataset3.csv**: CSV file to store the scraped data

## Dependencies
- BeautifulSoup4
- Selenium

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/joshua-dada-mayowa/Jumia-web-scraping-using-selenium-and-beautifulsoup4.git
   ```
2. Install the required dependencies:
   ```bash
   pip install beautifulsoup4 selenium
   ```
3. Download the ChromeDriver executable and update the `PATH` variable in `main.py`:
   ```python
   PATH = "C:\Path\To\Your\chromedriver.exe"
   ```

## Usage
1. Run the `main.py` script:
   ```bash
   python main.py
   ```
2. The script will scrape data from the Jumia website for different categories, and the results will be stored in the `dataset3.csv` file.

## Additional Notes
- The script includes functionality to prevent duplicate entries by checking if the item title already exists in the CSV file.
- The script runs continuously, scraping data every 60 seconds. You can adjust the `time_wait` variable to change the interval.

Feel free to explore and modify the script according to your requirements. If you encounter any issues or have suggestions, please open an issue on the [GitHub repository](https://github.com/joshua-dada-mayowa/Jumia-web-scraping-using-selenium-and-beautifulsoup4/issues).
