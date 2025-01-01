# Relative Grading System

This project is a Flask-based web application that calculates grades for students based on a relative grading system. It also generates a grade distribution chart to visualize the grading outcome. The application allows users to upload a CSV file containing student data and provides processed results dynamically.

## Features

- **Upload CSV File**: Upload student scores via a CSV file.
- **Dynamic Grade Calculation**: Calculates grades using a relative grading system based on the mean and standard deviation.
- **Grade Distribution Visualization**: Generates a bar chart showing the distribution of grades.
- **Responsive Interface**: User-friendly and interactive web interface built with HTML, CSS, and JavaScript.

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Data Handling**: Pandas (Python)
- **Visualization**: Matplotlib (Python)

## File Structure

```
.
├── app.py               # Main application script
├── templates
│   └── index.html       # Frontend HTML file
├── static
│   └── style.css        # CSS for styling the frontend
├── uploads              # Directory to store uploaded files
└── README.md            # Project description
```

## Setup and Installation

### Prerequisites

Ensure you have the following installed:
- Python 3.7 or higher
- pip (Python package manager)

### Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/relative-grading-system.git
   cd relative-grading-system
   ```

2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

## How to Use

1. Navigate to the application’s homepage.
2. Upload a CSV file containing the student data. The file should include the following columns:
   - `Name`: Student name
   - `Score`: Student score (numeric value)
3. Click the "Upload and Process" button.
4. View the results, including:
   - A table of student grades
   - A grade distribution chart

## Example CSV File Format

| Name           | Score |
|----------------|-------|
| Hannah Johnson | 85    |
| Ian Harris     | 78    |

Ensure the CSV file includes a header row with column names.

## Grading System Logic

Grades are assigned based on the mean and standard deviation of the scores:
- `A`: Score ≥ Mean + 1.5 * Std
- `B`: Mean + 0.5 * Std ≤ Score < Mean + 1.5 * Std
- `C`: Mean - 0.5 * Std ≤ Score < Mean + 0.5 * Std
- `D`: Mean - 1.5 * Std ≤ Score < Mean - 0.5 * Std
- `F`: Score < Mean - 1.5 * Std

## Screenshots

### Upload Interface
![Upload Interface](https://via.placeholder.com/800x400)

### Grade Distribution Chart
![Grade Chart](https://via.placeholder.com/800x400)

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## Contact

For questions or suggestions, please contact:
- **Your Name**: your.email@example.com
- **GitHub**: [your-username](https://github.com/your-username/)

