"""
Suite for Breed endpoint calls
"""
from expects import expect, contain, equal
from questions_three.logging import logger_for_module
from questions_three.scaffolds.test_table import execute_test_table
from questions_three.http_client import HttpClient

log = logger_for_module(__name__)

TABLE = (
    ('test'),
    ('pitbull'),
    ('poodle'),
    ('husky'),
    ('doberman'),
    ('dalmatian'))

def test_breed(breed):
    response = HttpClient().get('https://dog.ceo/api/breed/' + b)
    with check('response status is 200'):
        expect(response.status_code).to(equal(200))
    log.info(response)


execute_test_table(
    suite_name='test', table=TABLE, func=test_breed)

# with check_suite('/breed/* - breed related endpoints'):


#     #TODO replace code bellow
#     response = HttpClient().get('https://dog.ceo/api/breeds/list/all')
#     with check('response status is 200'):
#         expect(response.status_code).to(equal(200))

#     with check('response body contains pitbull'):
#         expect(response.text).to(contain('pitbull'))
