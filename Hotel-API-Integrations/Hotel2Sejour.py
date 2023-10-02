import re
import uuid
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


def H2S_Requester(method, cookie, params) -> list[dict]:
    
    headers = {
        "cookie": cookie
    }
    
    response = requests.get(
                url=f"https://admin.hotel2sejour.com/api/pax/{method}", 
                headers=headers,
                params=params
            )
    print(response.content)
    return Parse_XML(method, response.text)
    


def Parse_XML(method, response_text) -> list[dict]:
    
    element = ""
    results = []
    # escape_illegal_xml_characters = lambda x: re.sub(u'[\x00-\x08\x0b\x0c\x0e-\x1F\uD800-\uDFFF\uFFFE\uFFFF]', '', x)

    
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
    elif method == "getreservationlist":
        element = "FileCode"
        found_elements = root.findall(f".//{element}")
        for code in found_elements:
            results.append(code) # HACK needs to be checked
    # elif method == "checkreservationfile":
    #     element = "InfoMessage"
    #     info_message_element = root.findall(f".//{element}")
    #     if info_message_element is not None:
    #         info_message = info_message_element.text
    #         results.append(info_message)
    #     else:
    #         return None
    return results

def main():
    """methods:
    >>> gethotelagencies
    >>> getnotconfirmmessages
    >>> getsejourformapping
    >>> getreservationlist
    >>> checkreservationfile TODO <-- Broken request
    >>> sendconfirmation TODO <-- Broken request
    >>> pushreservationsforthirdparty
    """
    
    cookie = H2S_Login()
    
    
    
    # agencies = H2S_Requester("gethotelagencies", cookie, 
    #                          {'format': "xml"})
    # print(agencies)
    # print()
    
    # notconfirmmsgs = H2S_Requester("getnotconfirmmessages", cookie, 
    #                                {'format': "xml", 'paximumId': PAXIMUM_ID, 'langId': "tr-TR"})
    # print(notconfirmmsgs)
    # print()
    
    # sejourcodes_list = []
    # for agency in agencies:
    #     sejourcodes_list.append(H2S_Requester("getsejourformapping", cookie, 
    #                                           {'format': "xml", 'paximumId': PAXIMUM_ID, 'agencyId': agency['Id']}))
    # print(sejourcodes_list)
    # print()
    
    # checkin_date = datetime(2023, 9, 10)
    # checkout_date = datetime(2023, 9, 26)
    # f_checkin_date = checkin_date.strftime("%m.%d.%Y")
    # f_checkout_date = checkout_date.strftime("%m.%d.%Y")
    # reservation_code = H2S_Requester("getreservationlist", cookie, {'format': "xml",
    #                                                                 'paximumId': PAXIMUM_ID,
    #                                                                 # 'agencyId': None,
    #                                                                 'isSendRequired': False,
    #                                                                 'checkInStart': f_checkin_date,
    #                                                                 'checkInEnd': f_checkout_date,
    #                                                                 'status': "",
    #                                                                 })
    # print(reservation_code)
    # print()
    # reservationlist_ready = H2S_Requester("checkreservationfile", cookie, {'format': "xml",
    #                                                                        'fileCode': str(uuid.uuid4())
    #                                                                        })
    
    # print(reservationlist_ready)
    # print()
    
    # # sendconfirmation = H2S_Requester("sendconfirmation", cookie, {'format': "xml",
    # #                                                               'agencyId': 'f6fca414-7469-40fb-8f44-3ddde9c5cc9e',
    # #                                                               'paximumId': PAXIMUM_ID,
    # #                                                               'confirmationNote': "testnote",
    # #                                                               'confirmationStatus': "H",
    # #                                                               'notconfirmationNote': "",
    # #                                                               'pmsUser': "testUser",})
    
    
main()