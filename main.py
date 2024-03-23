
from flask import Flask, render_template, request, redirect, url_for
import string

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
  if request.method == 'POST':
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    errors = []

    if not name or not name.strip():
      errors.append('Name is required')
    if not email or not email.strip():
      errors.append('Email is required')
    if not password or not password.strip():
      errors.append('Password is required')
    if password and len(password) < 8:
      errors.append('Password must be at least 8 characters long')

    if not errors:
      # Here we would normally create a user account in the database
      # Since we don't have a database in this example, we just redirect to the homepage
      return redirect(url_for('index'))

  return render_template('register.html', errors=errors)

if __name__ == '__main__':
    app.run(debug=True)
