import os
import sys

from fastapi import FastAPI
import uvicorn


path = os.path.dirname(os.path.abspath(__file__))  # NOQA
sys.path.append(path)  # NOQA

# Configuration
from config import Config

# Initialize App
app = FastAPI()
app.config = Config().dict()

from controller.classify_text import *
# For run debugger
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=False)
