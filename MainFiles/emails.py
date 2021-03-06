# Fitness Planner E-mails
# Send automated E-mails from Python Fitness Planner
# Created 11/22/2014
#----------------------------------------------------------------------------------------------------------------------#

import smtplib
import email.utils
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
import string


# Create String from Files
def file_to_string(document):
    doc = open(document, 'r')
    file_contents = doc.read()
    doc.close()
    return file_contents


def generate_password(size=6, chars=string.ascii_uppercase + string.digits):
    pw = ''.join(random.choice(chars) for _ in range(size))
    return pw


def password_html(password):
    reset = file_to_string('PasswordReset.html')
    reset = reset % password
    return reset


def password_txt(password):
    reset = file_to_string('PasswordReset.txt')
    reset = reset % password
    return reset


# Send E-mail
def send_email(address, subject, html_message, string_message):
    host = 'smtp.gmail.com'
    email_addr = "python.fitness.planner@gmail.com"
    password = 'PopPop92'

    msg = MIMEMultipart('alternative')
    msg.set_unixfrom('author')
    msg['To'] = email.utils.formataddr(('Recipient', email))
    msg['From'] = email.utils.formataddr(('Python Fitness Planner', email_addr))
    msg['Subject'] = subject

    part1 = MIMEText(string_message, 'plain')
    part2 = MIMEText(html_message, 'html')

    # attaching message to e-mail. Priority list from least preferred to most preferred.
    msg.attach(part1)
    msg.attach(part2)

    # Connecting to the server
    server = smtplib.SMTP(host, 587)

    try:
        # Authenticate
        server.ehlo()

        # Use TLS
        if server.has_extn('STARTTLS'):
            server.starttls()
            # Authenticate over secure connection
            server.ehlo()

        server.login(email_addr, password)
        server.sendmail(email_addr, [address], msg.as_string())

    except Exception as e:
        print e

    finally:
        server.quit()


if __name__ == '__main__':
    html_string = file_to_string('WelcomeEmail.html')
    text_string = file_to_string('WelcomeEmail.txt')
    password = generate_password()
    reset_html = password_html(password)
    reset_txt = password_txt(password)
    send_email('guy.turner@hotmail.com', 'Welcome to Python Fitness Planner', html_string, text_string)
    send_email('guy.turner@hotmail.com', 'Password Reset', reset_html, reset_txt)
