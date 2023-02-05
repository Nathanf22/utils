import sys, os
#print(os.getcwd())
sys.path.append(os.getcwd())
from  json_replace import JSONReplace, Replacement
import json
json_content = {
            "id": "0524",
            "vehicle": {
                "trip": {
                    "trip_id": "1021020",
                    "start_date": "20230203",
                    "schedule_relationship": "SCHEDULED",
                    "route_id": "35"
                },
                "position": {
                    "latitude": 38.81944,
                    "longitude": -77.14301,
                    "bearing": 5.229427,
                    "speed": 0.0
                },
                "timestamp": "1675472444",
                "vehicle": {
                    "id": "0524"
                },
                "current_stop_sequence": 15,
                "current_status": "STOPPED_AT",
                "stop_id": "624"
            }
        }
    
JSONreplace = JSONReplace(json_content)

JSONreplace.replace_key(Replacement.TO_UPPERCASE)
# JSONreplace.replace_key(Replacement.TO_LOWERCASE)
# JSONreplace.replace_key(Replacement.UPPERCASE_TO_UNDERSCORE)
JSONreplace.replace_key(Replacement.UPPERCASE_TO_UNDERSCORE_LOWERCASE)
# JSONreplace.replace_key(Replacement.LOWERCASE_TO_UNDERSCORE_UPPERCASE)
JSONreplace.replace_key(Replacement.LOWERCASE_TO_UNDERSCORE_LOWERCASE)
#JSONreplace.replace_key(Replacement.UPPERCASE_TO, '7')
JSONreplace.replace_key(Replacement.LOWERCASE_TO, '3')

json_content = json.dumps(json_content, indent=4)

print(json_content)