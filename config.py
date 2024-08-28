from collections import namedtuple
import code
import pandas as pd
import datetime
## Configuration for handling each tax form 


### CONSTANTS ###

TAX_DATA_PATH = './taxdata.csv'
FORM_TEMPLATES_DIR = './templates'

LOCALITY_FORM_NAME_DICT = {
'Jefferson County ( Non Resident )' : 
  'Jefferson County',
'Jefferson County ( Resident )' : 
  'Jefferson County',
'Louisville' : 
  'Jefferson County',
'Boone County ' :
  'Boone County',
'Boone County - Sen. Cit. and Mental Health' :
  'Boone County',
'Boone County-School' :
  'Boone County',
'Georgetown' :
  'Scott County',
'Scott County' :
  'Scott County',
'Scott County School' :
  'Scott County',
'Boyle County' :
  'Boyle County',
'Danville' :
  'Boyle County',
'Campbell County' :
  'Campbell County',
'Highland Heights' :
  'Campbell County',
'Fort Thomas' :
  'Campbell County',
'Pulaski County (Somerset City Limits)' :
 'Pulaski County (Somerset City Limits)',
'Somerset' :
  'Pulaski County (Somerset City Limits)',
}


TAX_FUNCTION_MAP = {
        }


#DATA_TYPES

FieldArgs = namedtuple('FieldArgs', ['client_data', 'frequency'
                                     'period', 'year'])

ReportingAgency = namedtuple('ReportingAgency', ['name',  'agent',
                                                 'title', 'ein',
                                                 'email', 'phone',
                                                 'zip',   'city',
                                                 'state', 'address',
                                                 'fax'])


## Functions:

# Float Float -> Boolean
# Check the employee tax for errors 
# !!!
def check_eetax(loc_txbl, rate):
    return False


# DataFrame String Int -> Dict
# Take client data, locality, and quarter or month; return default field
# name to value dictionary
def get_default_fields(client_data, locality, month=0, quarter=0):
    
    default_fields = {
            'Client_Name' : get_client_name(client_data),
            'Address' : reporting_agency.city,
            'Phone_Number' : reporting_agency.phone,
            'Fax' : reporting_agency.fax,
            'Period_Start' : get_period_start(quarter),
            'Period_End' : get_period_end(quarter),
            'Due_Date' : get_due_date(quarter),
            'Local_Account_ID' : get_local_account_id(client_date,
                                                      locality),
            'Employee_Count' : get_employee_count(client_data,
                                                  locality),
            'Gross_Wages' : get_gross_wages(client_data, 
                                            locality)}
    return default_fields


# Int -> ReportingAgency
# Get ReportingAgency associated with client ID 
# - Psimer if in range[1000, 1999]
# - else PDUSA
# !!!
def get_reporting_agency(client_id):
    return ReportingAgency()


# DataFrame -> Int[1, 4000]
# Take DataFrame containing client data;
# return Client ID
# !!!
def get_client_id(client_data):
    return 0


# DataFrame -> String
# Take client_data DataFrame; return Client Name
# !!!
def get_client_name(client_data):
    return ''


# Int[1,12] Int[1,4] -> Date
# Take a month or a quarter and get the period start
# !!!
def get_period_start(month = 0, quarter = 0):
    period_start = Datetime()
    return period_start


# Int[1,12] Int[1,4] -> Date
# Take month or quarter; return period end
# !!!
def get_period_end(month = 0, quarter = 0):
    period_end = Datetime()
    return period_end


# Int[1,12] Int[1,4] -> Date
# Take month or quarter; return due date
# !!!
def get_due_date(month = 0, quarter = 0):
    due_date = Datetime()
    return due_date


# DataFrame String -> Int
# Take client data dataframe and locality; return local account id
# !!!
def get_local_account_id(client_date, locality):
    local_account_id = 0
    return local_account_id


# DataFrame String -> Int
# Take client data and locality; return employee count for client at loc
# !!!
def get_employee_count(client_data, locality):
    employee_count = 0 
    return employee_count


# DataFrame String -> Float[*.00]
# Take client data and locality; return gross wages


# DataFrame -> Dict
# Take DataFrame containing client data from quarter;
# return dictionary {ashland_field_names : client_data}
def ashland_quarterly(client_data, quater):

    client_id = get_client_id(client_data)
    reporting_agency = get_reporting_agency(client_id)
    locality = 'Ashland'

    field_data = {
            'Client_Name' : get_client_name(client_data),
            'Address' : reporting_agency.city,
            'Phone_Number' : reporting_agency.phone,
            'Fax' : reporting_agency.fax,
            'Period_Start' : get_period_start(quarter),
            'Period_End' : get_period_end(quarter),
            'Due_Date' : get_due_date(quarter),
            'Local_Account_ID' : get_local_account_id(client_date, 
                                                      locality),
            'Employee_Count' : get_employee_count(client_data,
                                                  locality)}


