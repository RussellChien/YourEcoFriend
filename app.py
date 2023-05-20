# Import necessary Flask modules
from flask import Flask, render_template

# Create Flask app
app = Flask(__name__)

# Define routes
@app.route('/')
def home():
    # Retrieve progress data (dummy data for demonstration)
    progress_data = {
        'task1': 50,
        'task2': 75,
        'task3': 20,
        'task4': 100
    }

    # Render the template with progress data
    return render_template('dashboard.html', progress_data=progress_data)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
