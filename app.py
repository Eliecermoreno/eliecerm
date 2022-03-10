from flask import Flask, render_template

var_app = Flask (__name__)
@var_app.route("/")
def inicio():
    return "hola mundo"

@var_app.router("/cur")
def cur():
   return render_template("cur.html")


if __name__== "main_":

    var_app.run(host='0.0.0.0',port=3000, debug=True,)