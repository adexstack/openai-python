from flask import Flask, render_template, request, redirect

app = Flask(__name__)


# Home page
@app.route('/')
def home():
    return render_template('index.html')


# Login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Add your login logic here

        # Redirect to a different page after successful login
        return redirect('/dashboard')

    return render_template('login.html')


# Dashboard page
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


if __name__ == '__main__':
    app.run()
