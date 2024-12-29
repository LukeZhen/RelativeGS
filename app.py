from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)

# Configurations
UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Helper function: Calculate grades
def calculate_grades(scores):
    mean = np.mean(scores)
    std = np.std(scores)

    grades = []
    for score in scores:
        if score >= mean + 1.5 * std:
            grades.append('A')
        elif score >= mean + 0.5 * std:
            grades.append('B')
        elif score >= mean - 0.5 * std:
            grades.append('C')
        elif score >= mean - 1.5 * std:
            grades.append('D')
        else:
            grades.append('F')
    return grades

# Helper function: Generate grade distribution plot
def generate_grade_plot(grades):
    grade_counts = pd.Series(grades).value_counts().sort_index()
    plt.figure()
    grade_counts.plot(kind='bar', color=['blue', 'green', 'yellow', 'orange', 'red'])
    plt.title('Grade Distribution')
    plt.xlabel('Grades')
    plt.ylabel('Number of Students')
    plt.tight_layout()
    
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    plt.close()  # Close the plot to free resources
    return base64.b64encode(image_png).decode('utf-8')


# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload-grades', methods=['POST'])
@app.route('/upload-grades', methods=['POST'])
@app.route('/upload-grades', methods=['POST'])
def upload_grades():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    try:
        # Read the CSV file
        data = pd.read_csv(filepath)

        # Ensure required columns are present
        if 'Name' not in data.columns or 'Score' not in data.columns:
            return jsonify({'error': 'CSV must contain "Name" and "Score" columns'}), 400

        # Add a unique Student ID
        data['StudentID'] = [f"S{str(i+1).zfill(3)}" for i in range(len(data))]

        # Calculate grades
        scores = data['Score']
        grades = calculate_grades(scores)
        data['Grade'] = grades

        # Prepare student data for JSON response
        students = data[['StudentID', 'Name', 'Score', 'Grade']].to_dict(orient='records')

        # Generate grade distribution plot
        grade_plot = generate_grade_plot(grades)

        # Return response with all students
        return jsonify(
            {
                "message": "Grades processed successfully",
                "students": students,  # Include all student data dynamically
                "grade_plot": grade_plot
            }
        )
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
