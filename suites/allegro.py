import json
import requests

import lemoncheesecake.api as lcc
from lemoncheesecake.matching import *

@lcc.suite("Allegro tests")
@lcc.tags("Allegro")
class allegro:
    @lcc.test("Get categories")
    def allegro_categories_test(self):
        lcc.set_step("Get Allegro categories information")
        lcc.log_info("GET https://api.allegro.pl.allegrosandbox.pl/sale/categories/{category_id}")
        resp = requests.get("https://api.allegro.pl.allegrosandbox.pl/sale/6061")
        require_that("HTTP code", resp.status_code, is_(404))
        resp_data = resp.json()
        lcc.log_info("Response\n%s" % json.dumps(resp_data, indent=4))

        lcc.set_step("Check API response")
     #   check_that_in(
     #       resp_data,
     #       "id", is_string(),
     #       "leaf", is_integer(),
     #       "name", is_not_none(),
     #       "options", is_(present()),
     #       "parent", match_pattern(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")
     #   )
    @lcc.test(" Get parameters supported by categories")
    def allegroParametersTest(self):
        lcc.set_step("Get Allegro categories parameters information")
        lcc.log_info("GET https://api.allegro.pl.allegrosandbox.pl/sale/categories/{category_id}/parameters")
        resp = requests.get("https://api.allegro.pl.allegrosandbox.pl/sale/categories/6061/parameters")
        require_that("HTTP code", resp.status_code, is_(200))
        resp_data = resp.json()
        lcc.log_info("Response\n%s" % json.dumps(resp_data, indent=4))

