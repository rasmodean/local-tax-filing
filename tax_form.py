import pandas as pd
from config import *



class TaxForm:
    def __init__(
            self,
            name,
            tax_data,
            filing_frequency,
            period,
            year,
            client_id
            ):
        self.__name: String = name
        self.__tax_data: pd.DataFrame = tax_data
        self.__filing_frequency: String = filing_frequency
        self.__period: int = period
        self.__client_id: int = client_id

        self.__fields: Dict = {
                'Client_Name'              : self.get_client_name(),
                'Client_ID'                : self.__client_id,
                'Local_Account_ID'         : self.get_loc_acct_id(),
                'FEIN'                     : self.get_fein(),

                'Name_Leslie'              : self.get_agent_name(),
                'Title_Name'               : self.get_title_name(),
                'Title'                    : self.get_title_name(),
                'Phone_number'             : self.get_agency_phone(),
                'Fax'                      : self.get_agency_fax(),
                'Email'                    : self.get_agency_email(),
                'Firm_name'                : self.get_agency_name(),
                'EIN'                      : self.get_agency_ein(),
                'Address'                  : self.get_agency_address(),
                'City'                     : self.get_agency_city(),
                'State'                    : self.get_agency_state(),
                'Zip'                      : self.get_agency_zip(),

                'Month'                    : self.get_month(),
                'Quarter'                  : self.get_quarter(),
                'Year'                     : self.get_year(),
                'Date'                     : self.get_date(),
                'Due_Date'                 : self.get_due_date(),
                'Period_Start'             : self.get_period_start(),
                'Period_End'               : self.get_period_end(),
                'Period_End_Month'         : self.get_period_end()[0],
                'Period_End_Day'           : self.get_period_end()[1],
                'Period_End_Year'          : self.get_period_end()[2],
                'Due_Date_Month'           : self.get_due_date()[0],
                'Due_Date_Day'             : self.get_due_date()[1],
                'Due_Date_Year'            : self.get_due_date()[2],

                'Check_Monthly'            : self.get_period_check(),
                'Check_Quarterly'          : self.get_period_check(),

                'Employee_Count'           : self.get_employee_count(),
                'Gross_Wages'              : self.get_gross_wages(),
                'Local_Taxable'            : self.get_local_taxable(),
                'Employee_Tax'             : self.get_employee_tax(),
                'Local_Taxable_TIMES_Rate' : self.calc_employee_tax(),
                'Outside_Wages'            : self.calc_outside_wages()
                }

    def get_client_name(self):
        return '   '

    def get_loc_acct_id(self):
        return '   '

    def get_fein(self):
        return '   '

    def get_agent_name(self):
        return '   '

    def get_title_name(self):
        return '   '

    def get_agency_phone(self):
        return '   '

    def get_agency_fax(self):
        return '   '

    def get_agency_email(self):
        return '   '

    def get_agency_name(self):
        return '   '

    def get_agency_ein(self):
        return '   '

    def get_agency_address(self):
        return '   '

    def get_agency_city(self):
        return '   '

    def get_agency_state(self):
        return '   '

    def get_agency_zip(self):
        return '   '

    def get_month(self):
        return '   '

    def get_quarter(self):
        return '   '

    def get_year(self):
        return '   '

    def get_date(self):
        return '   '

    def get_due_date(self):
        return '   '

    def get_period_start(self):
        return '   '

    def get_period_end(self):
        return '   '

    def get_period_end(self):
        return '   '

    def get_period_end(self):
        return '   '

    def get_period_end(self):
        return '   '

    def get_due_date(self):
        return '   '

    def get_due_date(self):
        return '   '

    def get_due_date(self):
        return '   '

    def get_period_check(self):
        return '   '

    def get_period_check(self):
        return '   '

    def get_employee_count(self):
        return '   '

    def get_gross_wages(self):
        return '   '

    def get_local_taxable(self):
        return '   '

    def get_employee_tax(self):
        return '   '

    def calc_employee_tax(self):
        return '   '

    def calc_outside_wages(self):
        return '   '

    def get_form_name(self):
        return self.__name

    def get_tax_data(self):
        return self.__tax_data

    def get_filing_frequency(self):
        return self.__filing_frequency

    def get_period(self):
        return self.__period

    def get_client_id(self):
        return self.__client_id

    def get_reporting_agency(self):
        return ''

    
class DefaultFiling(TaxForm):
    def __init__(
            self,
            name,
            tax_data,
            filing_frequency,
            period,
            year,
            client_id
            ):
        super().__init__(
                name,
                tax_data,
                filing_frequency,
                period,
                year,
                client_id
                )
