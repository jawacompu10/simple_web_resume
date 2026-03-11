import pytest
import subprocess
import time
import requests
import os

@pytest.fixture(scope="session")
def server():
    # Start the FastAPI server in the background
    process = subprocess.Popen(["uv", "run", "python", "main.py"], env=os.environ)
    
    # Wait for the server to be ready
    url = "http://localhost:8000"
    timeout = 10
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                break
        except requests.exceptions.ConnectionError:
            pass
        time.time()
        time.sleep(0.5)
    else:
        process.terminate()
        pytest.fail("Server failed to start")
        
    yield url
    
    # Terminate the server
    process.terminate()

@pytest.fixture(autouse=True)
def dismiss_storage_info(page, server):
    """Automatically dismiss the storage info modal for all tests."""
    page.goto(server)
    page.evaluate("localStorage.setItem('hasSeenStorageInfo', 'true')")
    page.reload()
