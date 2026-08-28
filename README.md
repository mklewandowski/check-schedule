# Yoga Space Schedule Notifier

An automated Python script that scrapes the weekly class schedule for **The Yoga Space (Mount Horeb)** via Playwright and sends an email notification if a target instructor is teaching that week.

Automated via **GitHub Actions** to run every Monday morning.

## How It Works

1. **Headless Scraping:** Launches a headless Chromium browser using `playwright` to render dynamic client-side JavaScript content on Momence.
2. **Teacher Check:** Evaluates the DOM to see if `TARGET_TEACHER` is listed for the upcoming week.
3. **Email Notification:** Connects to Gmail's SMTP server (`smtp.gmail.com:465`) and sends an alert email if a match is found.

## Prerequisites & Setup

### 1. Local Setup
Ensure you have Python 3.11+ installed.

```bash
# Clone repository
git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
cd your-repo-name

# Install dependencies
pip install playwright requests python-dotenv
playwright install chromium

# Set up local environment variable
echo "SENDER_PASSWORD=your_16_char_app_password" > .env
or set password in local .env file

# Run locally
python check_schedule.py
