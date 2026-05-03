import yaml

class LogAgent:
    def __init__(self):
        cfg = yaml.safe_load(open("config.yaml"))
        self.path = cfg["log_path"]

    def fetch_logs(self, n=50):
        try:
            with open(self.path) as f:
                return "".join(f.readlines()[-n:])
        except:
            return "NO LOGS"