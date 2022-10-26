import requests
from .models import Repeater, DuplexFrequencyPair


def fetch_json(url=None):
    url = "https://m17.club/.well_known/repeaters.json"

    response = requests.get(url)
    return response.json()

def validate_and_save(task):
    

    result = task.result
    

    print(result["repeaters"])
    owner = result["owner"]
    check_keys = ["name", "freq_in", "freq_out", "access_information", "lat", "lon", "antenna_alt_above_terrain"]
    if result:
        for repeater in result["repeaters"]:
            #check if all keys exist
            for key in check_keys:
                if key not in repeater.keys():
                    print(f"{key} is missing")
                    return

            if not repeater["name"]:
                print(f"Name is null")
                return 

            if float(repeater["lat"]) == 0 or float(repeater["lon"]) == 0:
                print("Invalid lat or lon")
                return

            alt = repeater["antenna_alt_above_terrain"].split("m")[0]
            try:
                freq_pair = DuplexFrequencyPair(in_freq=repeater["freq_in"], out_freq=repeater["freq_out"])
                freq_pair.save()
                new_rep = Repeater(callsign=repeater["name"], lat=repeater["lat"], lon=repeater["lon"], alt=alt, access_information=repeater["access_information"])
                new_rep.save()
                new_rep.freq.add(freq_pair)
                

            except Exception as e:
                print(str(e))
                
            print("saved in DB")
            

        


