from flask import Flask, request, redirect, render_template_string, url_for

app = Flask(__name__)

# Login form template
login_template = '''
<!DOCTYPE html>
<html>
<head>
    <title>Login Page</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 400px;
            margin: 0 auto;
            padding: 20px;
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
        }
        input[type="text"], input[type="password"] {
            width: 100%;
            padding: 8px;
            box-sizing: border-box;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 15px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <h2>Login</h2>
    <form method="POST" action="{{ url_for('login') }}">
        <div class="form-group">
            <label for="username">Username:</label>
            <input type="text" id="username" name="username" required>
        </div>
        <div class="form-group">
            <label for="password">Password:</label>
            <input type="password" id="password" name="password" required>
        </div>
        <button type="submit">Login</button>
    </form>
</body>
</html>
'''

# Success page template
success_template = '''
<!DOCTYPE html>
<html>
<head>
    <title>Success</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 400px;
            margin: 0 auto;
            padding: 20px;
            text-align: center;
        }
        h1 {
            color: #4CAF50;
        }
        a {
            color: #2196F3;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <h1>Success!</h1>
    <p>You have successfully logged in.</p>
    <a href="{{ url_for('index') }}">Back to Login</a>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(login_template)

@app.route('/login', methods=['POST'])
def login():
    # In a real application, you would validate the username and password here
    username = request.form.get('username')
    password = request.form.get('password')
    
    # For demonstration purposes, we're just redirecting to success
    # without actual authentication
    return redirect(url_for('success'))

@app.route('/success')
def success():
    return render_template_string(success_template)

if __name__ == '__main__':
    app.run(debug=True)