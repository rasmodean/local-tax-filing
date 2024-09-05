from tax_form import *
import pandas as pd


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
TEST_TAX_DATA_Q1_2024 = pd.read_csv(TAX_DATA_PATH_Q1_2024)
TEST_TAX_DATA_Q2_2024 = pd.read_csv(TAX_DATA_PATH_Q2_2024)
TEST_TAX_DATA_Q3_2024 = pd.read_csv(TAX_DATA_PATH_Q3_2024)
TEST_TAX_DATA_Q4_2023 = pd.read_csv(TAX_DATA_PATH_Q4_2023)
CONFIG = {
        'ReportingAgency' : {
            'PaydataUSA' : {
                'name'    : 'PaydataUSA',
                'agent'   : 'Leslie Plowman',
                'title'   : 'Reporting Agent',
                'ein'     : '123456789',
                'email'   : 'leslie@paydatausa.com',
                'phone'   : '8592777401',
                'zip'     : '40503',
                'city'    : 'Lexington',
                'state'   : 'Kentucky',
                'address' : '169 Burt Rd',
                'fax'     : '1234567890',
                'ids'     : '[1,999],[2000,9999]'
                },
            'Psimer' : {
                'name'    : 'Psimer',
                'agent'   : 'Leslie Plowman',
                'title'   : 'Reporting Agent',
                'ein'     : '123456789',
                'email'   : 'psimer@paydatausa.com',
                'phone'   : '8592777401',
                'zip'     : '40503',
                'city'    : 'Lexington',
                'state'   : 'Kentucky',
                'address' : '2533 Larkin Rd #200',
                'fax'     : '1234567890',
                'ids'     : '[1000, 1999]'               
                }
            },
        'Path' : {
            'tax_form_templates' : './templates',
            'tax_data'           : './tax_data.csv',
            'output'             : './output'
            }
        }
    


def get_tax_data(quarter:int, year:int):
    try:
        return pd.read_csv(TAX_DATA_PATHS[year][quarter])
    except KeyError as k:
        print(k)

def client_data(id:int, quarter:int, year:int):
    tax_data = get_tax_data(quarter, year)
    client_data = tax_data.query(f'`Client ID` == {id}')
    return client_data


test_cases = [
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

expected_outputs = [
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
            'get_form_name': 'Lexington City Tax',
            'get_filing_frequency': 'monthly',
            'get_period': '1',
            'get_client_id': '1'   
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
            'get_period': '4',
            'get_client_id': '1316'   
            }
   ]


expected_output = {
        'get_client_name': '',
        'get_loc_acct_id': '',
        'get_fein': '',
        'get_agent_name': '',
        'get_title_name': '',
        'get_agency_phone': '',
        'get_agency_fax': '',
        'get_agency_email': '',
        'get_agency_name': '',
        'get_agency_ein': '',
        'get_agency_address': '',
        'get_agency_city': '',
        'get_agency_state': '',
        'get_agency_zip': '',
        'get_month': '',
        'get_quarter': '',
        'get_year': '',
        'get_date': '',
        'get_due_date': '',
        'get_period_start': '',
        'get_period_end': '',
        'get_period_check': '',
        'get_employee_count': '',
        'get_gross_wages': '',
        'get_local_taxable': '',
        'get_employee_tax': '',
        'calc_employee_tax': '',
        'calc_outside_wages': '',
        'get_form_name': '',
        'get_tax_data': '',
        'get_filing_frequency': '',
        'get_period': '',
        'get_client_id': '',
        'get_config': '',
        'get_reporting_agency': ''
        }


def test_tax_from():
    pass



