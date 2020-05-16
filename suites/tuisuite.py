import requests
from requests.auth import HTTPBasicAuth
import json

import lemoncheesecake.api as lcc
from lemoncheesecake.matching import check_that, is_

@lcc.suite("GLC test")

class tuisuite:
    @lcc.test("glc_auth_test")
    @lcc.tags("glc")
    def glc_auth_test(self, glc_url, glc_auth):
        r = requests.get(glc_url, headers=glc_auth)
#        if r.status_code == 200:
#            print("json \n" + json.dumps(r.json()))
#        else:
#            print("Failed: {} - {}".format(r.status_code, r.text))
        check_that('http code', r.status_code, is_(200))
        resp1 = r.json()
        print(resp1)
        lcc.log_info("Response\n%s" % json.dumps(resp1, indent=4))