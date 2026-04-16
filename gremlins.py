import docker
import random
import time

client = docker.from_dev()

def kill_container(client):
	containers = client.containers.list()
	target = random.choice(containers)
	target.stop()

def cpu_spike(client):
	containers = client.containers.list()
	target = random.choice(containers)
	target.exec_run("stress --cpu 1 --timeout 30")

def memory_spike(client):
 	containers = client.containers.list()
	target = random.choice(containers)
	target.exec_run("stress --vm 1 --vm-bytes 256M --timeout 30")

actions = {
	"kill_container": kill_container,
	"cpu_spike": cpu_spike,
	"memory_spike": memory_spike,
}

while True:
	chosen = random.choice(list(actions.keys()))
	print(f"Injecting chaos: {chosen}")
	actions[chosen](client)
	time.sleep(30)

