class DiagnoseAgent:

    def analyze(self, metrics, logs):
        if metrics["http"] != 200:
            return {"type": "SERVICE_DOWN", "reason": logs[:200]}
        if metrics["cpu"] > 80:
            return {"type": "HIGH_CPU", "reason": "CPU spike"}
        if metrics["memory"] > 80:
            return {"type": "HIGH_MEMORY", "reason": "Memory spike"}
        return {"type": "UNKNOWN", "reason": logs[:200]}