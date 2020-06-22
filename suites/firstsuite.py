import lemoncheesecake.api as lcc
import requests
import json
from lemoncheesecake.matching import check_that, equal_to, is_


@lcc.suite("my_suite")
@lcc.tags("samples", "tutorials")
class firstsuite:
    @lcc.test("test1")
    def test1(self):
        check_that("value", 4, equal_to(4.0))

    @lcc.test("test2")
    #@lcc.disabled()
    def test2(self):
        pass

    @lcc.test("test3")
    @lcc.tags("example")
    def test3(self):
        r = requests.get('http://dummy.restapiexample.com/api/v1/employees')
        check_that("http code", r.status_code, is_(200))
        resp = r.json()
        lcc.log_info("Response\n%s" % json.dumps(resp, indent=4))