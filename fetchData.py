import imaplib
import email
from bs4 import BeautifulSoup

# Server and Port
IMAP_SERVER = "outlook.office365.com"
#IMAP_PORT = 993

email_address = 'omarrabehxiv@gmail.com'
password = 'stitsytasmownqoi'


mail = imaplib.IMAP4_SSL('outlook.office365.com')
mail.login(user=email_address, password=password)
#mail.login(email_address,password)


mail.select("Sent")  # inbox

# result, data = mail.search(None,"All")
result, data = mail.search(None, '(TO "omarrabehxiv@gmail.com" SUBJECT "Edit-Weight")')
email_ids = data[0].split()


def getEmailBody(msg):
    body = None

    if msg.is_multipart():
        for part in msg.walk():
            content_type = part.get_content_type()
            content_disposition = str(part.get("Content-Disposition"))

            if content_type == "text/plain":
                body = part.get_payload(decode=True).decode()
                break

            elif content_type == "text/html":
                html_content = part.get_payload(decode=True).decode()
                soup = BeautifulSoup(html_content, "html.parser")
                body = soup.get_text()
    else:
        soup = BeautifulSoup(msg.get_payload(decode=True).decode(), "html.parser")
        body = soup.get_text()

    return body


for email_id in email_ids:
    # Fetch the email by ID
    result, email_data = mail.fetch(email_id, "(RFC822)")
    raw_email = email_data[0][1]
    msg = email.message_from_bytes(raw_email)

    subject = msg["Subject"]
    body = getEmailBody(msg)
    sender = msg["From"]
    recipient = msg["To"]
    cc = msg["CC"] if msg["CC"] else "No CC"

    # Print the email details
    print(f"Email ID: {email_id.decode()}, Subject: {subject}")
    print(f"From: {sender}")
    print(f"To: {recipient}")
    print(f"CC: {cc}")
    print(f"Body:\n{body.strip()}")
    # print(f"Body:\n{msg.get_payload(decode=True).decode()}")
    print("-" * 50)

mail.logout()