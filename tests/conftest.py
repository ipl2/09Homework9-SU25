# conftest.py
import pytest
from httpx import AsyncClient
from app.main import app  # Adjust import path as necessary
from dotenv import load_dotenv # chgange
import os # change here

load_dotenv() # change

assert os.getenv("ADMIN_USER") is not None, "ADMIN_USER env var not set"
assert os.getenv("ADMIN_PASSWORD") is not None, "ADMIN_PASSWORD env var not set" # sanity checks

@pytest.fixture
async def client():
    async with AsyncClient(app=app, base_url="http://testserver") as ac:
        yield ac

@pytest.fixture
async def get_access_token_for_test(client):
    form_data = {"username": os.getenv("ADMIN_USER", "admin"), "password": os.getenv("ADMIN_PASSWORD", "secret")} # change
    response = await client.post("/token", data=form_data)
    return response.json()["access_token"]
