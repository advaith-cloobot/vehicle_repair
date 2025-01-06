
import psycopg2

from Monolithic.constants.config_constants import *

def init_pg_tables():
    #initializing postgresql database
    conn = psycopg2.connect(database=DB_NAME, user = DB_USER, password = DB_PASS, host = DB_HOST, port = DB_PORT)
    cur = conn.cursor()


    # cur.execute('''
    #     CREATE TABLE vehicle_repair_info (
    #                         vr_id SERIAL PRIMARY KEY,
    #                         vr_user_id INT,
    #                         vr_vehicle_make TEXT,
    #                         vr_vehicle_type TEXT,
    #                         vr_vehicle_gear_type TEXT,
    #                         vr_vehicle_issues TEXT,
    #                         vr_possible_fixes TEXT,
    #                         vr_estimated_cost INT,
    #                         status INT
    #                     );

    # ''')



    # cur.execute('''
    #    CREATE TABLE payment_invoice (
    #                                 pi_id SERIAL PRIMARY KEY,
    #                                 pi_user_id INT,
    #                                 pi_vr_id INT,
    #                                 pi_mobile_number BIGINT,
    #                                 pi_address TEXT,
    #                                 pi_mode_of_payment TEXT,
    #                                 pi_bank TEXT,
    #                                 pi_bill_amount INT,
    #                                 status INT
    #                             );


    # ''')


#####################################################################
    # conn.commit()
    # print("\n\nUserDetails Table created successfully\n\n")