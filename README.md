# Monitoring Dashboard 📊

ML model monitoring with drift detection, performance tracking, and alerting.

## Metrics Tracked

- **Data Drift**: PSI, KS-test, Jensen-Shannon divergence
- **Prediction Drift**: Distribution shifts, label changes
- **Performance**: Accuracy, latency, throughput over time
- **Alerts**: Configurable thresholds, Slack/email/webhook

## Quick Start

```python
from monitoring import ModelMonitor

monitor = ModelMonitor(model_name="classifier-v1")
monitor.log_prediction(input_data, prediction, ground_truth=actual)
report = monitor.generate_report()
```

## License

MIT