# Markwise — NumPy Student Marks

A responsive, distinctive student-marks analytics web app built with **Python, Flask, and NumPy** for Task 11.

## Features
- Accepts a comma-separated or newline-separated list of marks.
- Validates that marks are numeric and between 0 and 100.
- Calculates mean, median, maximum, minimum, population standard deviation, and score range using NumPy.
- Shows the dataset and a plain-language interpretation.
- Responsive interface with no database or paid service required.

## Requirements
- Python 3.10 or newer
- pip

## Run from the terminal

### Windows PowerShell
```powershell
cd numpy-student-marks
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python app.py
```

If PowerShell blocks activation, run `.\.venv\Scripts\python.exe -m pip install -r requirements.txt` and then `.\.venv\Scripts\python.exe app.py`.

### Windows Command Prompt
```bat
cd numpy-student-marks
py -m venv .venv
.venv\Scripts\activate.bat
python -m pip install --upgrade pip
pip install -r requirements.txt
python app.py
```

### macOS / Linux
```bash
cd numpy-student-marks
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python app.py
```

Open **http://127.0.0.1:5000** in your browser. Keep the terminal open while using the app. Press `Ctrl+C` to stop it.

## Example dataset
`78, 85, 92, 67, 88, 74, 95, 81`

For this dataset the app computes:
- Mean: 82.50
- Median: 83.00
- Maximum: 95
- Minimum: 67
- Population standard deviation: approximately 8.39

The standard deviation uses NumPy's default `ddof=0` (population standard deviation).

## Project structure
```text
numpy-student-marks/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── templates/
│   └── index.html
└── static/
    └── style.css
```

## GitHub submission
1. Create a **Public** repository at https://github.com/new named `numpy-student-marks`.
2. Do not select “Add a README”, `.gitignore`, or license on GitHub because this project already contains files for them.
3. Extract the ZIP and open a terminal in the extracted `numpy-student-marks` folder.
4. Run the commands in the submission guide provided with this project. Replace the example username with your own GitHub username if needed.

## Notes
- The Flask development server is for local learning/demo use, not production deployment.
- No student data is saved to a database; calculations happen when the form is submitted.
