from dagster import op, job


@op
def workflow_one():
    print("Hello from workflow_one")
    return "workflow_one done"


@job
def run_workflow_one():
    workflow_one()