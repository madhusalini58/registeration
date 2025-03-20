from flask import Flask, render_template, request, redirect, url_for, flash
import re

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        fullname = request.form.get('fullname')
        email = request.form.get('mail')
        username = request.form.get('username')
        phone = request.form.get('phone')
        password = request.form.get('pass')
        confirm_password = request.form.get('confirm_pass')
        gender = request.form.get('gender')

        errors = []

        # Validate Full Name
        if not fullname:
            errors.append("Full Name is required.")

        # Validate Email
        email_regex = r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, email):
            errors.append("Please enter a valid email.")

        # Validate Username
        if not username:
            errors.append("Username is required.")

        # Validate Password
        if not password:
            errors.append("Password is required.")

        # Validate Confirm Password
        if password != confirm_password:
            errors.append("Passwords do not match.")

        # Validate Gender
        if not gender:
            errors.append("Please select your gender.")

        # Validate Phone Number
        phone_regex = r'^\d{10}$'  # Assuming the phone number is 10 digits long
        if not re.match(phone_regex, phone):
            errors.append("Please enter a valid phone number.")

        if errors:
            for error in errors:
                flash(error)
            return redirect(url_for ('register'))

        # If no errors, you can process the data (e.g., save to database)
        flash('Registration successful!')
        return redirect(url_for('register'))

    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)