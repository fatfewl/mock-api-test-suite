import requests
import requests_mock


def post_to_endpoint(method, headers, payload):
    """Perform the api call
    :return the api response

    REALLY THIS SHOULD CALL THE API BUT WE WILL MOCK THIS TO RETURN THE CANNED EXPECTED DATA
    """
    uri = 'http://api.cushon.com' + payload['endpoint']
    with requests_mock.Mocker() as m:
        m.register_uri(method, uri, json=payload['expected-response'], status_code=payload['expected-status-code'])
        return requests.request(method, uri, headers=headers, data=payload)
