# D:\priyanshu backup\CPP\Deep_Learning\Intrusion_detection\self-healing-security\main.py

# Import necessary modules
from ml_model.predict import classify_traffic
from api.incident_response import block_ip, update_firewall_rules
from api.recovery import rollback_firmware, restart_container
from api.rl_policy_update import train_rl_policy
from simulation.attack_simulation import simulate_iot_botnet_attack
from simulation.metrics import evaluate_system_performance

# Initial threat classification
# Ensure traffic_features contains exactly 44 features
traffic_features = [0.8, 0.2, 0.5, 0.7] + [0.0] * 40  # Padding to match 44 features
try:
    result = classify_traffic(traffic_features)
    print(f"🔍 Classification Result: {result}")
except ValueError as e:
    print(f"⚠️ Error: {e}")
    exit()

# Simulate attack and evaluate system performance
try:
    simulate_iot_botnet_attack()
    print("🚨 IoT Botnet Attack Simulation Complete.")
except Exception as e:
    print(f"❗️ Error in simulation: {e}")

# Evaluate system performance
try:
    evaluate_system_performance()
    print("📊 System Performance Evaluation Complete.")
except Exception as e:
    print(f"❗️ Error in performance evaluation: {e}")

# RL Policy Training and Update
try:
    train_rl_policy()
    print("🤖 RL Policy Training Completed.")
except Exception as e:
    print(f"❗️ Error in RL Policy Training: {e}")

# Rollback compromised devices and restart containers
try:
    rollback_firmware("device1")
    print("🔄 Firmware rollback successful for device1.")
except Exception as e:
    print(f"❗️ Error in firmware rollback: {e}")

try:
    restart_container("firewall_container")
    print("🔁 Container restart successful for firewall_container.")
except Exception as e:
    print(f"❗️ Error in restarting container: {e}")
