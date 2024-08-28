import pandas as pd
import sys
import hashlib
import random

TAX_IMPORT_PATH = './test_tax_data.csv'
TAX_EXPORT_PATH = './testified_tax_data.csv'




def namify(name):

    def string_to_company_name(input_string, num_names=3):
        # Expanded list of common adjectives
        adjectives = [
            'Global',       'Dynamic',   'Innovative',    'Bright',
            'Rapid',        'Creative',
            'Reliable',     'Modern',    'Pioneer',       'Smart',       
            'Tech',         'NextGen',
            'Advanced',     'Elite',     'Agile',         'Future',      
            'Prime',        'Superior',
            'Visionary',    'Proactive', 'Strategic',     'Epic',        
            'Cutting-Edge', 'Leading',
            'Efficient',    'Unified',   'Synergistic',   'Progressive', 
            'Intelligent',  'Versatile',
            'Robust',       'Elegant',   'Sophisticated', 'Trailblazing',
            'Pioneering',   'Forward-Thinking'
        ]
        
        # Expanded list of common nouns
        nouns = [
            'Solutions',   'Technologies', 'Enterprises',    'Industries', 
            'Systems',
            'Concepts',    'Ventures',     'Partners',       'Holdings',
            'Services',
            'Group',
            'Dynamics',    'Innovations',  'Networks',       'Platforms',  
            'Resources',   'Developments',
           'Associates',   'Consulting',   'Designs',        'Management', 
           'Operations',   'Corporation',
            'Technics',    'Integrations', 'Fabrication',    'Productions',
            'Engineering', 'Logistics',
            'Strategies',  'Analytics',    'Transformation', 'Architecture',
            'Consultancy', 'Providers', 'Dentistry', 'Dermatology'
        ]
        
        # List of common suffixes for company names
        suffixes = [
            'Inc', 'LLC', 'Corp', 'Ltd', 'PLC', 'Co', 'GmbH', 'SAS', 'BV'
        ]

        # Seed the random number generator with the input string's hash
        random.seed(hash(input_string))
        
        # Generate a list of company names
        company_names = []
        for _ in range(num_names):
            adj = random.choice(adjectives)
            noun = random.choice(nouns)
            suffix = random.choice(suffixes)
            company_name = f"{adj} {noun} {suffix}"
            company_names.append(company_name)
        
        return company_names

# Example usage
    input_string = name
    company_names = string_to_company_name(input_string, 3)
    return company_names[0]



def fein_hash(fein):
    head = fein.split('-')[0]
    tail = fein.split('-')[1]
    
    head = '00'
    tail = numeric_hash(tail, 7)
    ffein = f'{head}-{tail}'

    return ffein


def locid_hash(id):
    id = str(id)
    id_len = len(id)

    hash_object = hashlib.sha1(id.encode())
    hash_str = str(hash_object.hexdigest())
    return hash_str[:id_len]


def numeric_hash(input_string, len=10):
    hash_object = hashlib.sha1(input_string.encode())
    # Convert the hash to an integer
    hash_integer = int(hash_object.hexdigest(), 16)
    # Apply modulo to get a number within a certain range
    numeric_hash = hash_integer % 10**len  # Limits the hash to 10 digits
    return f'{numeric_hash:0{len}d}'


def main():
   imported_taxdata = pd.read_csv(TAX_IMPORT_PATH)

   imported_taxdata['FEIN'] = imported_taxdata['FEIN'].apply(fein_hash)
   imported_taxdata['Local Account ID'] = imported_taxdata[
           'Local Account ID'].apply(locid_hash)
   imported_taxdata['Client Name'] = imported_taxdata[
           'Client Name'].apply(namify)



   imported_taxdata.to_csv(TAX_EXPORT_PATH, 
                           index=False,
                           encoding='utf-8')
   
   print('Testify complete')


if __name__ == "__main__":
    main()
