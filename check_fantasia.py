import requests
from bs4 import BeautifulSoup
import smtplib
from email.message import EmailMessage

movie = "fantasia"

sites = {
"New Beverly": "https://thenewbev.com/schedule/",
"American Cinematheque": "https://www.americancinematheque.com/now-showing/",
"Frida Cinema": "https://thefridacinema.org/calendar/",
"Alamo Drafthouse LA": "https://drafthouse.com/los-angeles/showtimes"
}

found = []

for name, url in sites.items():
    try:
        r = requests.get(url, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")

        if movie in soup.text.lower():
            found.append(f"{name}: {url}")
    except:
        pass

if found:
    msg = EmailMessage()
    msg["Subject"] = "Fantasia Screening Found!"
    msg["From"] = "youremail@gmail.com"
    msg["To"] = "youremail@gmail.com"

    msg.set_content("\n".join(found))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login("buddycrime1@gmail.com", "faog cymj rrup xswj")
        smtp.send_message(msg)
