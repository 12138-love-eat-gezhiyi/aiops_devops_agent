import psutil
import requests
import yaml

class MonitorAgent:
    def __init__(self):
        cfg = yaml.safe_load(open("config.yaml"))
        self.url = cfg["url"]
        self.cpu_th = cfg["cpu_threshold"]
        self.mem_th = cfg["memory_threshold"]

    def collect(self):
        return {
            "cpu": psutil.cpu_percent(),
            "memory": psutil.virtual_memory().percent,
            "http": self._http()
        }

    def _http(self):
        try:
            return requests.get(self.url, timeout=2).status_code
        except:
            return 500

    def is_anomaly(self, m):
        return m["cpu"] > self.cpu_th or m["memory"] > self.mem_th or m["http"] != 200