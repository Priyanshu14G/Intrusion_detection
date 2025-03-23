import time

def measure_response_time(func):
    """Measure response time of security mechanisms."""
    start_time = time.time()
    func()
    end_time = time.time()
    return round(end_time - start_time, 2)

def evaluate_system_performance():
    """Evaluate system performance."""
    response_time = measure_response_time(simulate_iot_botnet_attack)
    print(f"⏱️ Response Time: {response_time} seconds")
    print("✅ System Performance Evaluation Complete!")
