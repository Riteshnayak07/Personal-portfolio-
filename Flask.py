from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Index.html')

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    # Handle data (save or email)
    return f"Thank you {name}, your message has been sent!"

if __name__ == '__main__':
    app.run(debug=True)

