"""
An app to demonstrate using OneLogin OpenID Connect (OIDC), with Flask, 
for use login and registration.
"""

from flask import Flask, render_template, redirect, url_for
from flask_oidc import OpenIDConnect

app = Flask(__name__)

app.config["SECRET_KEY"] = "my well-kept secret string"
app.config["OIDC_CLIENT_SECRETS"] = "client_secrets.json"
app.config["OIDC_COOKIE_SECURE"] = False 
app.config["OIDC_CALLBACK_ROUTE"] = "/oidc/callback"
app.config["OIDC_SCOPES"] = ["openid", "email", "profile"]

oidc = OpenIDConnect(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/logout")
def logout():
    oidc.logout()
    return redirect(url_for("index"))
    
@app.route("/private")
@oidc.require_login
def private(user=None):
    if oidc.user_loggedin:
        user = oidc.user_getinfo(["email", "name", "sub"])
    return render_template("private.html", user=user)