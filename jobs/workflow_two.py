from dagster import op, job


@op
def workflow_two():
    print("Hello from workflow_two")
    return "workflow_two done"


@job
def run_workflow_two():
    workflow_two()