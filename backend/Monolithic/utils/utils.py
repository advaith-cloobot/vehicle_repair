

from Monolithic.constants.constants import *

from Components.PostgreDBtools.postgres_utils import get_row_by_id,get_rows_by_col

import json
from datetime import datetime,timedelta
import uuid
import hashlib
import jwt
import base64

def print_statement(*args):
    # logger = logging.getLogger(__name__)
    # logger.debug(args)
    print(datetime.now(),args, flush=True)


def get_jwt_token(payload):
    return jwt.encode( payload, JWT_SECRET, algorithm='HS256')


def get_token(useremail, password):
    # print("Entered Get Token")
    user_info = get_rows_by_col(PG_TABLE_IDS_USERS,opt_conds= " lower(" + pg_col_name_dict[PG_TABLE_IDS_USERS][3] + ") = '" + useremail.lower() + "' ")
    if len(user_info):
        row = user_info[0]
        # print("row ::", row)
        if(row[PG_TABLE_IDS_USERS_user_password] == password):

            payload = {
                'user_id': row[0],
                'exp': datetime.utcnow() + timedelta(seconds=JWT_EXP_DELTA_SECONDS)
            }
            #prepare token for new user
            encoded = get_jwt_token(payload)
            try:
                encoded = encoded.decode("UTF-8")
            except Exception as e:
                print_statement("get_token :: Exception Occurred :: ",e)
                
            # print_statement("after login : ",{"data":encoded.decode("UTF-8"),"user_id":row[0],"auth_level":row[5]})
            user_name = row[PG_TABLE_IDS_USERS_user_name]
            if user_name:
                hashed_pwd = hashlib.sha256(str.encode(row[PG_TABLE_IDS_USERS_user_password])).hexdigest()
                # return {"data":encoded.decode("UTF-8"),"user_id":row[0],"auth_level":row[5],"status":status,"user_name":user_info[0][pg_users_index_user_name],'org_name':org_info[pg_org_index_org_name],'org_id':org_info[pg_org_index_org_id],'bot_type':bot_type,'time_zone':org_info[pg_org_index_org_time_zone],"user_phone":user_info[0][pg_users_index_user_phone]}
                # print("\n\ntoken :: ",encoded)
                # Check conversation if available else create new conversation

                return {"data":encoded,"user_id":row[0],"status":True,"user_name":row[PG_TABLE_IDS_USERS_user_name],"user_mail":row[PG_TABLE_IDS_USERS_user_email],"secret":hashed_pwd,"message":"User Logged In"}
        else:
            {"data":False,"message":"Password does not match"}
    return {"data":False,"message":"User does not exist"}






def valid_user(token):
    try:
        decode = jwt.decode(token, JWT_SECRET,algorithms=['HS256'])
        print_statement("decode :: ", decode)
        user_info = get_row_by_id(PG_TABLE_IDS_USERS, pg_col_name_dict[PG_TABLE_IDS_USERS][PG_TABLE_IDS_USERS_user_id], decode['user_id'])
        if len(user_info):
            try:
                return True, decode['user_id']
            except:
                return True, decode['user_id']
    except:
        print_statement("\n\n\nerror in jwt\n\n\n")
    return False, None, None