from src.generate_data import generate_synthetic_telemetry
from src.preprocess import normalize_data
from src.model import train_model, predict
import matplotlib.pyplot as plt

df = generate_synthetic_telemetry()
df_norm = normalize_data(df)

model = train_model(df_norm)
labels, scores = predict(model, df_norm)

plt.figure(figsize=(10,4))
plt.plot(scores, label="Anomaly Score")
plt.title("Isolation Forest Anomaly Score")
plt.legend()
plt.grid()
plt.show()
