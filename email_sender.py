import logging
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP_SSL, SMTPException

logging.basicConfig(
    filename='email.log',
    filemode='w',
    format='%(process)d-%(levelname)s-%(message)s',
    datefmt='%d-%m-%y %H:%M:%S',
    level=logging.INFO
)


async def send_email(host, email_from, email_to, password, port, subject, message):
    start = time.time()
    try:
        msg = MIMEMultipart()
        msg['From'] = email_from
        msg['To'] = email_to
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))
        server = SMTP_SSL(host, port)
        server.login(email_from, password)
        server.send_message(msg)
        log_msg = f'''
            The message to the mail {email_to} has been sent.
            It took {time.time() - start:0.1f} seconds.
        '''
        logging.info(log_msg)
        return True
    except SMTPException as e:
        logging.error(e)
        return False


def parse_emails(file_path):
    if file_path:
        with open(file_path, 'r') as f:
            email_list = f.read().splitlines()
            return email_list
    return False
