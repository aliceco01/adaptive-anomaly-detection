from src.generate_data import generate_synthetic_telemetry
import matplotlib.pyplot as plt

df = generate_synthetic_telemetry()

df.plot(subplots=True, figsize=(12, 6), title=["CPU", "Errors", "Latency"])
plt.tight_layout()
plt.show()
