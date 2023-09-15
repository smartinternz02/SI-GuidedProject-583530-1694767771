# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 15:41:46 2023

@author: tallu
"""

from flask import Flask, request, render_template
import ibm_db
app1 = Flask(__name__)
app1.secret_key ="abcd"
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=fbd88901-ebdb-4a4f-a32e-9822b9fb237b.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=32731;UID=jvc88039;PWD=E7lcfT1MARIu0qcg;SECURITY=SSL;SSLCERTIFICATE=DigiCertGlobalRootCA(1).crt",'','');
print(conn)
print(ibm_db.active(conn))

@app1.route("/")
def index():
    return render_template("index.html")

@app1.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app1.run(debug=True, host="0.0.0.0")

