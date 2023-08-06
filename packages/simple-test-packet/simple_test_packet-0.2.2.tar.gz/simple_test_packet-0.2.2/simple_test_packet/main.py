from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root(name: Optional[str] = None):
    return {"Hello": name}
