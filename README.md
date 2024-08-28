# Local Tax Filing

This script completes the local tax forms (.pdf) for the counties & cities
in Kentucky. 


main.py: run on command line; takes filing frequency 
("monthly" or "quarterly"), and month [1,12] or quarter [1,4]. Assumes 
config.py, profile.py, profiles.json, and taxdata.csv are in root directory.

config.py: contains default and tax-form specific field->data maps for each
pdf. Field names in pdf and config must match. 

profile.py: data structures for the tax agent info. 

profiles.json: contains the tax agent specific information. 

taxdata.csv: contians the actual tax data used for filing the forms


---TESTING---

testify.py: turns tax data into fictitious tax data for testing and example

