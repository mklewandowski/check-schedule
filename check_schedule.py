import os
import smtplib
from email.message import EmailMessage
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
load_dotenv()

TARGET_TEACHER = "Sarah Goldsmith"
SCHEDULE_URL = "https://momence.com/u/the-yoga-space-cm3KCs"

SENDER_EMAIL = "mattkainlewandowski@gmail.com"
RECIPIENT_EMAIL = "mattkainlewandowski@gmail.com"
SENDER_PASSWORD = os.environ.get("SENDER_PASSWORD")

def send_notification_email(teacher_name):
    msg = EmailMessage()
    msg["Subject"] = f"🧘 Yoga Alert: {teacher_name} is teaching this week!"
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECIPIENT_EMAIL
    
    body = (
        f"Hi Matt,\n\n"
        f"{teacher_name} is listed on the schedule at The Yoga Space for this week!\n\n"
        f"View schedule & book: https://www.yogaspacemounthoreb.com/schedule/\n"
    )
    msg.set_content(body)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)
    print("Notification email sent successfully.")

def check_schedule():
    with sync_playwright() as p:
        # Launch headless browser
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        print("Loading schedule page...")
        page.goto(SCHEDULE_URL, wait_until="networkidle")
        
        # Wait up to 10s for class cards/content to dynamically load
        page.wait_for_timeout(3000)
        
        # Extract full rendered page HTML content
        content = page.content()
        browser.close()

        if TARGET_TEACHER.lower() in content.lower():
            print(f"Found {TARGET_TEACHER} on the rendered schedule!")
            send_notification_email(TARGET_TEACHER)
        else:
            print(f"{TARGET_TEACHER} was NOT found on the schedule for this week.")

if __name__ == "__main__":
    check_schedule()