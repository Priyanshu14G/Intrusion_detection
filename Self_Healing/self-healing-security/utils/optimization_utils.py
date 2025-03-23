from skopt import gp_minimize

# Optimize firewall parameters using Bayesian Optimization
def optimize_firewall_params():
    def objective(params):
        latency, security = params
        return -(security * 0.7 - latency * 0.3)

    res = gp_minimize(objective, [(10, 100), (0.1, 1.0)], n_calls=20, random_state=42)
    print(f"✅ Optimal Parameters: Latency={res.x[0]}, Security={res.x[1]}")
