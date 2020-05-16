import requests
from requests.auth import HTTPBasicAuth
import json
import lemoncheesecake.api as lcc
from lemoncheesecake.matching import check_that, is_



@lcc.suite("sec_suite")
@lcc.tags("validation", "white labels")
class secondsuite:
    @lcc.test("req1")
    def req1(self, authenticate):
        url = 'http://api.dev.compareking.no/api/application/111'
        lcc.log_url(url, "This is first shoot in this suite!!!")
        r = requests.get(url,
                         headers=authenticate)
        check_that('http code', r.status_code, is_(404))
        resp = r.json()
        lcc.log_info("Response\n%s" % json.dumps(resp, indent=4))

    @lcc.test("req2")
    def req2(self, endpoint, authenticate, throughput):
        r = requests.post(endpoint,
                          headers=authenticate, data=throughput)
        check_that('http code', r.status_code, is_(200))
        resp = r.json()
        lcc.log_info("Response\n%s" % json.dumps(resp, indent=4))

    @lcc.test("req3")
    def req3(self, endpoint, authenticate, throughput):
        r = requests.post(endpoint,
                          headers=authenticate, data=throughput)
        check_that('http code', r.status_code, is_(200))
        resp = r.json()
        lcc.log_info("Response\n%s" % json.dumps(resp, indent=4))

    @lcc.test("req4")
    def req4(self, endpoint, authenticate):
        payload = {
            'api_transaction_id': 'test_transaction',
            'desired_amount': '85000',
            'period': '1',
            'personal_id_number': '17119754402',
            'country_of_origin': 'no',
            'norwegian_citizen': '',
            'mobile_phone': '45028242',
            'email': 'nawaw@abc.abc',
            'marital_status': 'single',
            'marital_status_since': '',
            'children_num': '0',
            'housing': 'parents',
            'rent_expense': '0',
            'lived_on_home_address': '10',
            'education': 'university 4 years',
            'employment': 'public sector',
            'employer': 'test inc.',
            'employed_from': '01.2004',
            'work_position': 'boss',
            'income_gross': '300000',
            'income_gross_spouse': '',
            'income_gross_monthly': '50000',
            'income_rental': '10000',
            'income_extra': '0',
            'mortgage_debt': '0',
            'student_debt': '0',
            'car_debt': '0',
            'credit_debt': '0',
            'invoice_date': '1',
            'account_number': '15032080119',
            'obligations': {
                'amount': '100000',
                'bank': 'Bank 1',
                'loan_type': 'other',
                'duration': '1',
                'monthly': '300'
            }
        }
        r = requests.post(endpoint,
                          headers=authenticate, data=payload)
        check_that('http code', r.status_code, is_(200))
        resp = r.json()
        lcc.log_info("Response\n%s" % json.dumps(resp, indent=4))

    @lcc.test("req5")
    def req5(self, endpoint, authenticate):
        payload = {
            'api_transaction_id': 'test_transaction',
            'desired_amount': '85000',
            'period': '10',
            'personal_id_number': '15028933166',
            'country_of_origin': 'no',
            'norwegian_citizen': '',
            'mobile_phone': '45875651',
            'email': 'mainapp@test.com',
            'marital_status': 'single',
            'marital_status_since': '5',
            'children_num': '0',
            'housing': 'parents',
            'rent_expense': '1000',
            'lived_on_home_address': '10',
            'education': 'university 4 years',
            'employment': 'public sector',
            'employer': 'Employer',
            'employed_from': '05.2005',
            'work_position': 'Work Position',
            'income_gross': '350000',
            'income_gross_spouse': '200000',
            'income_gross_monthly': '10000',
            'income_rental': '5000',
            'income_extra': '0',
            'mortgage_debt': '10000',
            'student_debt': '10000',
            'car_debt': '10000',
            'credit_debt': '10000',
            'account_number': '15036838202',
            'invoice_date': '1',
            'co_personal_id_number': '01127523203',
            'co_mobile_phone': '40000000',
            'co_email': 'coapp@test.com',
            'co_marital_status': 'single',
            'co_children_num': '0',
            'co_housing': 'parents',
            'co_rent_expense': '0',
            'co_lived_on_home_address': '10',
            'co_employment': 'public sector',
            'co_employer': 'Employer',
            'co_employed_from': '01.2000',
            'co_income_gross': '360000',
            'co_income_gross_monthly': '30000',
            'co_income_rental': '0',
            'co_income_extra': '0',
            'co_mortgage_debt': '0',
            'co_student_debt': '0',
            'co_car_debt': '0',
            'co_credit_debt': '0',
            'co_relationship': 'family',
            'co_education': 'primary school',
            'co_work_position': 'director',
        }
        r = requests.post(endpoint,
                          headers=authenticate, data=payload)
        check_that('http code', r.status_code, is_(200))
        resp = r.json()
        lcc.log_info("Response\n%s" % json.dumps(resp, indent=4))

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
