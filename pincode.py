import requests
import json

ENDPOINT = "https://api.postalpincode.in/pincode/"

pincode = input("Enter pincode :")

response = requests.get(ENDPOINT+pincode)

pincode_information = json.loads(response.text)

necessary_information = pincode_information[0]['PostOffice'][0]

for key,value in necessary_information.items():
    print(f"{key} : {value}")