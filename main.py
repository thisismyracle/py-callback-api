""" The main file to run Callback API """

from fastapi import FastAPI
import uvicorn

from packages.queueing.threading import Threading
from routers import math_router


app = FastAPI(docs_url=None)
app.include_router(math_router.router)


if __name__ == '__main__':
    Threading.start_thread()
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=False)
    Threading.stop_thread()
