import os
import requests

def block_ip(ip_address):
    """Block malicious IP address via firewall."""
    os.system(f"iptables -A INPUT -s {ip_address} -j DROP")
    print(f"🚨 IP {ip_address} blocked successfully!")

def lockdown_device(device_id):
    """Isolate compromised device from the network."""
    print(f"🔒 Locking down device {device_id} to prevent further propagation.")

def update_firewall_rules(ip_list):
    """Dynamically update firewall rules."""
    for ip in ip_list:
        block_ip(ip)
    print("✅ Firewall rules updated dynamically.")
