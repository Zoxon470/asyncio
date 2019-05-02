import argparse
import asyncio
import logging
import sys

from email_sender import send_email, parse_emails

logging.basicConfig(
    filename='email.log',
    filemode='w',
    format='%(process)d-%(levelname)s-%(message)s',
    datefmt='%d-%m-%y %H:%M:%S',
)


async def main(args):
    emails = parse_emails(args.file_path)
    if emails:
        for email in emails:
            task = asyncio.create_task(
                send_email(args.host, args.username, email, args.password, args.port, args.subject, args.message)
            )
            await asyncio.wait([task])

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Asynchronous email sending.')
    parser.add_argument(
        '-H', '--HOST', dest='host', default='smtp.gmail.com', help='Email host (default: smtp.gmail.com)')
    parser.add_argument('-u', '--USERNAME', dest='username', help='Email host username')
    parser.add_argument('-p', '--PASSWORD', dest='password', help='Email host password')
    parser.add_argument('-P', '--PORT', dest='port', default=465, help='Email host port (default: 465)')
    parser.add_argument(
        '-f', '--FILE_PATH', dest='file_path', default='emails.txt', help='Email list (default: emails.txt)')
    parser.add_argument('-s', '--SUBJECT', dest='subject', default='H!', help='Email subject (default: H!)')
    parser.add_argument(
        '-m', '--MESSAGE', dest='message', default='Hello, World', help='Email message (default: Hello, World)')

    args = parser.parse_args()
    if not args.username or not args.password:
        parser.print_help()
        sys.exit(0)

    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main(args))
    except NotImplementedError as e:
        logging.info(e)
    finally:
        loop.close()
