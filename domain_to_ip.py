import socket
import concurrent.futures
import logging

# 设置日志记录
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
def get_ip_address(domain):
    try:
        ip = socket.gethostbyname(domain)
        logging.info(f"Successfully resolved: {domain} -> {ip}")
        return ip
    except socket.gaierror:
        logging.error(f"Failed to resolve: {domain}")
        return "Failed to resolve"

def read_domains_from_file(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file if line.strip()]

def main():
    domains_file = 'domains.txt'
    domains = read_domains_from_file(domains_file)
    ip_dict = {}

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_domain = {executor.submit(get_ip_address, domain): domain for domain in domains}
        for future in concurrent.futures.as_completed(future_to_domain):
            domain = future_to_domain[future]
            try:
                ip = future.result()
                if ip != "Failed to resolve":
                    ip_dict[domain] = ip
            except Exception as exc:
                logging.error(f"{domain} generated an exception: {exc}")

    with open('domain_ip_map.txt' and 'hosts', 'w') as file:
        for domain, ip in ip_dict.items():
            file.write(f"{ip}\t{domain}\n")

if __name__ == '__main__':
    main()