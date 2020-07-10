"""
Suite for Breeds list endpoint calls
"""
import json
from expects import expect, equal
from questions_three.scaffolds.check_script import check, check_suite
from questions_three.http_client import HttpClient

with check_suite('/breeds/*/list* - lists endpoint calls'):

    response = HttpClient().get('https://dog.ceo/api/breeds/list/all')
    with check('response status is 200'):
        expect(response.status_code).to(equal(200))

    body = json.loads(response.text)

    with check('response body status is a success'):
        expect(body["status"]).to(equal('success'))

    with check('response body message to have 94 breeds'):
        expect(len(body["message"])).to(equal(94))

with check_suite('/breeds/list/all/random/* - lists 10 random breeds including sub breeds'):

    response = HttpClient().get('https://dog.ceo/api/breeds/list/all/random/10')
    with check('response status is 200'):
        expect(response.status_code).to(equal(200))

    body = json.loads(response.text)

    with check('response body status is a success'):
        expect(body["status"]).to(equal('success'))

    with check('response body message to have 10 breeds and sub breeds'):
        expect(len(body["message"])).to(equal(10))

with check_suite('/breeds/list/random/* - lists 10 random breeds'):

    response = HttpClient().get('https://dog.ceo/api/breeds/list/random/10')
    with check('response status is 200'):
        expect(response.status_code).to(equal(200))

    body = json.loads(response.text)

    with check('response body status is a success'):
        expect(body["status"]).to(equal('success'))

    with check('response body message to have 10 breeds'):
        expect(len(body["message"])).to(equal(10))

# TODO - add more checks