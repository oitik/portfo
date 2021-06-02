from flask import Flask, render_template, request, url_for, redirect
import csv
app = Flask(__name__)


@app.route("/")
def my_home():
    return render_template('index.html')


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('info.txt', newline='', mode='a') as info:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        info.write(f'email:{email}\nsubject:{subject}\nmessage:{message}\n\n')


def write_to_csv(data):
    with open('database2.csv', newline='', mode='a') as info2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(info2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'Something went wrong'







