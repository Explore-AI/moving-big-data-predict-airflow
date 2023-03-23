import airflow
import json
import os
import csv
import boto3
from airflow import DAG
from datetime import timedelta, datetime
from pathlib import Path

HOME_DIR = "/opt/airflow"

#insert your mount folder

# ==============================================================

# The default arguments for your Airflow, these have no reason to change for the purposes of this predict.
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
}


# The function that uploads data to the RDS database, it is called upon later.

def upload_to_postgres(**kwargs):

	# Write a function that will upload data to your Postgres Database
	
	return "CSV Uploaded to postgres database"

def failure_sns(context):

	# Write a function that will send a failure SNS notificaiton

	return "Failure SNS Sent"

def success_sns(context):

	# Write a function that will send a success SNS Notification

	return "Success SNS sent"
# The dag configuration ===========================================================================
# Ensure your DAG calls on the success and failure functions above as it succeeds or fails.



# Write your DAG tasks below ============================================================



# Define your Task flow below ===========================================================


