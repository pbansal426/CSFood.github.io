from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Sample user data (replace with a database)
users = {
    "user1": "password1",
    "user2": "password2"
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username in users and users[username] == password:
        # Successful login
        return "Login successful!"
    else:
        # Invalid credentials
        return "Invalid username or password."
    return render_template("login.html")

if __name__ == '__main__':
    app.run(debug=True)