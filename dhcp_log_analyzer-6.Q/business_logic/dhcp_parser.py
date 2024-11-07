# business_logic/dhcp_parser.py
import re

def parse_data(data):
    client_id = request_ip = vendor_id = host_name = None

    if "OPTION: 61" in data:
        client_id_match = re.search(r"OPTION: 61 \(\d+\) Client-identifier (.+)", data)
        if client_id_match:
            client_id = client_id_match.group(1)
    
    if "OPTION: 50" in data:
        request_ip_match = re.search(r"OPTION: 50 \(\d+\) Request IP address (.+)", data)
        if request_ip_match:
            request_ip = request_ip_match.group(1)

    if "OPTION: 60" in data:
        vendor_id_match = re.search(r"OPTION: 60 \(\d+\) Vendor class identifier (.+)", data)
        if vendor_id_match:
            vendor_id = vendor_id_match.group(1)

    if "OPTION: 12" in data:
        host_name_match = re.search(r"OPTION: 12 \(\d+\) Host name (.+)", data)
        if host_name_match:
            host_name = host_name_match.group(1)
    
    return client_id, request_ip, vendor_id, host_name
