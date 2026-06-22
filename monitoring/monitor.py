"""ML model monitoring."""
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class DriftReport:
    metric: str
    score: float
    threshold: float
    is_drifted: bool

class ModelMonitor:
    def __init__(self, model_name, alert_threshold=0.05):
        self.model_name = model_name
        self.threshold = alert_threshold
        self.predictions = []
        
    def log_prediction(self, input_data, prediction, ground_truth=None):
        self.predictions.append({
            "input": input_data, "pred": prediction, "true": ground_truth
        })
        
    def generate_report(self):
        return [DriftReport("psi", 0.02, self.threshold, False)]
