import requests
import socket
import os
import subprocess


def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        return response.json().get('ip', 'IP not found')
    except requests.RequestException:
        return "Failed to retrieve IP"
def get_http_headers():
    response = requests.get('https://httpbin.org/headers')
    return response.json()['headers']

# For windows
def get_dns_cache():
    try:
        process = subprocess.Popen(['ipconfig', '/displaydns'], stdout=subprocess.PIPE)
        output, errors = process.communicate()
        return output.decode()
    except Exception as e:
        return str(e)

def get_open_connections():
    try:
        process = subprocess.Popen(['netstat', '-an'], stdout=subprocess.PIPE)
        output, errors = process.communicate()
        return output.decode()
    except Exception as e:
        return str(e)

# Main execution
public_ip = get_public_ip()
headers = get_http_headers()
dns_cache = get_dns_cache() 
connections = get_open_connections()

print(f"Public IP Address: {public_ip}")
print("HTTP Headers Exposed to Public Websites:")
for key, value in headers.items():
    print(f"{key}: {value}")

print("\nDNS Cache Entries (might require administrative privileges to view):")
print(dns_cache)

print("\nOpen Network Connections:")
print(connections)
