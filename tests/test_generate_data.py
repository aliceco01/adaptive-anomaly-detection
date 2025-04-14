# tests/test_generate_data.py
from src.generate_data import generate_synthetic_telemetry

def test_data_shape():
    df = generate_synthetic_telemetry()
    assert df.shape[0] == 1000
    assert set(df.columns) == {"cpu", "errors", "latency"}
