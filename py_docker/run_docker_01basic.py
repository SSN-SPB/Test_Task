import docker


client = docker.from_env()

container = client.containers.run(
    "nginx",
    name="test-nginx",
    ports={"80/tcp": 8081},
    detach=True,
)

print(container.id)
print(container.name)