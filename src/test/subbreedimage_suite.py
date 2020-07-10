"""
Suite for Sub breed image endpoint calls
"""
from expects import expect, contain, equal
from questions_three.scaffolds.check_script import check, check_suite
from questions_three.http_client import HttpClient

with check_suite('/breed/{breed}/images* - sub breed image endpoint calls'):

    #TODO replace code bellow
    response = HttpClient().get('https://dog.ceo/api/breeds/list/all')
    with check('response status is 200'):
        expect(response.status_code).to(equal(200))

    with check('response body contains pitbull'):
        expect(response.text).to(contain('pitbull'))
