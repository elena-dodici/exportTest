import os
# from exportFinalReport import get_final_report
from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

import time
from datetime import date
import logging
import threading 
import requests
import msal
from msal import PublicClientApplication
import webbrowser

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)

current_date = date.today()

# def run_export(file_path, proName):
    
#     if not os.path.isdir(file_path):
#         time.sleep(10) # wait for 1 second before checking again
#     get_final_report(proName)

## powerapp only allow GET method
# @app.route('/export', methods=['GET'])
# def exportReport():
#     param1 = request.args.get('p1', "default_projectID")
#     param2 = request.args.get('p2', "default_projectName")
#     param3 = request.args.get('p3', "default_userName")
#     print(f"rojectname: {param2}")
#     # path = f'\\\\eeazurefilesne.file.core.windows.net\\generalshare\\Ethos Digital\\BMS Points Generator Reports\\Points Schedule - {param2} - {current_date.day:02d}-{current_date.month:02d}-{current_date.year}.csv'
#     # pass the parameters to the ExampleHandler
#     # thread = threading.Thread(target=run_export, args=(path, param2))
#     # thread.start()
#     # thread.join() # main thread relies on the result of other threads, so join needed
#     return render_template('index.html', param1=param1, param2=param2, param3=param3)

@app.route('/token',methods=['GET', 'POST','PUT'])
def index():
    if request.method == 'POST':
        print(request.form)
    elif request.method == 'PUT':
        print("put")
    else:
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            json = request.get_json()
            data = json.loads(request.data)
            print(data)
            return json
        else:
            return 'Content-Type not supported!'
    


@app.route('/')
def mainpage():
   print('Request for index page received')
   return render_template('export.html')

@app.route('/hello')
def hello():
   ## test

   return redirect(url_for('export'))


# @app.route('/project/<projectName>')s
# def print(projectName):
   
#    return render_template('hello.html', name=projectName)

#    if name:
#        print('Request for hello page received with name=%s' % name)
#        return render_template('hello.html', name = name)
#    else:
#        print('Request for hello page received with no name or blank name -- redirecting')
#        return redirect(url_for('index'))



if __name__ == '__main__':
   app.run(debug=True, port=5000)