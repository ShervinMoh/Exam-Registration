# Exam Registration

## Overview
The "Exam Registration Form" is a web-based HTML application designed to collect user information and exam preferences for registration purposes. It includes a responsive design, validation, and user-friendly interface, allowing users to upload required documents and submit the form securely.

## Features
- **Dynamic Layout**: The form adapts to different screen sizes for better user experience.
- **Logo & Header**: Displays a logo and a form title to enhance visual branding.
- **Input Validation**: Ensures required fields are filled and validates email format.
- **Exam Type Selection**: Users can choose different types of exams and relevant sections.
- **Price Calculation**: Dynamically displays pricing based on selected options.
- **File Uploads**: Allows users to upload necessary documents, such as a passport image and payment receipt.

## Code Structure

### HTML
- **DOCTYPE**: Declares the document type and HTML version.
- **Head Section**:
  - `meta` tags for character set and viewport settings for responsiveness.
  - Title for the browser tab.
  - Internal CSS styles for layout and design.
  
- **Body Section**:
  - **Header**: Contains the form title and logo.
  - **Form**: Wrapped in a `<form>` element for data submission with various input fields:
    - **Text Inputs**: For first name, last name, phone number, and email.
    - **Radio Buttons**: To select exam types.
    - **Checkbox Groups**: For selecting individual exam sections and options.
    - **File Inputs**: For uploading necessary documents.
    - **Submit Button**: To submit the form.

### CSS Styles
- **Body**: Sets max-width, padding, and styling for the overall layout.
- **Header & Logo**: Flexbox layout for aligning title and logo with appropriate margins.
- **Form Inputs**: Styling for labels, input fields, buttons, and error messages.
- **Animation**: A bounce animation on the logo for a lively interface.
- **Conditional Styling**: User feedback through error messages and pricing displays.

### JavaScript
- **Event Listeners**: Manage form interactions, such as changing exam types and updating price displays.
- **Validation Functionality**: Checks if required fields and options are selected before submission.
- **Dynamic Price Calculation**: Updates totals based on user selections in checkbox groups.
- **Form Submission**: Uses the Fetch API to submit form data asynchronously, displaying success or error messages based on the server response.

## Usage
1. Open the HTML file in a web browser.
2. Fill in the required fields, select the appropriate exam type, and upload the necessary documents.
3. Click the "Submit" button to send the registration data. 
4. Receive feedback on submission success or errors directly on the form interface.

## Requirements
- A web browser (e.g., Chrome, Firefox).
- Internet connection (for processing submissions, if applicable).

---

### 1. HTML Structure
```html
<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Exam Registration Form</title>
```
- **DOCTYPE**: Defines the document as an HTML5 document.
- **`<html>` Attribute**: Sets the language to English and the text direction to left-to-right.
- **Head Section**:
  - **`<meta>` Tags**: Define the character encoding and ensure responsiveness on different devices.
  - **Title**: Sets the title that appears in the browser tab.

### 2. CSS Styles
```css
body {
    position: relative;
    font-family: Arial, sans-serif;
    max-width: 800px;
    margin: 0 auto;
    padding: 20px 70px !important;
}
```
- **Body Styles**: Centers the content, sets a maximum width, and adds padding for aesthetics.
- The use of `!important` ensures that the padding is not overridden by other styles.

### 3. Form Layout
```html
<div class="form-container">
    <form id="myForm" method="POST" enctype="multipart/form-data">
        <!-- Form groups for inputs -->
        <div class="form-group">
            <label for="input1">First Name <span class="required">*</span></label>
            <input type="text" id="input1" name="input1" placeholder="Enter your first name" required>
            <div class="error" id="input1-error">Please enter your first name</div>
        </div>
        <!-- More inputs follow -->
        <button type="submit">Submit</button>
    </form>
</div>
```
- **Form Element**: Uses `POST` method for data submission and allows for file uploads.
- **Form Groups**: Each group has a label, input field, and an error message element that displays when there's validation feedback.

### 4. JavaScript Functionality
```javascript
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('myForm');
    const examTypeRadios = document.querySelectorAll('input[name="exam-type"]');
    // Other initializations ...
    
    // Update checkbox groups based on selected exam type
    function updateCheckboxGroups() {
        // Logic to show/hide checkbox groups
    }
    
    // Form validation on submit
    form.addEventListener('submit', async function(event) {
        event.preventDefault(); // Prevent default submission
        let isValid = true;
        
        // Validation checks
        // If valid, fetch submission
    });
});
```
- **Event Listener**: Ensures that JavaScript runs after the DOM is fully loaded.
- **Form Submission Handling**: Prevents default submission and performs validation.
- **Functionality Updates**: Controls showing/hiding sections based on user selections (e.g., exam type) and updates prices dynamically.

---

### 1. HTML Document Declaration
```html
<!DOCTYPE html>
<html lang="en">
```
- The `<!DOCTYPE html>` declaration defines the document as an HTML5 document.
- `<html lang="en">` indicates that the language of the document is English.

### 2. Head Section
```html
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Exam Registration Portal</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
```
- **Character Encoding**: `<meta charset="UTF-8">` ensures that the document handles text properly, especially special characters.
- **Viewport Tag**: `<meta name="viewport" ...>` makes the site responsive, scaling correctly on various devices.
- **Title**: Sets the browser tab title to "Exam Registration Portal."
- **Font Link**: Loads the Poppins font from Google Fonts, enhancing the text aesthetic.

### 3. CSS Styles Within Style Tags
```css
:root {
    --primary: #006D77; /* Primary color */
    --secondary: #83C5BE; /* Secondary color */
    --accent: #FFDDD2; /* Accent color */
    --light: #EDF6F9; /* Light color */
    --dark: #2B2D42; /* Dark color */
    --error: #E63946; /* Error color */
}
```
- **CSS Variables**: These root variables define color schemes used throughout the document, making it easy to maintain and change styles.

### 4. General Styles and Layout
```css
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}
```
- **Universal Selector**: The asterisk (*) applies `box-sizing`, `margin`, and `padding` to all elements, ensuring consistent sizing and spacing.

### 5. Body Styles
```css
body {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh; /* Full viewport height */
    background: linear-gradient(135deg, #f5f7fa 0%, #e4e8f0 100%);
    font-family: 'Poppins', sans-serif;
}
```
- **Flexbox Layout**: Centers content both vertically and horizontally. The `min-height` ensures that it takes up at least the full height of the viewport.
- **Background Gradient**: A soft gradient background for a visually appealing context.

### 6. Design Elements
```css
.tape {
    position: absolute;
    background: linear-gradient(90deg, var(--primary), var(--secondary));
    height: 15px;
    width: 100%;
    z-index: 1; /* Positioned under other content */
}
```
- **Tape Elements**: Creates a decorative tape effect at the top and bottom of the content area using a gradient of primary and secondary colors.

### 7. Content Styles
```css
.content {
    padding: 40px;
    background-color: white;
    border-radius: 16px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
}
```
- **Content Area**: The main registration container, which has padding, background color, slight rounded corners, and a subtle shadow to lift it off the background.

### 8. Typography and Elements
```css
h1 {
    color: var(--primary);
    font-size: 2.5rem;
    font-weight: 600;
}
```
- **Heading Styles**: Sets the color, size, and weight of the main heading to make it prominent.

### 9. Important Note and Requirements List
```css
.important-note {
    color: var(--error);
    background-color: rgba(230, 57, 70, 0.1);
}
```
- **Error Highlighting**: The important note section uses distinctive styling to attract attention, indicating critical information.

### 10. Button Design
```css
.next-button {
    padding: 14px 32px;
    background: linear-gradient(135deg, var(--primary), var(--secondary));
    color: white;
}
```
- **Button Styles**: The registration button is styled with padding, gradient background, and transitions for hover effects, improving interactivity.

### 11. Button Click Functionality
```html
<button class="next-button" onclick="window.location.href='main_page'">Continue to Registration</button>
```
- **Navigation**: Clicking the button redirects to the 'main_page', which presumably contains the actual registration form.

### 12. Responsive Design
```css
@media (max-width: 768px) {
    .content {
        padding: 30px 20px;
        width: 95%;
    }
}
```
- **Media Queries**: Adjusts layout and text sizes for smaller screens, ensuring accessibility and user friendliness on mobile devices.

---

### 1. Document Structure
```html
<!DOCTYPE html>
<html lang="en">
```
- Declares the type of document as HTML5 and specifies English as the language for the document.

### 2. Head Section
```html
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin Dashboard</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
```
- **Character Set**: `<meta charset="UTF-8">` specifies the character encoding.
- **Viewport Settings**: Ensures proper display on mobile devices.
- **Title**: Sets the title of the page to "Admin Dashboard."
- **Font Link**: Loads the Poppins font from Google Fonts for styling the text.

### 3. CSS Styles
```css
:root {
    --primary: #006D77; /* Main color scheme */
    --secondary: #83C5BE;
    --accent: #FFDDD2;
    --dark: #2B2D42;
    --gray: #6c757d;
}
```
- **CSS Variables**: These variables define color schemes that can be reused throughout the stylesheet.

### 4. General Reset and Body Styles
```css
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: 'Poppins', sans-serif;
    margin: 0;
    padding: 30px;
    background-color: #f8f9fa;
    color: var(--dark);
    line-height: 1.6;
}
```
- **Reset Styles**: The universal selector (*) ensures all elements have consistent styling for margin and padding.
- **Body Styles**: Defines the body font, background color, and text color. It also adds padding for spacing.

### 5. Container and Heading Styles
```css
.container {
    max-width: 1400px;
    margin: 0 auto; /* Center aligns */
}

h1 {
    color: var(--primary);
    text-align: center;
    margin-bottom: 40px;
    font-size: 2.5rem;
}
```
- **Container**: Centers the dashboard content and restricts its maximum width.
- **Heading**: Styles the main title with color, size, and alignment.

### 6. Submissions Container and Submission Card
```css
.submissions-container {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(380px, 1fr));
    gap: 30px;
}

.submission {
    background: white;
    padding: 25px;
    border-radius: 12px;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);
    transition: all 0.3s;
}
```
- **Grid Layout**: The submissions are displayed in a responsive grid format that adapts to screen size.
- **Submission Card**: Each submission has a card style with padding, shadow, and rounded corners.

### 7. Submission Interaction Styles
```css
.submission:hover {
    transform: translateY(-8px);
    box-shadow: 0 10px 25px rgba(0, 109, 119, 0.15);
}
```
- **Hover Effect**: Submissions lift slightly and show a deeper shadow when hovered over, creating an interactive experience.

### 8. Submission Details
```css
.field {
    margin-bottom: 16px;
    display: flex;
}

.field label {
    font-weight: 500;
    color: var(--primary);
}
```
- **Field Structure**: Each piece of information is organized in a label-value format using flexbox for alignment.

### 9. Image Uploads
```css
img {
    max-width: 100%;
    max-height: 200px;
    margin-top: 10px;
    border-radius: 8px;
}
```
- **Image Styles**: Ensures images fit within their container and have a consistent appearance with rounded corners.

### 10. No Submissions Message
```css
.no-submissions {
    text-align: center;
    padding: 60px 40px;
}
```
- **Empty State**: Styles a message when there are no submissions available, providing user feedback.

### 11. Download Button
```css
.download-btn {
    display: inline-flex;
    margin-top: 12px;
    padding: 8px 16px;
    background-color: var(--primary);
    color: white;
}
```
- **Button Styles**: A styled button for downloading files that changes on hover to enhance user interaction.

### 12. Responsive Design
```css
@media (max-width: 768px) {
    .submissions-container {
        grid-template-columns: 1fr; /* Stack on small screens */
    }
}
```
- **Media Queries**: Adjusts the layout for screens smaller than 768px to stack the submission cards vertically.

### 13. Body Content
```html
<body>
    <div class="container">
        <h1>Admin Dashboard</h1>
        
        {% if submissions %}
            <div class="submissions-container">
                {% for submission in submissions %}
                    <div class="submission">
                        <!-- Submission Details Here -->
                    </div>
                {% endfor %}
            </div>
        {% else %}
            <div class="no-submissions">
                <p>No submissions found</p>
            </div>
        {% endif %}
    </div>
</body>
```
- **Conditional Rendering**: Uses template syntax (likely with a web framework like Flask) to display submissions if available. If not, it shows a message indicating that there are no submissions.
- **Submission Details**: Inside the loop, it dynamically inserts each submission’s details, including options based on the exam type, contact information, and uploaded files with download links.

---

### 1. Document Structure
```html
<html>
<head>
    <style>
```
- Opens the HTML document and starts the head section where CSS styles will be defined.

### 2. Font Import
```css
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&display=swap');
```
- This imports the Poppins font from Google Fonts for use throughout the document.

### 3. CSS Variables
```css
:root {
    --primary: #006D77;
    --secondary: #83C5BE;
    --light: #EDF6F9;
    --accent: #FFDDD2;
    --dark: #2B2D42;
}
```
- Defines a set of CSS variables (custom properties) for color themes, making it easy to maintain and change colors throughout the stylesheet.

### 4. General Reset and Body Styles
```css
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}
```
- **CSS Reset**: Resets margin and padding for all elements to ensure consistency.
  
```css
body {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    margin: 0;
    font-family: 'Poppins', sans-serif;
    background: linear-gradient(135deg, var(--primary), var(--secondary));
    background-size: 400% 400%;
    animation: gradient 10s ease infinite;
    color: var(--dark);
}
```
- **Body Styles**: The body uses flexbox to center content vertically and horizontally. It has a gradient background and animation that shifts smoothly over time.

### 5. Gradient Animation
```css
@keyframes gradient {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}
```
- Defines the animation for the background gradient, creating a smooth transition of colors.

### 6. Login Container Styles
```css
.login-container {
    text-align: center;
    width: 380px;
    padding: 40px 30px;
    background: rgba(255, 255, 255, 0.95);
    border-radius: 16px;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    backdrop-filter: blur(8px);
    border: 1px solid rgba(255, 255, 255, 0.18);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}
```
- Styles the login container with a semi-transparent background, rounded corners, and a shadow effect. The backdrop filter adds a blur effect when placed over a background.

### 7. Hover Effect for Login Container
```css
.login-container:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 40px rgba(0, 0, 0, 0.15);
}
```
- This effect gives a subtle lift and enhanced shadow when the user hovers over the login container.

### 8. Logo Image Styling
```css
img {
    width: 100px;
    height: 100px;
    object-fit: contain;
    margin-bottom: 25px;
    filter: drop-shadow(0 4px 8px rgba(0, 109, 119, 0.2));
    transition: transform 0.3s ease;
}
```
- Styles the logo image to be responsive, adds a drop shadow, and gives a hover effect that scales the image slightly.

### 9. Heading Styles
```css
h1 {
    font-size: 24px;
    font-weight: 600;
    margin: 0 0 30px 0;
    color: var(--primary);
    position: relative;
}
```
- Styles the main heading with size, weight, and color.

```css
h1::after {
    content: '';
    position: absolute;
    width: 50%;
    height: 3px;
    bottom: -8px;
    left: 25%;
    background: var(--accent);
    border-radius: 3px;
}
```
- Adds a colored underline effect under the heading using a pseudo-element.

### 10. Form Group Styles
```css
.form-group {
    margin-bottom: 20px;
    text-align: left;
}
```
- Styles the form groups to keep their contents aligned left and provides space between them.

### 11. Input Field Styles
```css
input {
    width: 100%;
    padding: 12px 15px;
    margin: 8px 0;
    border: 2px solid rgba(0, 0, 0, 0.1);
    border-radius: 8px;
    font-size: 14px;
    transition: all 0.3s ease;
    background: rgba(255, 255, 255, 0.8);
}
```
- Styles the input fields for a pleasing appearance with padding, border, and background.

```css
input:focus {
    outline: none;
    border-color: var(--secondary);
    box-shadow: 0 0 0 3px rgba(131, 197, 190, 0.3);
}
```
- These styles enhance input fields when they are focused, changing their border color and adding a glow effect.

### 12. Submit Button Styles
```css
input[type="submit"] {
    background-color: var(--primary);
    color: white;
    border: none;
    cursor: pointer;
    font-weight: 500;
    margin-top: 20px;
    padding: 14px;
    transition: all 0.3s ease;
}
```
- Styles the submit button, giving it a background color, rounded corners, and transition effects.

### 13. Hover Effect for Submit Button
```css
input[type="submit"]:hover {
    background-color: var(--secondary);
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0, 109, 119, 0.3);
}
```
- Adds an interactive effect to the submit button for better user feedback on hover.

### 14. Forgot Password Link Styles
```css
.forgot-password {
    display: block;
    margin-top: 15px;
    color: var(--primary);
    text-decoration: none;
}
```
- Styles the "Forgot password?" link with margin and color.

```css
.forgot-password:hover {
    color: var(--secondary);
    text-decoration: underline;
}
```
- Changes the link’s color and underlines it on hover for clarity.

### 15. Responsive Design
```css
@media (max-width: 480px) {
    .login-container {
        width: 90%;
        padding: 30px 20px;
    }
}
```
- Adjusts the login container’s width and padding for smaller screens to ensure mobile-friendliness.

### 16. Body Content
```html
<body>
    <div class="login-container">
        <img src="https://www.pngmart.com/files/21/Admin-Profile-Vector-PNG-Clipart.png" alt="Logo">
        <h1>Welcome Back</h1>
        <form method="POST">
            <div class="form-group">
                <label for="username">Username</label>
                <input type="text" id="username" name="username" placeholder="Enter your username" required>
            </div>
            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" id="password" name="password" placeholder="Enter your password" required>
            </div>
            <input type="submit" value="Sign In">
            <a href="#" class="forgot-password">Forgot password?</a>
        </form>
    </div>
</body>
```
- **Login Form Content**: Contains the logo, a welcome message, a form with username and password fields, and a submit button. The form uses POST method for submission.
- The link for "Forgot password?" is included for user convenience.

---

### 1. Importing Necessary Libraries
```python
from flask import Flask, render_template, request, jsonify, redirect, url_for, send_from_directory
import json
import os
from werkzeug.utils import secure_filename
```
- **Flask**: A micro web framework for making web applications.
- **json**: For handling JSON data.
- **os**: For interacting with the operating system (e.g., creating directories).
- **secure_filename**: A utility that helps ensure uploaded filenames are safe.

### 2. Application Setup
```python
app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'pdf'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
```
- Initializes a Flask app and sets up a configuration for an upload folder and allowed file types.

### 3. Predefined Credentials
```python
USERNAME = 'admin'
PASSWORD = 'admin'
```
- Hardcoded username and password for authentication.

### 4. Ensure Directory Exists
```python
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
```
- Creates the `uploads` directory if it doesn't already exist.

### 5. Setting Up Submissions Data
```python
if not os.path.exists('submissions.json'):
    with open('submissions.json', 'w') as f:
        json.dump([], f)
```
- Checks for the existence of a `submissions.json` file to store form submissions and initializes it if it doesn't exist.

### 6. Helper Function
```python
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
```
- A utility function to check if the uploaded file has an allowed extension.

### 7. Route Handlers

#### Home Page
```python
@app.route('/')
def information():
    return render_template('information.html')
```
- Renders the `information.html` page.

#### Main Page
```python
@app.route('/main_page')
def main_page():
    return render_template('main_page.html')
```
- Renders `main_page.html`.

#### Admin Login
```python
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == USERNAME and password == PASSWORD:
            return redirect(url_for('dashboard'))
        else:
            return render_template('admin.html', error="Invalid credentials")
    return render_template('admin.html')
```
- Handles the admin login process. If the credentials are correct, it redirects to the dashboard; otherwise, it displays an error.

#### Dashboard
```python
@app.route('/dashboard')
def dashboard():
    try:
        ...
        return render_template('dashboard.html', submissions=processed_submissions)
    except Exception as e:
        return render_template('dashboard.html', submissions=[], error=str(e))
```
- Loads and processes submissions from `submissions.json`. It handles specific processing for `B1` options and renders them on `dashboard.html`. If an error occurs, it shows an empty submission list with the error message.

### 8. File Uploads
```python
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
```
- Serves uploaded files from the uploads directory based on the filename.

### 9. Submission Handling
```python
@app.route('/submit', methods=['POST'])
def submit():
    ...
    return jsonify({"status": "success", "message": "Form submitted successfully!"})
```
- Handles form submissions, including managing uploaded files and storing submission data into `submissions.json`. It returns success or failure messages in JSON format.

### 10. Running the Application
```python
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
```
- Runs the Flask application on all available interfaces at port 5000 with debug mode enabled, allowing live reloading and error visibility.

---

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
