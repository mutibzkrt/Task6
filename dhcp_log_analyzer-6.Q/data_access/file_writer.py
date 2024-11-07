# data_access/file_writer.py
def save_data(client_id, request_ip, vendor_id, host_name, file_path="parsed_data.txt"):
    with open(file_path, "a") as f:
        f.write(f"Client Identifier: {client_id}\n")
        f.write(f"Request IP Address: {request_ip}\n")
        f.write(f"Vendor Class Identifier: {vendor_id}\n")
        f.write(f"Host Name: {host_name}\n")
        f.write("-" * 40 + "\n")
