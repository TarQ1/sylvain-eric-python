import uvicorn

def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("sylvain_eric_python.main:app", host='0.0.0.0', port=80, reload=True)
