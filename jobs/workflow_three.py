from dagster import op, job


@op
def workflow_three(context):
    context.log.info("Hello from workflow_three")
    return "workflow_three done"


@job
def run_workflow_three():
    workflow_three()
