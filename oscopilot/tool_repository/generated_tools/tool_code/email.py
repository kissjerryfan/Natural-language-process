
def email():
    """
        This function demonstrates how to authenticate with Gmail API, fetch unread emails, and send an email using Gmail API.

        Args:
          None

        Returns:
          None
    """
    from google.oauth2.credentials import Credentials
    from googleapiclient.discovery import build

    # Authenticate and Build Gmail Service
    def authenticate_gmail():
        creds = Credentials.from_authorized_user_file('credentials.json',
                                                      ['https://www.googleapis.com/auth/gmail.readonly',
                                                       'https://www.googleapis.com/auth/gmail.send'])
        service = build('gmail', 'v1', credentials=creds)
        return service

    # Fetch Emails
    def fetch_emails(service, query="is:unread"):
        results = service.users().messages().list(userId='me', q=query).execute()
        messages = results.get('messages', [])
        email_list = []
        for message in messages:
            msg = service.users().messages().get(userId='me', id=message['id']).execute()
            snippet = msg['snippet']
            email_list.append({
                'id': message['id'],
                'snippet': snippet,
            })
        return email_list

    # Compose and Send Email
    def send_email(service, to, subject, body):
        from email.mime.text import MIMEText
        import base64

        message = MIMEText(body)
        message['to'] = to
        message['subject'] = subject
        raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
        service.users().messages().send(userId='me', body={'raw': raw_message}).execute()

    service = authenticate_gmail()
    print("Fetching unread emails...")
    emails = fetch_emails(service)
    for email in emails:
        print(f"Email Snippet: {email['snippet']}")

    print("Composing a new email...")
    send_email(service, "recipient@example.com", "Test Subject", "This is a test email.")
