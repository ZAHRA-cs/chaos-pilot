import docker
import time

client = docker.from_env()

while True:
    containers = client.containers.list(all=True)
    for container in containers:
        if container.status == "exited":
            print(f"Restarting {container.name}")
            container.restart()
    time.sleep(10)
