from flask import Flask, redirect, url_for, request,render_template 
app = Flask(__name__)


@app.route('/about')
def aboutpage():
    return render_template("about.html")

@app.route('/')
def mainpage():
    return render_template("index.html")


if __name__=='__main__':
        app.run(debug = True)







