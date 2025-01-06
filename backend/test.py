
# repair_json = {{
#   "possible_fixes": [
#     {{
#       "possible_fix": "Inspect and clean the throttle body to remove carbon deposits.",
#       "possible_fix_cost": 1500
#     }},
#     {{
#       "possible_fix": "Inspect and lubricate or replace the throttle cable if it is frayed or dirty.",
#       "possible_fix_cost": 2500
#     }},
#     {{
#       "possible_fix": "Check and clean the accelerator pedal assembly, replacing bushings if necessary.",
#       "possible_fix_cost": 2000
#     }},
#     {{
#       "possible_fix": "Diagnose the electronic throttle system and replace the throttle position sensor (TPS) if needed.",
#       "possible_fix_cost": 4000
#     }},
#     {{
#       "possible_fix": "Perform a general inspection at a trusted service center to rule out other issues.",
#       "possible_fix_cost": 1000
#     }}
#   ]
# }}


# estimated_amount  = sum([fix["possible_fix_cost"] for fix in repair_json["possible_fixes"]])


# print(estimated_amount)


# {{
#   "possible_fixes": [
#     {{
#       "possible_fix": "<Description of the suggested fix>",
#       "possible_fix_cost": <Estimated cost of the fix in numerical value, e.g., 1500>
#     }},
#     {{
#       "possible_fix": "<Description of another suggested fix>",
#       "possible_fix_cost": <Estimated cost of this fix>
#     }}
#   ]
# }}


from Monolithic.utils.utils import process_possible_fix_response

issue_string = "the make of the car is a TATA, the model of the car is a i20, the type of the car is of an internal combustion engine, the gear type of the car is automatic, the issues with the car are the brake lights are not working properly as they are flcikering on and off when used"

print(process_possible_fix_response(issue_string))
