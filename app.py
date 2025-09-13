from flask import Flask, request, render_template, redirect, url_for
from openpyxl import Workbook, load_workbook
import os

app = Flask(__name__)

EXCEL_FILE = "submissions.xlsx"

@app.route("/")
def index():
    return render_template("form.html")

@app.route("/submit", methods=["POST"])
def submit():
    event_name = request.form.get("event_name")
    student_name = request.form.get("student_name")
    college_email = request.form.get("college_email")

    if os.path.exists(EXCEL_FILE):
        wb = load_workbook(EXCEL_FILE)
        ws = wb.active
    else:
        wb = Workbook()
        ws = wb.active
        ws.append(["Event Name", "Student Name", "College Email"])

    ws.append([event_name, student_name, college_email])
    wb.save(EXCEL_FILE)

    return redirect(url_for("view_submissions"))

@app.route("/submissions")
def view_submissions():
    if not os.path.exists(EXCEL_FILE):
        return "<h2>No submissions yet!</h2>"

    wb = load_workbook(EXCEL_FILE)
    ws = wb.active

    rows = list(ws.values)
    table = "<h2>All Submissions</h2><table border='1' cellpadding='5'>"
    for row in rows:
        table += "<tr>" + "".join([f"<td>{cell}</td>" for cell in row]) + "</tr>"
    table += "</table>"

    return table

if __name__ == "__main__":
    app.run(debug=True)
