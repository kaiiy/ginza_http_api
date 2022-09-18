from fastapi.testclient import TestClient

from ..main import app

client = TestClient(app)

def test_post():
    response = client.post(
        "/",
        headers={"content-type": "application/json"},
        json={ "text": "銀座でランチをご一緒しましょう。"},
    )
    
    assert response.status_code == 200