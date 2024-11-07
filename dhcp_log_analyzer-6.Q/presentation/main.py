# presentation/main.py
import time
from data_access.ssh_connection import connect_ssh
from data_access.file_writer import save_data
from business_logic.dhcp_parser import parse_data
import config

def main():
    stdout = connect_ssh(config.HOST, config.USERNAME, config.PASSWORD, config.COMMAND)
    start_time = time.time()

    while time.time() - start_time < 300:  # 300 saniye boyunca çalış
        line = stdout.readline()
        if "OPTION: 53 (1) DHCP message type 3 (DHCPREQUEST)" in line:
            client_id, request_ip, vendor_id, host_name = parse_data(line)
            save_data(client_id, request_ip, vendor_id, host_name)
        if not line:
            break

    print("Dinleme tamamlandı ve veri kaydedildi.")

if __name__ == "__main__":
    main()
