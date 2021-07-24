import requests
import time
import winsound
pincode=input('Enter the Pincode:')
date=input('Enter the Date (DD-MM-YYYY):')
URL= 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={}&date={}'.format(pincode,date)


def findAvailability():
    counter = 0
    result = requests.get(URL)
    response_json = result.json()
    data = response_json["sessions"]
    for each in data:
        if((each["available_capacity"] > 0) & (each["min_age_limit"] >= 18)):
            counter += 1	
            print("**************************************************************")
            print("Name:",each["name"])
            print("PinCode:",each["pincode"])
            print("Vaccine:",each["vaccine"])
            print("Dose1 Available:",each["available_capacity_dose1"])
            print("Dose2 Available:",each["available_capacity_dose2"])
            print("Total Dose Available:",each["available_capacity"])
            winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
            return False
    if(counter == 0):
        print("No Slots are Available")
        return False


while(findAvailability() != True):
    time.sleep(5)
    findAvailability()