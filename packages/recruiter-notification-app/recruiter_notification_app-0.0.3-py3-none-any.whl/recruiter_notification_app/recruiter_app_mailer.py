from flask_mail import Mail, Message
import os


class MailService:
    def __init__(self, app):
        self.sender_email = os.getenv('MAIL_USERNAME')
        self.mail = Mail(app)

    def send_mail(self, receiver, token):
        msg = Message('Interview-Software Engineer', sender=self.sender_email,
                      recipients=[receiver])
        msg.html = f"""
        <html><body>
        <p>Dear Candidate,</p>
        <p>To continue your next interview process, please click the below link and submit your answers with in next 2 days: </p>
        <p><a href=`http://127.0.0.1:5000/home?token={token}`>Exam link</a></p>
        <p>Thanks and Regards,</p>
        <p>HushHush Recruiter HR</p>
        """
        self.mail.send(msg)
        print("Message send successfully")
