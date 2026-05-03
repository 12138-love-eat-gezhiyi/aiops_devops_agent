import os
import yaml
from utils.logger import log

class ActionAgent:
    def __init__(self):
        self.cfg = yaml.safe_load(open("config.yaml"))

    def execute(self, diagnosis):
        mode = self.cfg.get("mode", "safe")

        if mode == "safe":
            log(f"[SAFE MODE] Would execute for {diagnosis}")
            return "DRY_RUN"

        t = diagnosis["type"]

        if t == "SERVICE_DOWN":
            os.system("systemctl restart myservice")
            return "RESTARTED"

        if t == "HIGH_CPU":
            os.system("pkill -f myservice")
            return "KILLED"

        if t == "HIGH_MEMORY":
            os.system("sync; echo 3 > /proc/sys/vm/drop_caches")
            return "CACHE_CLEARED"

        return "NO_ACTION"