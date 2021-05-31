# pip install yagmail
# pip install keyring
import credentials
import yagmail


def mail_sender(content, subject, recipient):

    yag = yagmail.SMTP(credentials.Credentials.email, credentials.Credentials.password, host='smtp.gmail.com')
    yag.send(recipient, subject, content)


mail_sender("Mail testowy 1234", "TEST_1", "gawroncode@gmail.com")
