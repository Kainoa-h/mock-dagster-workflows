from dagster import op, job


@op
def workflow_three():
    print("Hello from workflow_three")
    return "workflow_three done"


@job
def run_workflow_three():
    workflow_three()

