# pip install yagmail
# pip install keyring
from Functional_files import credentials
import yagmail


def mail_sender(content, subject, recipient):
    yag = yagmail.SMTP(credentials.Credentials.email, credentials.Credentials.password, host='smtp.gmail.com')
    yag.send(recipient, subject, content)


def set_email_content(applicant_name, job_offer):
    email_content = "Z przyjemnością informujemy, że aplikant " + applicant_name + " dołączy do nas" \
        " na stanowisku " + job_offer + ". Prosimy oczekiwać kolejnych informacji instrukcyjnych w najbliższych dniach.\n\n\nZ poważaniem,\nZespół HR (nazwa firmy)"

    return email_content


#mail_sender("Mail testowy 1234", "TEST_1", "gawroncode@gmail.com")
