from flask import Flask, render_template, request, redirect, url_for, session, flash
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# For demo purposes only
VALID_USERS = {
    "ananyas05": "Nabh@1005",
    "nabhp10": "Nabh@1005",
}

ENVELOPES = {
    "first": {"title": "Open When it's your Birthday", "video": "Birthday.mp4"},
    "second": {"title": "Open When You Miss Me",    "video": "Miss.mp4"},
    "third": {"title": "Open When You’re Very Happy", "video": "Happy.mp4"},
    "fourth": {"title": "Open When We've had a Fight", "video": "Fight.mp4"},
    "fifth": {"title": "Open When You Doubt Yourself", "video": "Doubt.mp4"},
    "sixth": {"title": "Open When You are Craving a Hug", "video": "Hug.mp4"},
    "seventh": {"title": "Open When You are Bored", "video": "Bored.mp4"},
    "eighth": {"title": "Open When You are Stressed", "video": "Stressed.mp4"},
    "ninth": {"title": "Open When I am in the Flight", "video": "Flight.mp4"},
    "tenth": {"title": "Open Anytime", "video": "Anytime.mp4"},

}

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        u = request.form.get("username", "")
        p = request.form.get("password", "")
        if VALID_USERS.get(u) == p:
            session["user"] = u
            return redirect(url_for("open_when"))
        else:
            flash("Invalid credentials", "error")
    return render_template("login.html")

@app.route("/open-when")
def open_when():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("open_when.html", envelopes=ENVELOPES)

@app.route("/envelope/<name>")
def envelope(name):
    if "user" not in session or name not in ENVELOPES:
        return redirect(url_for("open_when"))
    data = ENVELOPES[name]
    return render_template("envelope.html", name=name, title=data["title"], video=data["video"])

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
