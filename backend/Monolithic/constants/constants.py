JWT_SECRET = 'BDa8yfPp29X918cA2e7w'

JWT_EXP_DELTA_SECONDS = 86400 * 30



GPT_35_16K = 0
OPENAI_ENGINE_NAME_GPT3_5_16K = "Cloobot-ChatGPT3-16k"
OPENAI_ENGINE_NAME_GPT3_5_16K_V2 = "Cloobot-ChatGPT35-16k-SwitzNorth"
OPENAI_ENGINE_NAME_GPT3_5_16K_V3 = "Cloobot-ChatGPT35-16k-SwitzNorth"

GPT_4_32K = 1
OPENAI_ENGINE_NAME_GPT4_32K = "Cloobot-32K-GPT4"
OPENAI_ENGINE_NAME_GPT4_32K_V2 = "Cloobot-ChatGPT4-32k-SwitzNorth"
OPENAI_ENGINE_NAME_GPT4_32K_V3 = "Cloobot-ChatGPT4-32k-CanadaEast"

GPT_VECT_EMBED = 2
OPENAI_ENGINE_NAME_GPT_VECT_EMBED = "Cloobot-ChatGPT4-VectEmbed-32k-EastUS"

GPT_4o_50k = 3
OPENAI_ENGINE_NAME_GPT4o_50k = "GPT4o"

GPT_4O_12K = 4
OPENAI_ENGINE_NAME_GPT4O_12K = "brd_image_indexing"


OpenAI_Res_Depl_ID_Map = {}
OpenAI_Res_Depl_ID_Map[OPENAI_ENGINE_NAME_GPT_VECT_EMBED] = "vector_embedding_test_1"


per_gpt_token_cost = {}
per_gpt_token_cost[OPENAI_ENGINE_NAME_GPT3_5_16K] = {}
per_gpt_token_cost[OPENAI_ENGINE_NAME_GPT3_5_16K][0] = 0.025    #input
per_gpt_token_cost[OPENAI_ENGINE_NAME_GPT3_5_16K][1] = 0.04     #output

per_gpt_token_cost[OPENAI_ENGINE_NAME_GPT4_32K] = {}
per_gpt_token_cost[OPENAI_ENGINE_NAME_GPT4_32K][0] = 0.5
per_gpt_token_cost[OPENAI_ENGINE_NAME_GPT4_32K][1] = 1

per_gpt_token_cost[OPENAI_ENGINE_NAME_GPT3_5_16K_V2] = {}
per_gpt_token_cost[OPENAI_ENGINE_NAME_GPT3_5_16K_V2][0] = 0.025    #input
per_gpt_token_cost[OPENAI_ENGINE_NAME_GPT3_5_16K_V2][1] = 0.04     #output

per_gpt_token_cost[OPENAI_ENGINE_NAME_GPT4_32K_V2] = {}
per_gpt_token_cost[OPENAI_ENGINE_NAME_GPT4_32K_V2][0] = 0.5
per_gpt_token_cost[OPENAI_ENGINE_NAME_GPT4_32K_V2][1] = 1

per_gpt_token_cost[OPENAI_ENGINE_NAME_GPT3_5_16K_V3] = {}
per_gpt_token_cost[OPENAI_ENGINE_NAME_GPT3_5_16K_V3][0] = 0.025    #input
per_gpt_token_cost[OPENAI_ENGINE_NAME_GPT3_5_16K_V3][1] = 0.04     #output

per_gpt_token_cost[OPENAI_ENGINE_NAME_GPT4_32K_V3] = {}
per_gpt_token_cost[OPENAI_ENGINE_NAME_GPT4_32K_V3][0] = 0.5
per_gpt_token_cost[OPENAI_ENGINE_NAME_GPT4_32K_V3][1] = 1

per_gpt_token_cost[OPENAI_ENGINE_NAME_GPT_VECT_EMBED] = {}
per_gpt_token_cost[OPENAI_ENGINE_NAME_GPT_VECT_EMBED][0] = 0.5
per_gpt_token_cost[OPENAI_ENGINE_NAME_GPT_VECT_EMBED][1] = 1

per_gpt_token_cost[OPENAI_ENGINE_NAME_GPT4o_50k] = {}
per_gpt_token_cost[OPENAI_ENGINE_NAME_GPT4o_50k][0] = 0.5
per_gpt_token_cost[OPENAI_ENGINE_NAME_GPT4o_50k][1] = 1

per_gpt_token_cost[OPENAI_ENGINE_NAME_GPT4O_12K] = {}
per_gpt_token_cost[OPENAI_ENGINE_NAME_GPT4O_12K][0] = 0.5
per_gpt_token_cost[OPENAI_ENGINE_NAME_GPT4O_12K][1] = 1


JSON_OBJ = 0
JSON_LIST = 1
JSON_NONE = 2





pg_col_name_dict = {}
PG_TABLE_IDS_USERS = "users"

# Constants for "users" table
pg_col_name_dict[PG_TABLE_IDS_USERS] = {}
pg_col_name_dict[PG_TABLE_IDS_USERS][0] = 'user_id'
pg_col_name_dict[PG_TABLE_IDS_USERS][1] = 'user_name'
pg_col_name_dict[PG_TABLE_IDS_USERS][3] = 'user_password'
pg_col_name_dict[PG_TABLE_IDS_USERS][2] = 'user_email'
pg_col_name_dict[PG_TABLE_IDS_USERS][4] = 'created_timestamp'
pg_col_name_dict[PG_TABLE_IDS_USERS][5] = 'last_updated_timestamp'
pg_col_name_dict[PG_TABLE_IDS_USERS][6] = 'status'

PG_TABLE_IDS_USERS_user_id                  = 0
PG_TABLE_IDS_USERS_user_name                = 1
PG_TABLE_IDS_USERS_user_password            = 3
PG_TABLE_IDS_USERS_user_email               = 2
PG_TABLE_IDS_USERS_created_timestamp        = 4
PG_TABLE_IDS_USERS_last_updated_timestamp   = 5
PG_TABLE_IDS_USERS_status                   = 6




PG_TABLE_VEHICLE_REPAIR_INFO = "vehicle_repair_info"

# Constants for "vehicle_repair_info" table
pg_col_name_dict[PG_TABLE_VEHICLE_REPAIR_INFO] = {}
pg_col_name_dict[PG_TABLE_VEHICLE_REPAIR_INFO][0] = 'vr_id'
pg_col_name_dict[PG_TABLE_VEHICLE_REPAIR_INFO][1] = 'vr_user_id'
pg_col_name_dict[PG_TABLE_VEHICLE_REPAIR_INFO][2] = 'vr_vehicle_make'
pg_col_name_dict[PG_TABLE_VEHICLE_REPAIR_INFO][3] = 'vr_vehicle_type'
pg_col_name_dict[PG_TABLE_VEHICLE_REPAIR_INFO][4] = 'vr_vehicle_gear_type'
pg_col_name_dict[PG_TABLE_VEHICLE_REPAIR_INFO][5] = 'vr_vehicle_issues'
pg_col_name_dict[PG_TABLE_VEHICLE_REPAIR_INFO][6] = 'vr_possible_fixes'
pg_col_name_dict[PG_TABLE_VEHICLE_REPAIR_INFO][7] = 'vr_estimated_cost'
pg_col_name_dict[PG_TABLE_VEHICLE_REPAIR_INFO][8] = 'status'

PG_TABLE_VEHICLE_REPAIR_INFO_vr_id               = 0
PG_TABLE_VEHICLE_REPAIR_INFO_vr_user_id          = 1
PG_TABLE_VEHICLE_REPAIR_INFO_vr_vehicle_make     = 2
PG_TABLE_VEHICLE_REPAIR_INFO_vr_vehicle_type     = 3
PG_TABLE_VEHICLE_REPAIR_INFO_vr_vehicle_gear_type = 4
PG_TABLE_VEHICLE_REPAIR_INFO_vr_vehicle_issues   = 5
PG_TABLE_VEHICLE_REPAIR_INFO_vr_possible_fixes   = 6
PG_TABLE_VEHICLE_REPAIR_INFO_vr_estimated_cost   = 7
PG_TABLE_VEHICLE_REPAIR_INFO_status              = 8




PG_TABLE_PAYMENT_INVOICE = "payment_invoice"

# Constants for "payment_invoice" table
pg_col_name_dict[PG_TABLE_PAYMENT_INVOICE] = {}
pg_col_name_dict[PG_TABLE_PAYMENT_INVOICE][0] = 'pi_id'
pg_col_name_dict[PG_TABLE_PAYMENT_INVOICE][1] = 'pi_user_id'
pg_col_name_dict[PG_TABLE_PAYMENT_INVOICE][2] = 'pi_vr_id'
pg_col_name_dict[PG_TABLE_PAYMENT_INVOICE][3] = 'pi_mobile_number'
pg_col_name_dict[PG_TABLE_PAYMENT_INVOICE][4] = 'pi_address'
pg_col_name_dict[PG_TABLE_PAYMENT_INVOICE][5] = 'pi_mode_of_payment'
pg_col_name_dict[PG_TABLE_PAYMENT_INVOICE][6] = 'pi_bank'
pg_col_name_dict[PG_TABLE_PAYMENT_INVOICE][7] = 'pi_bill_amount'
pg_col_name_dict[PG_TABLE_PAYMENT_INVOICE][8] = 'pi_created_user_id'
pg_col_name_dict[PG_TABLE_PAYMENT_INVOICE][9] = 'pi_created_timestamp'
pg_col_name_dict[PG_TABLE_PAYMENT_INVOICE][10] = 'pi_last_updated_user_id'
pg_col_name_dict[PG_TABLE_PAYMENT_INVOICE][11] = 'pi_last_updated_timestamp'
pg_col_name_dict[PG_TABLE_PAYMENT_INVOICE][12] = 'status'

PG_TABLE_PAYMENT_INVOICE_pi_id                    = 0
PG_TABLE_PAYMENT_INVOICE_pi_user_id               = 1
PG_TABLE_PAYMENT_INVOICE_pi_vr_id                 = 2
PG_TABLE_PAYMENT_INVOICE_pi_mobile_number         = 3
PG_TABLE_PAYMENT_INVOICE_pi_address               = 4
PG_TABLE_PAYMENT_INVOICE_pi_mode_of_payment       = 5
PG_TABLE_PAYMENT_INVOICE_pi_bank                  = 6
PG_TABLE_PAYMENT_INVOICE_pi_bill_amount           = 7
PG_TABLE_PAYMENT_INVOICE_pi_created_user_id       = 8
PG_TABLE_PAYMENT_INVOICE_pi_created_timestamp     = 9
PG_TABLE_PAYMENT_INVOICE_pi_last_updated_user_id  = 10
PG_TABLE_PAYMENT_INVOICE_pi_last_updated_timestamp = 11
PG_TABLE_PAYMENT_INVOICE_status                   = 12
