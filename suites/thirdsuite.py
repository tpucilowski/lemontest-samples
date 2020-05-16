import lemoncheesecake.api as lcc
import requests
from lemoncheesecake.matching import check_that, is_


@lcc.suite("my_suite")
class thirdsuite:
    @lcc.test("Submit existing application or sent less than 3 months ago")
    def req1(self):
        url = 'http://api.dev.compareking.no/api/application'
        payload = {
            'api_transaction_id': 'test_transaction',
            'desired_amount': '85000',
            'period': '1',
            'personal_id_number': '',
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
        }
        auth_headers = {
            'Authorization': 'Login: Test, Password: Test'
        }
        r = requests.post(url,
                          headers=auth_headers, data=payload)
        check_that('http code', r.status_code, is_(400))
        r.raise_for_status
        print(r.json())

    @lcc.test("Submit unfinished application with all required information")
    def req2(self):
        url = 'http://api.dev.compareking.no/api/contact'
        payload = {
            "email":  "test@test.com",
            "phone":  "40000001",
            "amount":  "85000",
        }
        auth_headers = {
            'Authorization': 'Login: Test, Password: Test'
        }
        r = requests.post(url,
                          headers=auth_headers, json=payload)
        check_that('http code', r.status_code, is_(200))
        r.raise_for_status
        print(r.json())

    @lcc.test("Submit unfinished application with incomplete required info")
    def req3(self):
        url = 'http://api.dev.compareking.no/api/contact'
        payload = {
            "email":  "",
            "phone":  "",
            "amount":  "85000",
        }
        auth_headers = {
            'Authorization': 'Login: Test, Password: Test'
        }
        r = requests.post(url,
                          headers=auth_headers, json=payload)
        check_that('http code', r.status_code, is_(400))
        print(r.json())

    @lcc.test("Submit unfinished application that already exists")
    def req4(self):
        url = 'http://api.dev.compareking.no/api/contact'
        payload = {
            "email":  "test@test.com",
            "phone":  "40000001",
            "amount":  "85000",
        }
        auth_headers = {
            'Authorization': 'Login: Test, Password: Test'
        }
        r = requests.post(url,
                          headers=auth_headers, json=payload)
        check_that('http code', r.status_code, is_(422))
        print(r.json())
