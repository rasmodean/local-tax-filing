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
                'ids'     : lambda x: ((x >=1 and x < 1000)
                                       or (x >= 2000 and < 9999))
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
                'ids'     :  lambda x: ((x >= 1000 and x < 2000)
              
                }
            },
        'Path' : {
            'tax_form_templates' : './templates',
            'tax_data' : './tax_data.csv',
            'output' : './output'
            }
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

