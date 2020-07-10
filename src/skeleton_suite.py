"""
simple skeleton attempt at using questions_three to make http check
"""
from expects import expect, contain, equal
from questions_three.scaffolds.check_script import check, check_suite
from questions_three.http_client import HttpClient

with check_suite('SkeletonSuite - list all breeds'):

    response = HttpClient().get('https://dog.ceo/api/breeds/list/all')
    with check('response status is 200'):
        expect(response.status_code).to(equal(200))

    with check('response body contains pitbull'):
        expect(response.text).to(contain('pitbull'))
