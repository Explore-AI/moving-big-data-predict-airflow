import requests

airflow_instance_ip = ""
airflow_dag = ""

def lambda_handler(event, context):
    
    response = requests.post(f"http://{airflow_instance_ip}:8080/api/v1/dags/{airflow_dag}/dagRuns",
                             headers={"Content-Type": "application/json", "Accept": "application/json"},
                             auth = ("airflow", "airflow"),
                             json={"conf": {}})

    print('event', event)
    print('context', context)

    if response.status_code == 200:
        print("DAG triggered successfully")
    else:
        print(f"Failed to trigger the DAG, status code: {response.status_code}")
        raise Exception("Failed to trigger the DAG")