import docker
from docker.errors import APIError

client = docker.from_env()

try:
    container = client.containers.run(
        "mcr.microsoft.com/mssql/server:2022-latest",
        name="sqlserver",
        environment={
            "ACCEPT_EULA": "Y",
            "SA_PASSWORD": "YourStrong!Passw0rd",
        },
        ports={
            "1433/tcp": 1433,
        },
        detach=True,
    )
    print(container.id)
# except Exception as e:
#     print(e.__doc__)
#     print(dir(e))
#     for k in dir(e):
#         print(f"{k} = {getattr(e, k)}")

except APIError as e:
    if e.response.status_code == 409:
        print("Container already exists")
    else:
        raise
