import os
import imaplib
import email
from email.header import decode_header
import time


def show_progress(current, total, bar_length=50):
    percent = current / total
    hashes = "#" * int(percent * bar_length)
    spaces = " " * (bar_length - len(hashes))
    print(f"\rProgress: [{hashes}{spaces}] {percent * 100:.2f}%", end="")


# Configuration
IMAP_SERVER = "*********"  # Replace with your server
EMAIL_ACCOUNT = "*******"  # Replace with your email address
PASSWORD = "********"  # Replace with your password
RETRY_INTERVAL = 5  # Seconds to wait before retrying login

# Create a folder to store the emails (if it doesn't exist)
path_to_store = "yor/path/to/store"
os.makedirs(path_to_store, exist_ok=True)


def ensure_logged_in(mail):
    """Ensure the mail connection is logged in."""
    while True:
        try:
            # Check connection
            mail.noop()
            return mail
        except imaplib.IMAP4.abort:
            print("\nSession expired. Reconnecting...")
            try:
                mail = imaplib.IMAP4_SSL(IMAP_SERVER)
                mail.login(EMAIL_ACCOUNT, PASSWORD)
                mail.select("inbox")
                print("Reconnected successfully.")
                return mail
            except Exception as e:
                print(f"Reconnection failed: {e}. Retrying in {RETRY_INTERVAL} seconds...")
                time.sleep(RETRY_INTERVAL)


# Connect to the IMAP server
mail = imaplib.IMAP4_SSL(IMAP_SERVER)
mail.login(EMAIL_ACCOUNT, PASSWORD)
mail.select("inbox")

# Search for all emails
status, messages = mail.search(None, "ALL")
email_ids = messages[0].split()
total_mails = len(email_ids)
print(f"Total mails: {total_mails}")

# Iterate over each email ID
count = 1
useless = []

try:
    for email_id in email_ids:
        # Ensure logged in before processing
        mail = ensure_logged_in(mail)

        try:
            # Fetch the email
            status, msg_data = mail.fetch(email_id, "(RFC822)")

            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    # Parse the email
                    msg = email.message_from_bytes(response_part[1])

                    # Decode the subject
                    subject = msg.get("Subject")
                    if subject:
                        subject, encoding = decode_header(subject)[0]
                        if isinstance(subject, bytes):
                            subject = subject.decode(encoding if encoding else "utf-8")
                    else:
                        subject = "No Subject"

                    # Get the sender
                    sender = msg.get("From")

                    # Extract the email body (plain text only, no attachments)
                    body = None
                    if msg.is_multipart():
                        for part in msg.walk():
                            if part.get_content_type() == "text/plain" and part.get("Content-Disposition") is None:
                                try:
                                    body = part.get_payload(decode=True).decode("utf-8")
                                except (UnicodeDecodeError, AttributeError):
                                    body = None
                                break
                    else:
                        if msg.get_content_type() == "text/plain":
                            try:
                                body = msg.get_payload(decode=True).decode("utf-8")
                            except (UnicodeDecodeError, AttributeError):
                                body = None

                    # Save the email content
                    if body:
                        filename = os.path.join(path_to_store, f"{count}.txt")
                        with open(filename, "w", encoding="utf-8") as f:
                            f.write(f"!#@$)(*sender: {sender}\n")
                            f.write(f"!#@$)(*subject: {subject}\n")
                            f.write(f"!#@$)(*message: {body}\n")
                    else:
                        useless.append(email_id)

        except Exception as e:
            print(f"\nError processing email ID {email_id}: {e}")
            useless.append(email_id)

        count += 1
        show_progress(count - 1, total_mails)

except KeyboardInterrupt:
    print("\nInterrupted by user.")

finally:
    mail.logout()

# Save the IDs of emails with issues
filename = os.path.join(path_to_store, "useless.txt")
with open(filename, "w", encoding="utf-8") as f:
    for i in useless:
        f.write(f"{i.decode()}\n")

print(f"\nTotal mails: {total_mails}")
print(f"Useless: {len(useless)}")
