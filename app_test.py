"""Unit test for application."""
import os
from app import app


def test_hello_endpoint():
    """Test /api/hello endpoint returns correct format."""
    client = app.test_client()
    response = client.get('/api/hello')
    assert response.status_code == 200
    hostname = os.getenv('HOSTNAME', 'unknown')
    expected_message = f'Hello, KubeRocketCI from {hostname}'
    assert response.data.decode('utf-8') == expected_message
