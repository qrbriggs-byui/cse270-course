import requests
import pytest

@pytest.fixture
def api_url():
    return "http://127.0.0.1:8000/data/all"

def test_response_status_and_json(api_url):
    response = requests.get(api_url)
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    
    try:
        json_data = response.json()
        assert 'businesses' in json_data, "JSON response does not contain 'businesses' member"
        businesses = json_data['businesses']
        assert len(businesses) > 0, "No businesses found in JSON response"
        first_business = businesses[0]
        assert 'name' in first_business, "First business object does not contain 'name' member"
        assert first_business['name'] == "Teton Elementary", "Name of the first business is not 'Teton Elementary'"
    except ValueError:
        pytest.fail("Response is not valid JSON")
