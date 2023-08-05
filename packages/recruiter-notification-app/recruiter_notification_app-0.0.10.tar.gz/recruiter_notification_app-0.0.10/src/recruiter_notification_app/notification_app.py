from recruiter_app.elt_app.collections.evaluate_candidates import EvalCandidates
from recruiter_app.utilities.helpers import mongo_global_init
from recruiter_notification_app.recruiter_app_mailer import MailService

from flask import Flask, render_template, request, jsonify
from flask_mail import Mail
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
import os
import random


sender_email = os.getenv('MAIL_USERNAME')
app = Flask(__name__, template_folder='templates')
app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
app.config['MAIL_PORT'] = os.getenv('MAIL_PORT')
app.config['MAIL_USERNAME'] = sender_email
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

s = URLSafeTimedSerializer('Thisisasecret!')
mongo_global_init("cloud")


# Routes to the host and send e-mail
@app.route("/notify_candidates", methods=["post"])
def index():
    """
    payload structure:
    {"candidate_id": "1234"}
    :return:
    """
    print(f"Starting to notify candidates {request.args}")
    recipients = ['anamadheyaashoka005@gmail.com', 'anamadheyaashoka003@gmail.com']
    req_dict = request.get_json(force=True)
    candidate_id = req_dict.get("candidate_id")
    jd_name = req_dict.get("jd_name")
    if candidate_id:
        print(f"request received for id : {candidate_id}")
        rand_mail_idx = random.randint(0, 1)
        token = s.dumps(recipients[rand_mail_idx], salt='test_sample_token')

        eval_candidate_coll = EvalCandidates()
        eval_candidate_coll.candidate_id = candidate_id
        eval_candidate_coll.jd_name = jd_name
        eval_candidate_coll.token = token
        eval_candidate_coll.save()

        mailer_obj = MailService(app)
        mailer_obj.send_mail(recipients[rand_mail_idx], token)
        return '<h1>Email sent!!</h1>'
    return '<h1>Error occurred!!!!!</h1>'


# Route to the home page with set of questions
@app.route("/home", methods=["post", "get"])
def home():
    token = request.args.get("token")
    try:
        s.loads(token, salt='test_sample_token', max_age=100)
    except SignatureExpired:
        return '<h1>Link is expired!</h1>'
    if EvalCandidates.objects(token=token):
        return '<h1>Answers already Submitted!</h1>'

    visible = True
    if request.method == 'POST':
        candidate_name = request.form['candidate_name']
        question1 = request.form['question1']
        question2 = request.form['question2']
        question3 = request.form['question3']

        if question1 is not None or question2 is not None or question3 is not None:
            visible = False

        eval_candidate_coll = EvalCandidates.objects(candidate_id=candidate_name)[0]
        eval_candidate_coll.answer_1 = question1
        eval_candidate_coll.answer_2 = question2
        eval_candidate_coll.answer_3 = question3
        eval_candidate_coll.save()

    return render_template("home.html", visible=visible, token=token)


def main():
    app.run(host="0.0.0.0", port=8080)
