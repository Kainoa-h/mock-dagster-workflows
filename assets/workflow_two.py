from dagster import asset


@asset
def workflow_two():
    print("Hello from workflow_two")
    return "workflow_two done"