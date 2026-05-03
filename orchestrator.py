from agents.monitor_agent import MonitorAgent
from agents.diagnose_agent import DiagnoseAgent
from agents.action_agent import ActionAgent
from agents.notify_agent import NotifyAgent
from agents.log_agent import LogAgent
from utils.logger import log

class Orchestrator:
    def __init__(self):
        self.monitor = MonitorAgent()
        self.diagnose = DiagnoseAgent()
        self.action = ActionAgent()
        self.notify = NotifyAgent()
        self.log_agent = LogAgent()

    def run(self):
        log("🚀 AIOps Agent Started")

        metrics = self.monitor.collect()

        if self.monitor.is_anomaly(metrics):
            log("⚠️ Anomaly detected")

            logs = self.log_agent.fetch_logs()
            diagnosis = self.diagnose.analyze(metrics, logs)

            result = self.action.execute(diagnosis)

            self.notify.send(metrics, diagnosis, result)

        else:
            log("✅ System healthy")