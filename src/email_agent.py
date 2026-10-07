from imaplib import IMAP4_SSL
server=IMAP4_SSL("imap.gmail.com")

try:
    from dotenv import load_dotenv
    import os
    import email
    import email.header
    load_dotenv()
    email_address = os.getenv("EMAIL_ADDRESS")
    password = os.getenv("EMAIL_PASSWORD")
    if not email_address or not password:
        raise ValueError("EMAIL_ADDRESS or EMAIL_PASSWORD not set in .env file")
    server.login(email_address, password)
    server.select("inbox")

    #searching
    status, data=server.search(None, "ALL")
    latest_id=data[0].split()[-1]

    #fetching
    status, msg_data = server.fetch(latest_id, "(RFC822)")

    #parsing
    raw_email = msg_data[0][1]
    msg_data=email.message_from_bytes(raw_email)
    header=msg_data['Subject']
    decoded=email.header.decode_header(header)
    for text, charset in decoded:
        if isinstance(text, bytes):
            text=text.decode(encoding=charset or 'utf-8')
    print(f"{decoded[0][0]}, {decoded[0][1]}")
    print(f"Connected to Gmail and fetched the latest email from {msg_data['From']} with subject: {msg_data['Subject']}")
except Exception as e:
    print(f"Failed to connect to Gmail and fetch latest email {e}")