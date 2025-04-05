

import os
import subprocess
import time
import json
import pdfkit
import matplotlib.pyplot as plt
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize browser
def initialize_browser():
    """Initialize and return the Selenium WebDriver."""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run in headless mode
    return webdriver.Chrome(options=options)

# --- TASK 1: FIND AI HEADLINES ---
def search_ai_headlines():
    """Scrape and save top 5 AI news headlines from Google News."""
    driver = initialize_browser()
    driver.get("https://news.google.com/search?q=artificial+intelligence")

    try:
        # Wait for headlines to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//a[contains(@class, 'JtKRv')]"))
        )

        # Extract top 5 headlines
        headline_elements = driver.find_elements(By.XPATH, "//a[contains(@class, 'JtKRv')]")[:5]
        ai_news = [headline.text for headline in headline_elements if headline.text.strip()]

        driver.quit()

        if ai_news:
            # Number the headlines
            numbered_headlines = "\n".join([f"{i+1}. {headline}" for i, headline in enumerate(ai_news)])

            # Save to file
            write_to_file("ai_headlines.txt", numbered_headlines)
            return numbered_headlines
        else:
            return "No AI headlines found."

    except Exception as e:
        driver.quit()
        return f"Error: {str(e)}"


# --- TASK 2: SEARCH SMARTPHONE REVIEWS ---
def search_smartphone_reviews():
    """Scrape smartphone reviews, extract pros/cons, and summarize."""
    driver = initialize_browser()
    driver.get("https://www.gsmarena.com/")
    time.sleep(3)

    phones = driver.find_elements(By.CLASS_NAME, "news-item")[:5]
    reviews = [phone.text for phone in phones if phone.text]

    driver.quit()

    if reviews:
        pros = [review.split(" - ")[0] for review in reviews]
        cons = [review.split(" - ")[-1] for review in reviews]

        summary = f"📱 Smartphone Reviews Summary 📱\n\nPros:\n" + "\n".join(pros) + "\n\nCons:\n" + "\n".join(cons)
        write_to_file("smartphone_reviews.txt", summary)
        return summary
    else:
        return "No smartphone reviews found."

# --- TASK 3: RESEARCH RENEWABLE ENERGY, ANALYZE TRENDS, & CREATE PDF --


# Configure wkhtmltopdf

    
# Configure wkhtmltopdf


# Configure wkhtmltopdf
config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")

def analyze_renewable_energy():
    """Research renewable energy trends, analyze data, and create a PDF report with charts."""

    # Sample data for trends
    trends = {
        "Solar": 40,
        "Wind": 30,
        "Hydro": 20,
        "Geothermal": 10
    }

    # Create and save the bar chart
    plt.bar(trends.keys(), trends.values(), color=['yellow', 'blue', 'green', 'red'])
    plt.xlabel("Energy Sources")
    plt.ylabel("Growth Percentage")
    plt.title("Renewable Energy Trends (2025)")
    
    image_filename = "energy_trends.png"
    plt.savefig(image_filename)  # Save chart as image
    plt.close()

    # Convert image path to absolute path
    image_path = os.path.abspath(image_filename)

    # Generate HTML content
    html_content = f"""
    <html>
    <head><meta charset="UTF-8"></head>
    <body>
        <h1>Renewable Energy Trends Report</h1>
        <p><strong>Analysis:</strong> Solar and Wind energy dominate the renewable sector, with Solar growing at 40%.</p>
        <img src="{image_path}" width="500px">
    </body>
    </html>
    """

    # PDF generation with --enable-local-file-access
    options = {
        'enable-local-file-access': None  # This allows local file access for images
    }

    # Save as PDF
    pdfkit.from_string(html_content, "renewable_energy_report.pdf", configuration=config, options=options)

    return "Renewable Energy Report created: renewable_energy_report.pdf"


# --- HELPER FUNCTIONS ---
def write_to_file(filename, content):
    """Write content to a file."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(str(content))

# --- MAIN FUNCTION ---
def main():
    print("Autonomous AI Agent Started...\n")
    tasks = {
        "find top ai headlines": search_ai_headlines,
        "search smartphone reviews": search_smartphone_reviews,
        "analyze renewable energy": analyze_renewable_energy
    }

    while True:
        command = input("Enter instruction: ").strip().lower()
        if command in ["exit", "quit"]:
            print("Exiting AI agent...")
            break
        elif command in tasks:
            result = tasks[command]()
            print("\nTask Result:\n", result)
        else:
            print("Invalid command. Try again.")

if __name__ == "__main__":
    main()

