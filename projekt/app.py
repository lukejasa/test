from flask import Flask, render_template, request, redirect, flash
import smtplib

app = Flask(__name__)
app.secret_key = "nejaky_tajny_klic"  # pro flash zprávy

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        jmeno = request.form["jmeno"]
        email = request.form["email"]
        zprava = request.form["zprava"]

        # zde by šel poslat email přes SMTP
        print(f"Jméno: {jmeno}, Email: {email}, Zpráva: {zprava}")

        flash("Zpráva byla úspěšně odeslána!")
        return redirect("/")

    return render_template("index.html")