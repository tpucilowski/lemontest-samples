import requests
import lemoncheesecake.api as lcc
#import amadeus
#from amadeus import Client, ResponseError


@lcc.fixture(scope="test")
def user_auth(cli_args):
    # we assume that custom cli arguments "user" and "password" have been
    # previously set through project file
    return cli_args.user, cli_args.password


@lcc.fixture(scope="test")
def api(user_auth):
    session = requests.Session()
    session.auth = user_auth
    return session


@lcc.fixture(scope="test")
def endpoint():
    url = 'http://api.dev.compareking.no/api/application'
    return url


@lcc.fixture(scope="test")
def authenticate():
    auth_headers = {
        'Authorization': 'Login: Test, Password: Test'
    }
    return auth_headers

@lcc.fixture(scope="test")
def glc_url():
#    glc_sap = 'https://irisplus.tui.de/ipl360/api'
    glc_sap = 'http://dummy.restapiexample.com/api/v1/employees'
#    glc_sap = 'https://irisplus-local.tui.de/irisplus/'
    return glc_sap


@lcc.fixture(scope="test")
def glc_auth():
    glc_headers = {
    'Authorization': 'user_id: IPLUSST,  password: '
    }
    return glc_headers  

@lcc.fixture(scope="test")
def throughput():
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
        'account_number': '15032080119'
    }
    return payload

@lcc.fixture(scope="test")
def authorization():
    amd = {
        'client_id': 'txOuJU8GZ82uqfBBrmoUer7ToGqTK6Mm',
        'client_secret': 'FCwVX3vDVT3FEpWs'
    }
    return amd

@lcc.fixture(scope="test")
def inspiration():
    inspiration_payload = {
        'origin': 'PAR',
        'destination': 'MAD',
        'departureDate': '2019-09-01'
    }
    return inspiration_payload

@lcc.fixture(scope="session")
def login_details():
    login_context = {
        'user_id':[],
        'login': [],
        'office_id': [],
        'agent_sign': [],
        'agent_initials': [],
        'duty_code': [],
        'organization': []
    }
    return login_context

@lcc.fixture(scope="test")
def office_lat():
    av_lat = ['AF', 'AV', 'AY', 'BA', 'FB', 'LH', 'SQ', 'XB', '0E', '2X', '6X', '7X', '8X']
    return av_lat

@lcc.fixture(scope="test")
def companies_test():
    company_profiles = [
        {'recloc': 'TC381N', 'Company name': 'Suez Energy Servicios Es'},
        {'recloc': '216FGC', 'Company name': 'Gemalto'},
        {'recloc': '3SGTGC', 'Company name': 'Bnp Paribas Freire'},
        {'recloc': '1R3LFR', 'Company name': 'Peugeot Polska'},
        {'recloc': '39BFZS', 'Company name': 'Instytut Lotnictwa'}
    ]
    return company_profiles

@lcc.fixture(scope="test")
def agencies_test():
    agency_profiles = [
        {'recloc': 'KB8F5H', 'Agency name': 'Amadeus'},
        {'recloc': 'HG8M69', 'Agency name': 'Plp'},
        {'recloc': 'VD4J2G', 'Agency name': 'Agence Amadeus Projets'}
    ]
    return agency_profiles