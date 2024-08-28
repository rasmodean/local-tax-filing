import sys
import pandas as pd
import config as c
## Take filing frequency, and month or quarter; completes the occupational
## tax forms for the clients in taxdata.csv


## ---Constants---
MONTHLY = 'monthly'
QUARTERLY = 'quarterly'

VALID_ARGS = {MONTHLY : range(1,13), QUARTERLY : range(1,5)}

USAGE_MESSAGE = "Usage: python main.py <filingfrequency> <period> <year>" 

TAX_DATA_PATH = c.TAX_DATA_PATH
FORM_TEMPLATES_DIR = c.FORM_TEMPLATES_DIR
OUTPUT_DIR = c.OUTPUT_DIR



## ---Functions---

# Int[1,12] -> List(String)
# Takes the month being filed for and completes all of the monthly tax forms
# for monthly filers. Returns a confirmation log of either successful or
# failed tax forms
# !!!
def file_monthly(month, year):

    tax_data = pd.read_csv(path=TAX_DATA_PATH)
    client_ids = get_client_ids(data=tax_data)
    output_log = ['']

    verify_headers(data=tax_data)
    verify_localities(data=tax_data)


    for id in client_ids:
        client_data = get_client_data(data=tax_data, 
                                      id=id)
        client_localities = get_localities(data=tax_data,
                                           id=id)
        tax_forms = get_tax_forms(localities=client_localities, 
                                  filing_frequency=MONTHLY)

        for form in tax_forms:
            confirmation = complete_tax_form(data=client_data, 
                                             form=form,
                                             period=month,
                                             ffq=MONTHLY,
                                             year=year,
                                             id=id)
            confirmation_message = f'{id} {form} {status}'
            output_log += confirmation_message

    return output_log


# DataFrame -> String
# Verifies column headers are correct
# - True -> "Pass"
# - False -> "Fail: header {invalid_header} invalid
def verify_headers(data):
    return ''


# DataFrame -> String
# Verifies all localities are in master tax list
# - "Pass"
# - "Fail" {invalid_locality} is not a valid locality
def verify_localities(data):
    return ''


# List(String) String -> Set(String)
# Take client localities and filing frequency; return names of corresponding
# tax forms 
def test_get_tax_forms():
    assert get_tax_forms(['Lexington City Tax'],'monthly') == [
            'Lexington City Tax']
    assert get_tax_forms([
        'Boone County',
        'Boone County - Sen. Cit. and Mental Health',
        'Boone County-School',], 'quarterly') == [
                'Boone County']
    assert get_tax_forms([
        'Georgetown',
        'Scott County',
        'Scott County School'], 'monthly') == [
                'Scott County']
    assert get_tax_forms([
        'Georgetown',
        'Scott County',
        'Scott County School'], 'quarterly') == [
                'Scott County']
    assert get_tax_forms([
        'Boyle County',
        'Danville',
        'Fayette County School Tax'], 'quarterly') == [
                'Boyle County',
                'Fayette County School Tax']

def get_tax_forms(locs, ffq):
    
    tax_forms = set()

    for loc in locs:
        tax_form = c.get_form_name(loc)
        tax_forms.add(tax_form)

    return list(tax_forms)

test_get_tax_forms()


# DataFrame String -> String
# Take the client data and tax form to be filed; return confirmation message
# - Complete
# - Error
# !!!
def complete_tax_form(client_data, form, ffq, period, year, id):
    
    confirmation = 'Error'
    template_path = get_template_path(form, ffq)
    save_name = get_save_name(client_data, form, ffq, period, year, id)
    save_path = os.join(OUTPUT_DIR, save_name)

    field_args = c.FieldArgs(
            client_data=client_data, filing_frequency=ffq,
            period=period,           year=year)
    field_data: Dict() = get_field_data(form=form,field_args)

    try:
        doc_pdf = fitz.open(form_path)
        page = doc_pdf.load_page(0)
    except:
        error_message = (f'Could not complete {ffq} filing for client {id}'
              + f'in {form}. Unable to open {template_path}')
        print(error_message)
        return error_message

    confirmation = update_fields(field_data, page)

    try:
        doc_pdf.save(save_path)
        doc_pdf.close
        confirmation += f'\n{form} completed successfully for {id}'
    except:
        error_message = (f'Could not complete {ffq} filing for client {id}'
                      + f'in {form}. Unable to save{template_path}')
        return error_message

    return confirmation


# String FieldArgs -> Dict
# Takes form and field args; return dict(field:value)
# uses TAX_FUNCTION_MAP to call function associated with the form, passing
# field_args
# MAKE SURE TO CHECK THE FORM
# - default()
# - [special](); where special is somerset, jefferson, etc...
# !!!

def get_field_data(form, field_args):
    tax_functions = {
            }
    return {}


# Dict Page -> String
# Updates the page fields with the field data
# !!!
def update_fields(data, page):


# String -> String
# Take a locality and return the form name associated with it
# Form name is the name of the local tax form from the county
# assumes all localities passed to get_form_name are VALID
def test_get_form_name():
    assert get_form_name('Lexington City Tax') == 'Lexington City Tax'
    assert get_form_name('Jefferson County ( Non Resident )') == (
            'Jefferson County')
    assert get_form_name('Jefferson County ( Non Resident )') == (
            'Jefferson County')
    assert get_form_name('Louisville') == 'Jefferson County'
    assert get_form_name('Boone County') == 'Boone County'
    assert get_form_name('Boone County - Sen. Cit. and Mental Health') == (
            'Boone County')
    assert get_form_name('Boone County-School') == 'Boone County'
    assert get_form_name('Georgetown') == 'Scott County'
    assert get_form_name('Scott County') == 'Scott County'
    assert get_form_name('Scott County School') == 'Scott County'
    assert get_form_name('Boyle County') == 'Boyle County'
    assert get_form_name('Danville') == 'Boyle County'
    assert get_form_name('Campbell County') == 'Campbell County'
    assert get_form_name('Highland Heights') == 'Campbell County'
    assert get_form_name('Fort Thomas') == 'Campbell County'
    assert get_form_name('Pulaski County (Somerset City Limits)') == (
        'Pulaski County (Somerset City Limits)')
    assert get_form_name('Somerset') == (
        'Pulaski County (Somerset City Limits)')

def get_form_name(loc):
    if loc in c.LOCALITY_FORM_NAME_DICT:
        return c.LOCALITY_FORM_NAME_DICT[loc]
    else:
        return loc

test_get_form_name()




# DataFrame String String Int -> String
# Gets the save name for the specific form
def get_save_name(data, form, ffq, period, year, id):
    p = f'M{period}' if ffq == MONTHLY else f'Q{period}'
    save_name = f'{Form} {year} {p} {id}.pdf'
    return save_name


# String String -> Path
# Take the form name and filing frequency; return the path to the pdf form
# !!!
def get_template_path(form, ffq):
    return './'


# DataFrame Int[1,4000]-> DataFrame
# Takes a client id; returns the corresponding data
# !!!
def get_client_data(data, id):
    return pd.DataFrame()


# DataFrame -> List(String)
# Returns the tax localities for the given client data
# !!!
def get_localities(data, id):
    return ['']


# DataFrame-> List(Int)
# Takes the tax data; returns a list of client ids
# !!!
def get_client_ids(data):
    return [-1]


# Int[1,4] -> List(String)
# Takes the quarter being filed for and completes all of the quarterly tax
# forms for quarterly filers and for quarterly recons
# !!!
def file_quarterly(quarter):
    return ['']

## ---Main--- ##
def main(arg1, arg2, arg3):
    filing_frequency = arg1
    period = arg2
    year = arg3

    if filing_frequency == MONTHLY:
        file_monthly(period, year)
    else: 
        file_quarterly(period, year)

    print(f'{period} {filing_frequency} filing for {year} complete')

    return 0


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(USAGE_MESSAGE)
    elif sys.argv[1] not in VALID_ARGS:
        print(f'Either {arg1} is not a valid option.')
    elif sys.argv[1].lower() == MONTHLY:

        if int(sys.argv[2]) not in VALID_ARGS[MONTHLY]:
            print(f'{sys.argv[2]} is not a valid month')
    
    elif sys.argv[1].lower() == QUARTERLY:

        if int(sys.argv[2]) not in VALID_ARGS[QUARTERLY]:
            print(f'{sys.argv[2]} is not a valid quarter')
    if not sys.argv[3].isnumeric():
        print(f'{sys.argv[3]} is not a valid year')

    else:
        main(sys.argv[1], sys.argv[2], sys.argv[3])



