import os

def rollback_firmware(device_id):
    """Rollback firmware to secure version."""
    print(f"🔄 Rolling back firmware for device {device_id} to last secure version.")
    os.system(f"ssh device_{device_id} 'rollback_firmware.sh'")

def restart_container(container_name):
    """Restart compromised container securely."""
    os.system(f"docker restart {container_name}")
    print(f"✅ Container {container_name} restored successfully.")
