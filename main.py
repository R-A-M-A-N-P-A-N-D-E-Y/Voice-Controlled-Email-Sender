import smtplib  # Simple Mail Transfer Protocol
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage
from email.utils import formataddr

SMTP_SERVER = "smtp.gmail.com"
PORT = 587
EMAIL_ID = "email"
PASSWORD = "PASSWORD"

listener = sr.Recognizer()
engine = pyttsx3.init()

email_list = {
    'buddy1': 'email',
    'buddy2': 'email1',
    'buddy3': 'email2'
}


def send_email(receiver, subject, message):
    server = smtplib.SMTP(SMTP_SERVER, PORT)
    server.starttls()  # Transport Layer Security
    server.login(EMAIL_ID, PASSWORD)
    email = EmailMessage()

    email['From'] = formataddr(('Mini Project', EMAIL_ID))
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)

    server.send_message(email)


def get_info():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        print('Some error occurred unable to send email...!')


def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_email_info():
    talk('To whom you want to send email...!')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk('What is the subject of the email?')
    subject = get_info()
    talk('Tell me the content of the email..?')
    message = get_info()
    send_email(receiver, subject, message)
    talk('Email was sent...!')
    talk('Do you want to send more..!')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()


get_email_info()
