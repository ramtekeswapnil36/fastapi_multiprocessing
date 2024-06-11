# fastapi_multiprocessing

This project implements a FastAPI application to perform addition on lists of integers using Python's multiprocessing pool. It follows the MVC (Model-View-Controller) pattern and includes request and response validation using Pydantic models, error handling, logging, and unit tests.

mkdir fastapi_multiprocessing
cd fastapi_multiprocessing

python -m venv venv
source venv/bin/activate


pip install fastapi uvicorn pydantic gunicorn pytest

pip install -r requirements.txt


uvicorn app.main:app --reload

#Features
FastAPI for building the web API.
Pydantic for data validation.
Multiprocessing for parallel computation.
Logging for debugging and monitoring.
Comprehensive unit tests.

Installation
fastapi 
uvicorn
pydantic
gunicorn
pytest



Prerequisites
Python 3.8+
Virtual environment (recommended)
