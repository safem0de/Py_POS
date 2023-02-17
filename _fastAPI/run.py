# import uvicorn

# if __name__ == "__main__":
#     uvicorn.run("_fastAPI.main:app", port=5000, log_level="info")

# from _fastAPI.main import app
# import asyncio
# import uvloop
# from hypercorn.asyncio import serve
# from hypercorn.config import Config

# if __name__ == "__main__":

#     config = Config()
#     config.bind = ["0.0.0.0:8000"]

#     asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
#     loop = asyncio.new_event_loop()
#     asyncio.set_event_loop(loop)

#     loop.run_until_complete(serve(app, config))

import uvicorn
from multiprocessing import cpu_count, freeze_support


def start_server(host="127.0.0.1",
                 port=5000,
                 num_workers=4,
                 loop="asyncio",
                 reload=False):
    uvicorn.run("_fastAPI.main:app",
                host=host,
                port=port,
                workers=num_workers,
                loop=loop,
                reload=reload)


if __name__ == "__main__":
    freeze_support()  # Needed for pyinstaller for multiprocessing on WindowsOS
    num_workers = int(cpu_count() * 0.75)
    start_server(num_workers=num_workers)