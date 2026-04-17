import docker
import time

client = docker.from_env()

while True:
    containers = [c for c in client.containers.list(all=True) 
              if "grafana" not in c.name 
              and "prometheus" not in c.name]
    for container in containers:
        if container.status == "exited":
            print(f"Restarting {container.name}")
            container.restart()
    time.sleep(10)
