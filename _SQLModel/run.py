import uvicorn
from multiprocessing import cpu_count, freeze_support
import main as m

# # https://medium.com/codex/how-to-create-a-fastapi-uvicorn-server-windows-service-af41f075dabf
def start_server(host="127.0.0.1",
                 port=5000,
                 num_workers=4,
                 loop="asyncio",
                 reload=False):
    uvicorn.run("main:app",
                host=host,
                port=port,
                workers=num_workers,
                loop=loop,
                reload=reload)


if __name__ == "__main__":
    try:
        m.create_db_and_tables()
    except:
        print("database already created")

    freeze_support()  # Needed for pyinstaller for multiprocessing on WindowsOS
    num_workers = int(cpu_count() * 0.75)
    start_server(num_workers=num_workers)