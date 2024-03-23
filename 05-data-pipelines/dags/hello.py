from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator
from airflow.utils import timezone


with DAG(
    "hello",
    start_date=timezone.datetime(2024, 3 ,23),
    schedule=None,
    tags=["DS525"],
):
    start = EmptyOperator(task_id="start")

    echo_hello = BashOperator(
        task = "echo_hello",
        bash_commands"echo 'hello'",
    )
    end = EmptyOperator(task_id="end")

    start >> end
