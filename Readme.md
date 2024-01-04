# Project Setup
- create virtual environment
`virtualenv env`
- activate virtual environment
`source env/bin/activate`
- Install all required dependent libraries
`pip install -r requirements.txt`
- Check app is up and running
`streamlit run app.py`


### Setup DB
---
Store your db connection in `config.yaml`
Create a db name `expense` and run following command

`
python src/db_create.py
`



