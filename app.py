import os
from flask import Flask, render_template, request
from predictor import check,check2
author = 'TEAM DELTA'

app = Flask(__name__, static_folder="static")

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/random')
def mypage():
    return render_template('random.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    target = os.path.join(APP_ROOT, 'images/')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist('file'):
        print(file)
        filename = file.filename
        print(filename)
        dest = '/'.join([target, filename])
        print(dest)
        file.save(dest)
        statusx=check2(filename)
        print(statusx)
        if statusx==True:
            status = check(filename)
            return render_template('complete.html', image_name=filename, predvalue=status)
        else:
            return render_template('random.html', image_name=filename)
    
@app.route('/my-link/')
def my_link():
  print ('I got clicked!')
  return render_template('upload.html')




if __name__ == "main":
    app.run(port=4555, debug=True)
