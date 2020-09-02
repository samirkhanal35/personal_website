from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
   return render_template("home.html")

@app.route('/projects')
def projects():
   return render_template("projects.html")

@app.route('/articles')
def articles():
   return render_template("articles.html")


if __name__ == '__main__':
   # app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
   app.run(debug = True)