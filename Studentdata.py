from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def StudentData():
    return render_template("Studentdata.html")

@app.route("/search")
def searchstudent():
    return render_template("search.html")
@app.route("/delete")
def deletestudent():
    return render_template("delete.html")
if __name__ == "__main__":
    app.run()