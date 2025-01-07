

from Monolithic.constants.constants import *
from Monolithic.constants.gpt_constants import *
from Components.PostgreDBtools.postgres_utils import get_row_by_id,get_rows_by_col
from Components.gpt_tools.gpt_utils import process_gpt_response
import json
from datetime import datetime,timedelta
import uuid
import hashlib
import jwt
import base64


from Monolithic.db_ops.db_ops import insert_vehicle_repair_info,insert_payment_invoice

def print_statement(*args):
    # logger = logging.getLogger(__name__)
    # logger.debug(args)
    print(datetime.now(),args, flush=True)



def check_login_user(user_email, user_password):
    user_info = get_rows_by_col(PG_TABLE_IDS_USERS,opt_conds= " lower(" + pg_col_name_dict[PG_TABLE_IDS_USERS][PG_TABLE_IDS_USERS_user_email] + ") = '" + user_email.lower() + "' ")
    print_statement("user_info :: ",user_info)
    if len(user_info):
        row = user_info[0]
        print_statement("password :: ",user_password," :: ",row[PG_TABLE_IDS_USERS_user_password])
        print_statement(row[PG_TABLE_IDS_USERS_user_password] == user_password)
        if(row[PG_TABLE_IDS_USERS_user_password] == user_password):
            return True, row[PG_TABLE_IDS_USERS_user_id]
    return False, None




def get_jwt_token(payload):
    return jwt.encode( payload, JWT_SECRET, algorithm='HS256')


def get_token(useremail, password):
    print("Entered Get Token")
    user_info = get_rows_by_col(PG_TABLE_IDS_USERS,opt_conds= " lower(" + pg_col_name_dict[PG_TABLE_IDS_USERS][2] + ") = '" + useremail.lower() + "' ")
    print_statement("user_info :: ",user_info)
    if len(user_info):
        row = user_info[0]
        print("row ::", row)
        print("compare :: ",row[PG_TABLE_IDS_USERS_user_password] == password)
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
                print_statement("User Logged In :: ",encoded, " :: user name :: ",user_name)
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


def process_possible_fix_response(issue_string):
    prompt_message_list = [
        {
            "role":GPT_SYS_ROLE,
            "content":VEHICLE_REPAIR_SYSTEM_GUIDELINES
        },
        {
            "role":GPT_USER_ROLE,
            "content":VEHICLE_REPAIR_SAMPLE_INPUT
        },
        {
            "role":GPT_ASST_ROLE,
            "content":VEHICLE_REPAIR_ASSISTANT
        },
        {
            "role":GPT_USER_ROLE,
            "content":issue_string
        }
    ]

    gpt_resp, input_tokens, output_tokens, gpttype = process_gpt_response(GPT_4_32K, prompt_message_list, JSON_OBJ)
    print_statement("gpt_resp :: ",gpt_resp," :: ",type(gpt_resp))
    return gpt_resp




def diagnose_and_get_possible_fixes(user_id, vehicle_make, vehicle_model, vehicle_type, gear_type, issues):
    if vehicle_type!= "electric":
        issue_string = f"""the make of the car is a {vehicle_make}, the model of the car is a {vehicle_model}, the type of the car is {vehicle_type}, the gear type of the car is {gear_type}, the issues with the car are {issues}"""
    else:
        issue_string = f"""the make of the car is a {vehicle_make}, the model of the car is a {vehicle_model}, the type of the car is {vehicle_type}, the issues with the car are {issues}"""

    print_statement("issue_string :: ",issue_string)
    repair_json = process_possible_fix_response(issue_string)
    possible_fix_list = ", ".join([fix["possible_fix"] for fix in repair_json["possible_fixes"]])    
    print_statement("possible_fix_list :: ",possible_fix_list)
    estimated_amount = sum([fix["possible_fix_cost"] for fix in repair_json["possible_fixes"]])
    print_statement("estimated_amount :: ",estimated_amount)
    status, vr_id = insert_vehicle_repair_info(user_id, vehicle_make,vehicle_model, vehicle_type, gear_type, issues, possible_fix_list, estimated_amount)
    return status, vr_id, possible_fix_list, estimated_amount

def process_payment_invoice(user_id, vr_id, mobile_number, address, mode_of_payment, bank, bill_amount):
    status, pi_id = insert_payment_invoice(user_id, vr_id, mobile_number, address, mode_of_payment, bank, bill_amount)
    return status, pi_id


def get_payment_invoice_details(user_id, p_id):
    payment_invoice_dict = {}
    user_name = get_row_by_id(PG_TABLE_IDS_USERS, pg_col_name_dict[PG_TABLE_IDS_USERS][0], user_id)[0][PG_TABLE_IDS_USERS_user_name]
    payment_invoice = get_row_by_id(PG_TABLE_PAYMENT_INVOICE, pg_col_name_dict[PG_TABLE_PAYMENT_INVOICE][0], p_id)
    vr_row = get_row_by_id(PG_TABLE_VEHICLE_REPAIR_INFO, pg_col_name_dict[PG_TABLE_VEHICLE_REPAIR_INFO][0], payment_invoice[0][PG_TABLE_PAYMENT_INVOICE_pi_vr_id])[0]
    payment_invoice_dict = {
        'user_name':user_name,
        'vehicle_make':vr_row[PG_TABLE_VEHICLE_REPAIR_INFO_vr_vehicle_make],
        'vehicle_model':vr_row[PG_TABLE_VEHICLE_REPAIR_INFO_vr_vehicle_model],
        'vehicle_type':vr_row[PG_TABLE_VEHICLE_REPAIR_INFO_vr_vehicle_type],
        'issues':vr_row[PG_TABLE_VEHICLE_REPAIR_INFO_vr_vehicle_issues],
        'possible_fixes':vr_row[PG_TABLE_VEHICLE_REPAIR_INFO_vr_possible_fixes].split(","),
        'bill_amount':payment_invoice[0][PG_TABLE_PAYMENT_INVOICE_pi_bill_amount],
        'bank':payment_invoice[0][PG_TABLE_PAYMENT_INVOICE_pi_bank],
        'mode_of_payment':payment_invoice[0][PG_TABLE_PAYMENT_INVOICE_pi_mode_of_payment],
    }
    print_statement("payment_invoice_dict :: ",payment_invoice_dict)
    return payment_invoice_dict














