from utils.logger import log

class NotifyAgent:
    def send(self, metrics, diagnosis, result):
        msg = f"[ALERT] {metrics} | {diagnosis} -> {result}"
        log(msg)