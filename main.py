from flask import Flask, render_template, request, jsonify, redirect, url_for, send_from_directory
import json
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'pdf'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Predefined username and password for authentication
USERNAME = 'admin'
PASSWORD = 'admin'

# Ensure uploads directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Ensure 'submissions.json' exists
if not os.path.exists('submissions.json'):
    with open('submissions.json', 'w') as f:
        json.dump([], f)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def information():
    return render_template('information.html')

@app.route('/main_page')
def main_page():
    return render_template('main_page.html')

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

@app.route('/dashboard')
def dashboard():
    try:
        with open('submissions.json', 'r', encoding='utf-8') as f:
            submissions = json.load(f)
        
        # Process submissions to handle B1 options properly
        processed_submissions = []
        for sub in submissions:
            processed_sub = sub.copy()
            
            # Handle B1 options
            if sub.get('exam-type') == 'B1':
                if 'b1-selected-options' in sub:
                    try:
                        processed_sub['selected_options'] = json.loads(sub['b1-selected-options'])
                    except json.JSONDecodeError:
                        processed_sub['selected_options'] = sub.get('b1-options', '')
                else:
                    processed_sub['selected_options'] = sub.get('b1-options', '')
            else:
                # For other exam types
                exam_key = f"{sub.get('exam-type', '').lower()}-options"
                processed_sub['selected_options'] = sub.get(exam_key, '')
            
            processed_submissions.append(processed_sub)
        
        return render_template('dashboard.html', submissions=processed_submissions)
    except Exception as e:
        return render_template('dashboard.html', submissions=[], error=str(e))

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/submit', methods=['POST'])
def submit():
    try:
        form_data = request.form.to_dict()
        files = {}
        
        # Handle file uploads
        for file_key in ['pass-upload', 'image-upload']:
            if file_key not in request.files:
                continue
                
            file = request.files[file_key]
            if file.filename == '':
                continue
                
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                files[file_key] = filename  # Store only filename, not full path
        
        # Handle B1 options specifically
        if form_data.get('exam-type') == 'B1':
            # Get all selected B1 options
            selected_options = request.form.getlist('b1-options')
            form_data['b1-selected-options'] = json.dumps(selected_options)
        
        submission = {**form_data, **files}
        
        # Read existing submissions
        try:
            with open('submissions.json', 'r', encoding='utf-8') as f:
                submissions = json.load(f)
        except:
            submissions = []
        
        # Add new submission
        submissions.append(submission)
        
        # Write back to file
        with open('submissions.json', 'w', encoding='utf-8') as f:
            json.dump(submissions, f, indent=4, ensure_ascii=False)
        
        return jsonify({"status": "success", "message": "Form submitted successfully!"})
    
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)