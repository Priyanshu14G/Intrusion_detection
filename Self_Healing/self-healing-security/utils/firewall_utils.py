# Firewall utilities for managing IP rules
def add_firewall_rule(ip_address, action="block"):
    if action == "block":
        print(f"🚫 Blocking IP: {ip_address}")
    else:
        print(f"✅ Allowing IP: {ip_address}")

def remove_firewall_rule(ip_address):
    print(f"🔓 Removing firewall rule for IP: {ip_address}")
