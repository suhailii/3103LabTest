from flask import Flask,render_template, request, redirect, url_for
import re 


app = Flask(__name__)

def xss_validate_comment(string):
        regex = "(<|%3C)script[\s\S]*?(>|%3E)[\s\S]*?(<|%3C)(\/|%2F)script[\s\S]*?(>|%3E)"
        match = re.search(regex, string)
        if match:
            return True
        else:
            return False
        
def sql_code_validate(string):
        regex="('(''|[^'])*')|(;)|(\b(ALTER|CREATE|DELETE|DROP|EXEC(UTE){0,1}|INSERT( +INTO){0,1}|MERGE|SELECT|UPDATE|UNION( +ALL){0,1})\b)"
        match = re.search(regex, string)
        if match:
            return True
        else:
            return False

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        search = request.form['search']
        print(xss_validate_comment(search))

        if sql_code_validate(search):
                return redirect(url_for('index'))
        else:
            if xss_validate_comment(search):
                return redirect(url_for('index'))
            else:
                if search != "":
                    return render_template("home.html",search = search)
    else:
        return render_template("index.html")

    return redirect(url_for('index'))

@app.route("/home")
def home():

    return render_template("home.html")