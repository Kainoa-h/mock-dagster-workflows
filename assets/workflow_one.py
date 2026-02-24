from dagster import asset


@asset
def workflow_one():
    print("Hello from workflow_one")
    return "workflow_one done"