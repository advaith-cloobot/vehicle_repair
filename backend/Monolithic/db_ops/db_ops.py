from Monolithic.constants.constants import *
from Components.PostgreDBtools.postgres_utils import get_row_by_id,get_rows_by_col,insert_new_row_return_id,update_row
from datetime import datetime



def insert_new_user(user_email,user_password,user_name):
    user_row = get_rows_by_col(PG_TABLE_IDS_USERS,pg_col_name_dict[PG_TABLE_IDS_USERS][3],user_email)
    if not user_row:
        rowDict = {
            pg_col_name_dict[PG_TABLE_IDS_USERS][1]:user_name,
            pg_col_name_dict[PG_TABLE_IDS_USERS][2]:user_email,
            pg_col_name_dict[PG_TABLE_IDS_USERS][3]:user_password,
            pg_col_name_dict[PG_TABLE_IDS_USERS][4]: datetime.utcnow(),
            pg_col_name_dict[PG_TABLE_IDS_USERS][5]: datetime.utcnow(),
            pg_col_name_dict[PG_TABLE_IDS_USERS][6]: 1
        }
        status,user_id = insert_new_row_return_id(PG_TABLE_IDS_USERS,rowDict,pg_col_name_dict[PG_TABLE_IDS_USERS][0])
        return status,user_id
    else:
        return False,None






def insert_vehicle_repair_info(user_id, vehicle_make, vehicle_type, gear_type, issues, possible_fixes, estimated_cost):
    rowDict = {
        pg_col_name_dict[PG_TABLE_VEHICLE_REPAIR_INFO][1]: user_id,
        pg_col_name_dict[PG_TABLE_VEHICLE_REPAIR_INFO][2]: vehicle_make,
        pg_col_name_dict[PG_TABLE_VEHICLE_REPAIR_INFO][3]: vehicle_type,
        pg_col_name_dict[PG_TABLE_VEHICLE_REPAIR_INFO][4]: gear_type,
        pg_col_name_dict[PG_TABLE_VEHICLE_REPAIR_INFO][5]: issues,
        pg_col_name_dict[PG_TABLE_VEHICLE_REPAIR_INFO][6]: possible_fixes,
        pg_col_name_dict[PG_TABLE_VEHICLE_REPAIR_INFO][7]: estimated_cost,
        pg_col_name_dict[PG_TABLE_VEHICLE_REPAIR_INFO][8]: 1  # status
    }
    status, vr_id = insert_new_row_return_id(
        PG_TABLE_VEHICLE_REPAIR_INFO,
        rowDict,
        pg_col_name_dict[PG_TABLE_VEHICLE_REPAIR_INFO][0]
    )
    return status, vr_id



def insert_payment_invoice(user_id, vr_id, mobile_number, address, mode_of_payment, bank, bill_amount):
    rowDict = {
        pg_col_name_dict[PG_TABLE_PAYMENT_INVOICE][1]: user_id,
        pg_col_name_dict[PG_TABLE_PAYMENT_INVOICE][2]: vr_id,
        pg_col_name_dict[PG_TABLE_PAYMENT_INVOICE][3]: mobile_number,
        pg_col_name_dict[PG_TABLE_PAYMENT_INVOICE][4]: address,
        pg_col_name_dict[PG_TABLE_PAYMENT_INVOICE][5]: mode_of_payment,
        pg_col_name_dict[PG_TABLE_PAYMENT_INVOICE][6]: bank,
        pg_col_name_dict[PG_TABLE_PAYMENT_INVOICE][7]: bill_amount,
        pg_col_name_dict[PG_TABLE_PAYMENT_INVOICE][8]: user_id,
        pg_col_name_dict[PG_TABLE_PAYMENT_INVOICE][9]: datetime.utcnow(),
        pg_col_name_dict[PG_TABLE_PAYMENT_INVOICE][10]: user_id,
        pg_col_name_dict[PG_TABLE_PAYMENT_INVOICE][11]: datetime.utcnow(),
        pg_col_name_dict[PG_TABLE_PAYMENT_INVOICE][12]: 1  # status
    }
    status, pi_id = insert_new_row_return_id(
        PG_TABLE_PAYMENT_INVOICE,
        rowDict,
        pg_col_name_dict[PG_TABLE_PAYMENT_INVOICE][0]
    )
    return status, pi_id
