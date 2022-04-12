from typing import Dict

from fastapi import FastAPI

description = """
My Hello World API
This is the best documentation
"""

app = FastAPI(title="Sylvain-Eric-Python", description=description, version="22-04-11")


@app.get("/")
def home() -> Dict:
    return {"hello": "world"}
