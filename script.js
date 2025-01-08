document.getElementById('RegistrationForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form submission to check validation first

    let errors = [];

    // Validate Full Name
    let fullname = document.getElementById('fullname').value;
    if (fullname.trim() === '') {
        errors.push("Full Name is required.");
    }

    // Validate Email
    let email = document.getElementById('email').value;
    let emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    if (!email.match(emailRegex)) {
        errors.push("Please enter a valid email.");
    }

    // Validate Username
    let username = document.getElementById('username').value;
    if (username.trim() === '') {
        errors.push("Username is required.");
    }

    // Validate Password
    let password = document.getElementById('password').value;
    if (password.trim() === '') {
        errors.push("Password is required.");
    }

    // Validate Confirm Password
    let confirmPassword = document.getElementById('confirmPassword').value;
    if (confirmPassword !== password) {
        errors.push("Passwords do not match.");
    }

    // Validate Gender
    let gender = document.querySelector('input[name="gender"]:checked');
    if (!gender) {
        errors.push("Please select your gender.");
    }

    // Validate Phone Number
    let phone = document.getElementById('phone').value;
    let phoneRegex = /^[0-9]{10}$/; // Assuming the phone number is 10 digits long
    if (!phone.match(phoneRegex)) {
        errors.push("Please enter a valid phone number.");
    }

    // Show errors if any
    let errorMessages = document.getElementById('errorMessages');
    errorMessages.innerHTML = ''; // Clear previous errors
    if (errors.length > 0) {
        let ul = document.createElement('ul');
        errors.forEach(function(error) {
            let li = document.createElement('li');
            li.textContent = error;
            ul.appendChild(li);
        });
        errorMessages.appendChild(ul);
    } else {
        // If no errors, submit the form (this part should be added to handle form submission)
        alert('Form submitted successfully!');
        // You can now submit the form if using AJAX or directly
        // this.submit();
    }
});