# Web CSV Summarizer
A web based CSV summarizer built with Python and Streamlit. Upload any CSV file and get instant statistical summaries of numeric columns.

## What It Does
Upload any CSV file and get an instant overview: column names, row count, and statistical summaries (sum, average, min, max) for every numeric column. Built with Streamlit so it runs in the browser.

## Why I Built It
My CLI CSV summarizer worked, but it required editing the file path in code and running from the terminal. I wanted to turn it into a tool anyone could use—drag, drop, and get results.

## How to Run It
1. Clone this repo
2. Install the dependency: `pip install -r requirements.txt`
3. Run: `python -m streamlit run web_csv_summarizer.py`
4. Open the local URL, upload a CSV, and view your stats

## Tech Used
- Python 3
- Streamlit (web interface)
- csv module (data parsing)

## What I Learned
- **Streamlit file uploader:** Handling user-uploaded files via a browser interface.
- **io.StringIO:** Converting uploaded bytes into something csv.reader can parse.
- **Streamlit layout:** Using columns and metrics to present data cleanly.
- **Bridging CLI to web:** Taking logic I already understood and wrapping it in a user-friendly interface.
