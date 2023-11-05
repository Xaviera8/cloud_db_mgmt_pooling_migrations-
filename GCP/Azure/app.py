from flask import Flask, render_template, request
import os
from dotenv import load_dotenv
from pandas import read_sql
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, text, engine
import pandas as pd

load_dotenv()  

AZUREURL = os.getenv("AZURE")

azure_engine = create_engine("mysql+mysqlconnector://xavier:Jinchuriki1@migration-test2.mysql.database.azure.com/xavierdtb")    
Session = sessionmaker(bind=azure_engine)

app = Flask(__name__)   

@app.route('/')
def mainpage():
    return render_template('base.html')

@app.route('/Medical Record')
def medicalRecordPage():
            # Establish a database connection
    with azure_engine.connect() as connection:
        # Execute an SQL query to fetch data (replace this with your query)
        query2 = text('SELECT * FROM medical_records')

        result2 = connection.execute(query2)

        # Fetch all rows of data
        medical_records = result2.fetchall()
    return render_template('medicalrecords.html', data2=medical_records)


@app.route('/Patient')
def patientPage():
        # Establish a database connection
    with azure_engine.connect() as connection:
        # Execute an SQL query to fetch data (replace this with your query)
        query1 = text('SELECT * FROM patients')

        result1 = connection.execute(query1)

        # Fetch all rows of data
        patientdata = result1.fetchall()

    return render_template('patient.html', data1=patientdata)


if __name__ == '__main__':
    app.run(
        debug=True,
        port=8080)

