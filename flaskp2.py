from flask import Flask,request
app=Flask(__name__)
@app.route("/form")
def form():
    return'''
<form action="/submit" method="post">
Name: <input type="text" name="name">
<input type="submit"><br>
Age : <input type="number" name="age"></form>'''

@app.route("/submit",methods=["POST"])
def submit():
    a=request.form.get("name")
    b=request.form.get("age")
    return f"{a} is {b} years old !!!"

if __name__=="__main__":
    app.run(debug=True)

