import datetime, os

os.makedirs("logs", exist_ok=True)

def log(msg):
    now = datetime.datetime.now()
    line = f"{now} {msg}"
    print(line)
    with open("logs/agent.log", "a") as f:
        f.write(line + "\n")