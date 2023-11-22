# init project

pip install -r requirements.txt
# preparing databases
## Make Tables
python3 db/moduleSql/module.py
## Insert data from api
python3 db/moduleSql/insertData.py

# Run project 
univcorn main:app --reload
