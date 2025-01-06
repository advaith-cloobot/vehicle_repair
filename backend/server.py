from flask import Flask,request,render_template, jsonify,Response,make_response
import json
from flask_cors import CORS
import pickle
import random 
import sys
# from Monolithic.postgres_utils import global_init_db,global_init_db_vector
from Monolithic.utils.utils import print_statement,check_login_user,get_token
# from Monolithic.postgres_utils import global_init_db,global_init_db_vector
import logging
from logging import FileHandler
import traceback

import datetime
import traceback

from datetime import datetime

from Monolithic.db_ops.db_ops import insert_new_user

app = Flask(__name__,template_folder='assets/html_templates')

app.debug = True

cors = CORS(app, resources={r"/*": {"origins": "*"}})

app.logger.handlers.clear()
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.DEBUG)

app.logger.debug("Hello World")
ENVIRONMENT = "Server"





@app.route("/check_login",methods=['POST'])
def check_login():
    try:
        print_statement('In check_login :: ',request.json)
        user_email = request.json['user_email']
        user_password = request.json['user_password']
        status,user_id = check_login_user(user_email,user_password)
        if status:
            return get_token(user_email,user_password)
        return {"status":False,"user_id":None}
    except Exception as e:
        print('Exception in check_login ::',e)
        return make_response(jsonify({'error':'Internal error'}), 500)
    

@app.route("/sign_up_user",methods=['POST'])
def sign_up_user():
    try:
        print_statement('In check_ sign up :: ',request.json)
        user_name = request.json['user_name']
        user_email = request.json['user_email']
        user_password = request.json['user_password']
        status,user_id = insert_new_user(user_email,user_password,user_name)
        return {"status":status,'user_id':user_id}
    except Exception as e:
        print('Exception in sign_up_user ::',e)
        return make_response(jsonify({'error':'Internal error'}), 500)
    


    



@app.route("/")
def hello2():
    return "<h1 style='color:blue'>Hello world :)</h1>"

if __name__ == '__main__':
    # print_statement("Server initated")
    # Initialisaing logger
    logging.basicConfig(filename='serverlog_'+str(datetime.today().strftime("%D").replace("/","-"))+'.log', level=logging.DEBUG, force=True, filemode='a')
    # print_statement('---------------------------------------Started')
    
    #initialising db
    # global_init_db()
    
    #For live x.cloobot.ai/backend
    if ENVIRONMENT == "Server":
        app.run(host='0.0.0.0', port=5000, debug=True ,use_reloader=False)
