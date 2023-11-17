from fastapi.testclient import TestClient
import pytest
import requests
import requests_mock

from app.main import app


def gen_request_test(test_data, client, mock_requests):
    from_value = test_data['value_from'].lower()
    to_value = test_data['value_to'].lower()

    url_base = f"latest/currencies/{from_value}.min.json"
    url_req = f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/{url_base}"
    mock_requests.get(
        url_req,
        json={
            "date": "2023-11-16",
            from_value: {to_value: test_data['req_rate_value']},
        },
    )
    api_url = "/api/v1/conversion/request?value_from={}&value_to={}&amount={}".format(
        test_data['value_from'], test_data['value_to'], test_data['amount']
    )
    response = client.get(api_url)

    return response


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def mock_requests():
    with requests_mock.Mocker() as m:
        yield m


def test_conversion_endpoint_with_mocked_request_for_btc_to_usd_success(
    client, mock_requests
):
    test_data = {
        'amount': 10,
        'value_from': 'BTC',
        'value_to': 'USD',
        'req_rate_value': 50000,
    }

    response = gen_request_test(test_data, client, mock_requests)
    expected_response = {
        "requested_amount": test_data['amount'],
        "value_from": test_data['value_from'],
        "value_to": test_data['value_to'],
        "amount_converted": test_data['amount'] * test_data['req_rate_value']
    }

    assert response.status_code == 200
    assert response.json() == expected_response


def test_conversion_endpoint_with_mocked_request_for_usd_to_eur_success(
    client, mock_requests
):
    test_data = {
        'amount': 10,
        'value_from': 'USD',
        'value_to': 'EUR',
        'req_rate_value': 1131,
    }

    response = gen_request_test(test_data, client, mock_requests)
    expected_response = {
        "requested_amount": test_data['amount'],
        "value_from": test_data['value_from'],
        "value_to": test_data['value_to'],
        "amount_converted": test_data['amount'] * test_data['req_rate_value']
    }

    assert response.status_code == 200
    assert response.json() == expected_response


def test_conversion_endpoint_with_mocked_request_for_usd_to_eur_fail_connection(
    client, mock_requests
):
    # Mock the external API call
    test_data = {
        'amount': 10,
        'value_from': 'USD',
        'value_to': 'EUR',
        'req_rate_value': 1131,
    }

    from_value = test_data['value_from'].lower()

    url_base = f"latest/currencies/{from_value}.min.json"
    url_req = f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/{url_base}"
    mock_requests.get(
        url_req,
        json={},
    )
    mock_requests.side_effect = requests.exceptions.JSONDecodeError
    api_url = "/api/v1/conversion/request?value_from={}&value_to={}&amount={}".format(
        test_data['value_from'], test_data['value_to'], test_data['amount']
    )
    response = client.get(api_url)

    assert response.status_code == 502


def test_conversion_endpoint_with_mocked_request_for_usd_to_eur_fail_api(
    client, mock_requests
):
    # Mock the external API call
    test_data = {
        'amount': 10,
        'value_from': 'USD',
        'value_to': 'EUR',
        'req_rate_value': 1131,
    }

    from_value = test_data['value_from'].lower()

    url_base = f"latest/currencies/{from_value}.min.json"
    url_req = f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/{url_base}"
    mock_requests.get(
        url_req,
        json={},
        status_code=500
    )
    api_url = "/api/v1/conversion/request?value_from={}&value_to={}&amount={}".format(
        test_data['value_from'], test_data['value_to'], test_data['amount']
    )
    response = client.get(api_url)

    assert response.status_code == 502
