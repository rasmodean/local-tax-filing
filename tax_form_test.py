from tax_form import *
import pandas as pd
from config import *


TAX_DATA_PATHS = {
        2024 : {
            1 : './test/testified_taxdata_Q1_2024.csv',
            2 : './test/testified_taxdata_Q2_2024.csv',
            3 : './test/testified_taxdata_Q3_2024.csv',
            4 : ''
            },
        2023 : {
            1 : './test/testified_taxdata_Q1_2023.csv',
            2 : './test/testified_taxdata_Q2_2023.csv',
            3 : './test/testified_taxdata_Q3_2023.csv',
            4 : './test/testified_taxdata_Q4_2023.csv'
            }
        }

TAX_DATA_PATH_Q1_2024 = './test/testified_taxdata_Q1_2024.csv'
TAX_DATA_PATH_Q2_2024 = './test/testified_taxdata_Q2_2024.csv'
TAX_DATA_PATH_Q3_2024 = './test/testified_taxdata_Q3_2024.csv'
TAX_DATA_PATH_Q4_2023 = './test/testified_taxdata_Q4_2023.csv'
# TEST_TAX_DATA_Q1_2024 = pd.read_csv(TAX_DATA_PATH_Q1_2024)
# TEST_TAX_DATA_Q2_2024 = pd.read_csv(TAX_DATA_PATH_Q2_2024)
# TEST_TAX_DATA_Q3_2024 = pd.read_csv(TAX_DATA_PATH_Q3_2024)
# TEST_TAX_DATA_Q4_2023 = pd.read_csv(TAX_DATA_PATH_Q4_2023)

def get_tax_data(quarter:int, year:int):
    try:
        return pd.read_csv(TAX_DATA_PATHS[year][quarter])
    except KeyError as k:
        print(k)

def client_data(id:int, quarter:int, year:int):
    tax_data = get_tax_data(quarter, year)
    client_data = tax_data.query(f'`Client ID` == {id}')
    return client_data

TEST_CASES = [
        (name:='Fayette County School Tax',
         tax_data:=client_data(id=1, quarter=1, year=2024),
         filing_frequency:='quarterly',
         period:=1,
         year:=2024,
         client_id:=1),
        (name:='Lexington City Tax',
         tax_data:=client_data(id=1, quarter=1, year=2024),
         filing_frequency:='monthly',
         period:=3,
         year:=2024,
         client_id:=1),
        (name:='Hazard',
         tax_data:=client_data(id=1316, quarter=2, year=2024),
         filing_frequency:='quarterly',
         period:=2,
         year:=2024,
         client_id:=1316),       
        (name:='Hazard',
         tax_data:=client_data(id=1316, quarter=4, year=2023),
         filing_frequency:='quarterly',
         period:=4,
         year:=2023,
         client_id:=1316)       
        ]

EXPECTED_OUTPUTS = [
        {
            'get_client_name': 'Progressive Dynamics LLC',
            'get_loc_acct_id': 'd01122',
            'get_fein': '00-2297635',
            'get_agent_name': 'Leslie Plowman',
            'get_title_name': 'Reporting Agent',
            'get_agency_phone': '8592777401',
            'get_agency_fax': '1234567890',
            'get_agency_email': 'leslie@paydatausa.com',
            'get_agency_name': 'PaydataUSA',
            'get_agency_ein': '123456789',
            'get_agency_address': '169 Burt Rd',
            'get_agency_city': 'Lexington',
            'get_agency_state': 'KY',
            'get_agency_zip': '40503',
            'get_month': '',
            'get_quarter': '1',
            'get_year': '2024',
            'get_date': '08/28/2024',
            'get_due_date': '04/30/2024',
            'get_period_start': '01/01/2024',
            'get_period_end': '03/31/2024',
            'get_period_check': '',
            'get_employee_count': '1',
            'get_gross_wages': '22429.62',
            'get_local_taxable': '2191.62',
            'get_employee_tax': '10.98',
            'calc_employee_tax': '10.96',
            'calc_outside_wages': '20238',
            'get_form_name': 'Fayette County School Tax',
            'get_filing_frequency': 'quarterly',
            'get_period': '1',
            'get_client_id': '1'
            },
        {
            'get_client_name': 'Progressive Dynamics LLC',
            'get_loc_acct_id': 'd01122',
            'get_fein': '00-2297635',
            'get_agent_name': 'Leslie Plowman',
            'get_title_name': 'Reporting Agent',
            'get_agency_phone': '8592777401',
            'get_agency_fax': '1234567890',
            'get_agency_email': 'leslie@paydatausa.com',
            'get_agency_name': 'PaydataUSA',
            'get_agency_ein': '123456789',
            'get_agency_address': '169 Burt Rd',
            'get_agency_city': 'Lexington',
            'get_agency_state': 'KY',
            'get_agency_zip': '40503',
            'get_month': '3',
            'get_quarter': '',
            'get_year': '2024',
            'get_date': '08/28/2024',
            'get_due_date': '04/15/2024',
            'get_period_start': '03/01/2024',
            'get_period_end': '03/30/2024',
            'get_period_check': '',
            'get_employee_count': '4',
            'get_gross_wages': '22429.62',
            'get_local_taxable': '22429.62',
            'get_employee_tax': '504.66',
            'calc_employee_tax': '504.67',
            'calc_outside_wages': '0',
            'get_form_name': 'Lexington City Tax',
            'get_filing_frequency': 'monthly',
            'get_period': '1',
            'get_client_id': '1'
            },
        {
            'get_client_name': 'Bright Holdings Corp',
            'get_loc_acct_id': '611',
            'get_fein': '00-7531439',
            'get_agent_name': 'Leslie Plowman',
            'get_title_name': 'Reporting Agent',
            'get_agency_phone': '8592777401',
            'get_agency_fax': '1234567890',
            'get_agency_email': 'mypayroll@psimer.com',
            'get_agency_name': 'Psimer',
            'get_agency_ein': '123456789',
            'get_agency_address': '2533 Larkin Rd #200',
            'get_agency_city': 'Lexington',
            'get_agency_state': 'KY',
            'get_agency_zip': '40503',
            'get_month': '',
            'get_quarter': '2',
            'get_year': '2024',
            'get_date': '08/28/2024',
            'get_due_date': '07/30/2024',
            'get_period_start': '04/01/2024',
            'get_period_end': '06/30/2024',
            'get_period_check': '',
            'get_employee_count': '8',
            'get_gross_wages': '117330.00',
            'get_local_taxable': '117330.00',
            'get_employee_tax': '1465.90',
            'calc_employee_tax': '1466.62',
            'calc_outside_wages': '0',
            'get_form_name': 'Hazard',
            'get_filing_frequency': 'quarterly',
            'get_period': '2',
            'get_client_id': '1316'   
            },
         {
            'get_client_name': 'Pioneer Corporation GmbH',
            'get_loc_acct_id': '611',
            'get_fein': '00-7531439',
            'get_agent_name': 'Leslie Plowman',
            'get_title_name': 'Reporting Agent',
            'get_agency_phone': '8592777401',
            'get_agency_fax': '1234567890',
            'get_agency_email': 'mypayroll@psimer.com',
            'get_agency_name': 'Psimer',
            'get_agency_ein': '123456789',
            'get_agency_address': '2533 Larkin Rd #200',
            'get_agency_city': 'Lexington',
            'get_agency_state': 'KY',
            'get_agency_zip': '40503',
            'get_month': '',
            'get_quarter': '4',
            'get_year': '2024',
            'get_date': '08/28/2024',
            'get_due_date': '07/30/2024',
            'get_period_start': '04/01/2024',
            'get_period_end': '06/30/2024',
            'get_period_check': '',
            'get_employee_count': '8',
            'get_gross_wages': '40187.33',
            'get_local_taxable': '40187.33',
            'get_employee_tax': '1507.17',
            'calc_employee_tax': '1507.03',
            'calc_outside_wages': '0',
            'get_form_name': 'Hazard',
            'get_filing_frequency': 'quarterly',
            'get_period': '4',
            'get_client_id': '1316'   
            }
   ]


def test_tax_form():
    i = 1
    for case, output in zip(TEST_CASES, EXPECTED_OUTPUTS):
        print(f'************ Case Test:{i} ************')
        print_chunk(case_test(case, output))
        i += 1

def print_chunk(lst, size=2):
    for i in range(0, len(lst), size):
        chunk = lst[i: i + size]
        print(chunk)

    
def case_test(test_case, expected_output):
    tax_form = TaxForm(*test_case)

    failed_assertions = []

    try:
        assert (tax_form.get_client_name() 
                == expected_output['get_client_name'])
    except AssertionError:
        failed_assertions.append('get_client_name failed')

    try:
        assert (tax_form.get_loc_acct_id() 
                == expected_output['get_loc_acct_id'])
    except AssertionError:
        failed_assertions.append('get_loc_acct_id failed')

    try:
        assert (tax_form.get_fein() 
                == expected_output['get_fein'])
    except AssertionError:
        failed_assertions.append('get_fein failed')

    try:
        assert (tax_form.get_agent_name() 
                == expected_output['get_agent_name'])
    except AssertionError:
        failed_assertions.append('get_agent_name failed')

    try:
        assert (tax_form.get_title_name() 
                == expected_output['get_title_name'])
    except AssertionError:
        failed_assertions.append('get_title_name failed')

    try:
        assert (tax_form.get_agency_phone() 
                == expected_output['get_agency_phone'])
    except AssertionError:
        failed_assertions.append('get_agency_phone failed')

    try:
        assert (tax_form.get_agency_fax() 
                == expected_output['get_agency_fax'])
    except AssertionError:
        failed_assertions.append('get_agency_fax failed')

    try:
        assert (tax_form.get_agency_email() 
                == expected_output['get_agency_email'])
    except AssertionError:
        failed_assertions.append('get_agency_email failed')

    try:
        assert (tax_form.get_agency_name() 
                == expected_output['get_agency_name'])
    except AssertionError:
        failed_assertions.append('get_agency_name failed')

    try:
        assert (tax_form.get_agency_ein() 
                == expected_output['get_agency_ein'])
    except AssertionError:
        failed_assertions.append('get_agency_ein failed')

    try:
        assert (tax_form.get_agency_address() 
                == expected_output['get_agency_address'])
    except AssertionError:
        failed_assertions.append('get_agency_address failed')

    try:
        assert (tax_form.get_agency_city() 
                == expected_output['get_agency_city'])
    except AssertionError:
        failed_assertions.append('get_agency_city failed')

    try:
        assert (tax_form.get_agency_state() 
                == expected_output['get_agency_state'])
    except AssertionError:
        failed_assertions.append('get_agency_state failed')

    try:
        assert (tax_form.get_agency_zip() 
                == expected_output['get_agency_zip'])
    except AssertionError:
        failed_assertions.append('get_agency_zip failed')

    try:
        assert (tax_form.get_month() 
                == expected_output['get_month'])
    except AssertionError:
        failed_assertions.append('get_month failed')

    try:
        assert (tax_form.get_quarter() 
                == expected_output['get_quarter'])
    except AssertionError:
        failed_assertions.append('get_quarter failed')

    try:
        assert (tax_form.get_year() 
                == expected_output['get_year'])
    except AssertionError:
        failed_assertions.append('get_year failed')

    try:
        assert (tax_form.get_date() 
                == expected_output['get_date'])
    except AssertionError:
        failed_assertions.append('get_date failed')

    try:
        assert (tax_form.get_due_date() 
                == expected_output['get_due_date'])
    except AssertionError:
        failed_assertions.append('get_due_date failed')

    try:
        assert (tax_form.get_period_start() 
                == expected_output['get_period_start'])
    except AssertionError:
        failed_assertions.append('get_period_start failed')

    try:
        assert (tax_form.get_period_end() 
                == expected_output['get_period_end'])
    except AssertionError:
        failed_assertions.append('get_period_end failed')

    try:
        assert (tax_form.get_period_check() 
                == expected_output['get_period_check'])
    except AssertionError:
        failed_assertions.append('get_period_check failed')

    try:
        assert (tax_form.get_employee_count() 
                == expected_output['get_employee_count'])
    except AssertionError:
        failed_assertions.append('get_employee_count failed')

    try:
        assert (tax_form.get_gross_wages() 
                == expected_output['get_gross_wages'])
    except AssertionError:
        failed_assertions.append('get_gross_wages failed')

    try:
        assert (tax_form.get_local_taxable() 
                == expected_output['get_local_taxable'])
    except AssertionError:
        failed_assertions.append('get_local_taxable failed')

    try:
        assert (tax_form.get_employee_tax() 
                == expected_output['get_employee_tax'])
    except AssertionError:
        failed_assertions.append('get_employee_tax failed')

    try:
        assert (tax_form.calc_employee_tax() 
                == expected_output['calc_employee_tax'])
    except AssertionError:
        failed_assertions.append('calc_employee_tax failed')

    try:
        assert (tax_form.calc_outside_wages() 
                == expected_output['calc_outside_wages'])
    except AssertionError:
        failed_assertions.append('calc_outside_wages failed')

    try:
        assert (tax_form.get_form_name() 
                == expected_output['get_form_name'])
    except AssertionError:
        failed_assertions.append('get_form_name failed')

    try:
        assert (tax_form.get_filing_frequency() 
                == expected_output['get_filing_frequency'])
    except AssertionError:
        failed_assertions.append('get_filing_frequency failed')

    try:
        assert (tax_form.get_period() 
                == expected_output['get_period'])
    except AssertionError:
        failed_assertions.append('get_period failed')

    try:
        assert (tax_form.get_client_id() 
                == expected_output['get_client_id'])
    except AssertionError:
        failed_assertions.append('get_client_id failed')

    return failed_assertions


def main():

    test_tax_form()


if __name__ == "__main__":
    main()

    


