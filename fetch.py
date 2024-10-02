import imaplib
import ssl

email_user = "omarrabeh21014@outlook.com" #outlook_C324630165E32A6F@outlook.com
email_pass = "stitsytasmownqoi"  # App Password

IMAP_SERVER = 'imap-mail.outlook.com'#"outlook.office365.com"# imap-mail.outlook.com
IMAP_PORT = 993

context = ssl.create_default_context()

with imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT, ssl_context=context) as mail:
    try:
        # Try logging in
        mail.login(email_user, email_pass)
        print("Login successful!")
    except imaplib.IMAP4.error as e:
        print(f"LOGIN failed: {str(e)}")
    except Exception as general_error:
        print(f"An error occurred: {str(general_error)}")
