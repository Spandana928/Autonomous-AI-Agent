 Autonomous AI Agent
A Python-based Autonomous AI Agent that automates tasks like scraping AI news headlines, summarizing smartphone reviews, and analyzing renewable energy trends with PDF generation.

🎥 Video Walkthrough
Watch the full demo here:
🔗 Project Demo

🚀 Features
✅ AI News Scraper: Fetches the top 5 latest AI headlines from Google News.

✅ Smartphone Review Analyzer: Scrapes smartphone reviews and summarizes pros and cons.

✅ Renewable Energy Report Generator: Analyzes trends and creates a downloadable PDF with charts.

✅ Command Line Interaction: Run tasks with simple natural language instructions.

✅ PDF Generation with Chart Embedding.

🛠 Technologies Used
Python 3.12

Selenium for web automation

Matplotlib for data visualization

pdfkit + wkhtmltopdf for PDF generation

ChromeDriver for headless browsing

🧩 Available Instructions
You can interact with the system using these instructions:

diff
Copy
Edit
- find top ai headlines
- search smartphone reviews
- analyze renewable energy
- exit
📌 Detailed Approach
1. AI News Scraper
Opens Google News and searches for "artificial intelligence".

Scrapes the top 5 article headlines using XPath targeting.

Saves and displays the results in a text file (ai_headlines.txt) with numbering for clarity.

2. Smartphone Review Summarizer
Accesses GSMArena and fetches recent review headlines.

Extracts relevant points and splits them into Pros and Cons.

Writes a structured summary into smartphone_reviews.txt.

3. Renewable Energy Analyzer
Uses sample data representing 2025 growth trends in Solar, Wind, Hydro, and Geothermal.

Generates a bar chart using matplotlib.

Embeds the chart into an HTML file and converts it to PDF with pdfkit.

Outputs the file as renewable_energy_report.pdf.

🖥 How to Run Locally
Clone the Repository

bash
git clone <your-repo-link>
cd Autonomous-AI-Agent
Install Dependencies

bash
pip install selenium matplotlib pdfkit
Set up wkhtmltopdf

Download from https://wkhtmltopdf.org/downloads.html

Ensure the path in the script matches your installed location.

Run the Project

bash
python AI.py
🏁 Example Run
yaml
Enter instruction: find top ai headlines
Enter instruction: search smartphone reviews
Enter instruction: analyze renewable energy
Enter instruction: exit
