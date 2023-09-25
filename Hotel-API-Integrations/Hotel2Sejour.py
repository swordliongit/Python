import requests
import json
import xml.etree.ElementTree as ET
from datetime import datetime


PAXIMUM_ID = 100826

def H2S_Login():
    user = "ARTIN_TP"
    passw = "RQUJFZAH"
    
    response = requests.get(
                url=f"https://admin.hotel2sejour.com/api/system/login?user={user}&pass={passw}"
            )
    cookie = json.loads(response.content)
    return cookie


def H2S_Requester(method, cookie, **kwargs) -> list[dict]:
    
    headers = {
        "cookie": cookie
    }
    
    params = None
    
    if method == "gethotelagencies":
        params = "format=xml"
    elif method == "getnotconfirmmessages":
        params = {'format': "xml", 'paximumId': PAXIMUM_ID, 'langId': "tr-TR"}
    elif method == "getsejourformapping":
        params = {'format': "xml", 'paximumId': PAXIMUM_ID, 'agencyId': kwargs['agencyId']}
    elif method == "getreservationlist":
        params = {'format': "xml", 'paximumId': PAXIMUM_ID, 'agencyId': kwargs['agencyId'], 'status': "", 'isSendRequired': False,
                  'checkInStart': kwargs['checkInStart'], 'checkInEnd': kwargs['checkInEnd']}
    response = requests.get(
                url=f"https://admin.hotel2sejour.com/api/pax/{method}", 
                headers=headers,
                params=params
            )
    
    return Parse_XML(method, response.text)
    


def Parse_XML(method, response_text) -> list[dict]:
    
    element = ""
    results = []
    
    # Parse the XML response
    root = ET.fromstring(response_text)
    if method == "gethotelagencies":
        element= "DefinitionHotelAgency"
        # Find all wanted elements
        found_elements = root.findall(f".//{element}")
        # Initialize an empty list to store the results
        for agency in found_elements:
            # Extract the Id and Name elements from each DefinitionHotelAgency element
            agency_id = agency.find("Id").text
            agency_name = agency.find("Name").text
            # Append the extracted data to the results list as a dictionary
            results.append({'Id': agency_id, 'Name': agency_name})
    elif method == "getnotconfirmmessages":
        element = "NotConfirmMessage"
        found_elements = root.findall(f".//{element}")
        for msg in found_elements:
            agency_id = msg.find("Id").text
            msg_text = msg.find("Name").text
            results.append({'Id': agency_id, 'Name': msg_text})
    elif method == "getsejourformapping":
        element = "SejourCodesForMapping"
        found_elements = root.findall(f".//{element}")
        for sejour_mapping in found_elements:
            # Create a dictionary to store the contents of SejourCodesForMapping
            sejour_mapping_data = {}
            # Extract and add the content of each child element to the dictionary
            for child_element in sejour_mapping:
                sejour_mapping_data[child_element.tag] = child_element.text
            # Append the dictionary to the results list
            results.append(sejour_mapping_data)
            
    return results

def main():
    """methods:
    >>> gethotelagencies
    >>> getnotconfirmmessages
    >>> getsejourformapping
    >>> getreservationlist
    """
    
    cookie = H2S_Login()
    
    agencies = H2S_Requester("gethotelagencies", cookie)
    print(agencies)
    print()
    notconfirmmsgs = H2S_Requester("getnotconfirmmessages", cookie)
    print(notconfirmmsgs)
    print()
    sejourcodes_list = []
    for agency in agencies:
        sejourcodes_list.append(H2S_Requester("getsejourformapping", cookie, {'agencyId': agency['Id']}))
    print(sejourcodes_list)
    print()
    reservation_list = H2S_Requester("getreservationlist", cookie, {'agencyId': agency['Id'], 'checkInStart': })
    
main()