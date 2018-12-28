import pytest
import json
from tests.test_data import dat
from app import implementation, routes


@pytest.fixture(scope='function')
def client():
    red_flags = implementation.red_flags
    red_flags.clear()
    app = routes.app
    test_client = app.test_client()
    cxt = app.app_context()
    cxt.push()
    yield test_client
    cxt.pop()


# Encode test requests to json
def post_json(client, url, json_dict):
    return client.post(
        url, data=json.dumps(json_dict), content_type='application/json'
        )


# Decode json requests
def json_of_response(response):
    return json.loads(response.data.decode())


# Test red_flag creation and expected reponse; code and content
def test_red_flag_creation(client):
    response = post_json(client, 'api/v1/red_flags', dat['basic'])
    assert response.status_code == 201
    assert json_of_response(response)['data'][0]['message'] ==\
        'Created red flag'


def test_get_flags(client):
    post_json(client, '/api/v1/red_flags', dat['basic'])
    post_json(client, '/api/v1/red_flags', dat['basic'])
    post_json(client, '/api/v1/red_flags', dat['basic'])
    post_json(client, '/api/v1/red_flags', dat['basic'])
    response = client.get('/api/v1/red_flags')
    assert len(json_of_response(response)['data']) == 4
