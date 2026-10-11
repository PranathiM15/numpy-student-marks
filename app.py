from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

SAMPLE_MARKS = [78, 85, 92, 67, 88, 74, 95, 81]

def analyze_marks(raw_marks):
    marks = np.array(raw_marks, dtype=float)
    return {
        "count": int(marks.size),
        "mean": round(float(np.mean(marks)), 2),
        "median": round(float(np.median(marks)), 2),
        "maximum": round(float(np.max(marks)), 2),
        "minimum": round(float(np.min(marks)), 2),
        "std": round(float(np.std(marks)), 2),
        "marks": [int(x) if float(x).is_integer() else float(x) for x in marks],
        "spread": round(float(np.max(marks) - np.min(marks)), 2),
    }

@app.route("/", methods=["GET", "POST"])
def index():
    raw = ", ".join(map(str, SAMPLE_MARKS))
    error = None
    result = analyze_marks(SAMPLE_MARKS)
    if request.method == "POST":
        raw = request.form.get("marks", "").strip()
        try:
            pieces = [piece.strip() for piece in raw.replace("\n", ",").split(",") if piece.strip()]
            if not pieces:
                raise ValueError("Enter at least one mark.")
            marks = [float(piece) for piece in pieces]
            if not all(np.isfinite(marks)):
                raise ValueError("Marks must be finite numbers.")
            if any(mark < 0 or mark > 100 for mark in marks):
                raise ValueError("Use marks between 0 and 100.")
            result = analyze_marks(marks)
        except ValueError as exc:
            error = str(exc) if str(exc) else "Please enter valid numbers separated by commas."
            result = None
    return render_template("index.html", raw=raw, result=result, error=error)

if __name__ == "__main__":
    app.run(debug=True)
