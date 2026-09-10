# AI School Timetable Optimizer

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/ai-school-timetable-optimizer.git
   cd ai-school-timetable-optimizer
   ```

2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Running the Application

1. Start the FastAPI server:
   ```sh
   uvicorn main:app --reload
   ```

2. Open your web browser and navigate to `http://127.0.0.1:8000/docs` to access the interactive API documentation.

## Project Structure

- `main.py`: FastAPI application entry point.
- `requirements.txt`: List of Python packages required for the project.
- `README.md`: This file.
- `static/index.html`: HTML template for the frontend.
- `timetable.py`: Contains the timetable optimization logic.
- `excel_parser.py`: Handles parsing of Excel files.
- `models.py`: Defines data models for the application.
- `database.py`: Manages the SQLite database.

## Example Usage

1. Place your Excel file in the project directory.
2. Make a POST request to `/optimize-timetable` with the Excel file as a multipart form data.

Example using `curl`:
```sh
curl -X POST "http://127.0.0.1:8000/optimize-timetable" -F "file=@path/to/your/excel_file.xlsx"
```

This will return the optimized timetable in JSON format.