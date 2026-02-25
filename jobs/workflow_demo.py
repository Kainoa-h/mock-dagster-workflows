from dagster import op, job


@op
def stage_one_initialize(context):
    context.log.info("Stage 1: Initializing system resources...")
    return "System Ready"


@op
def stage_two_process_data(context, start_signal):
    context.log.info(f"Stage 2: Processing data based on: {start_signal}")
    # Simulating logic
    return "Data Processed"


@op
def stage_three_validate(context, processed_data):
    context.log.info(f"Stage 3: Validating {processed_data}...")
    return "Validation Passed"


@op
def stage_four_cleanup(context, validation_status):
    context.log.info(f"Stage 4: Final status is {validation_status}. Cleaning up.")
    return "Workflow 4 Complete"


@job
def run_workflow_demo():
    # We pass the output of one op as the input to the next
    # to create a sequential dependency graph.
    init_res = stage_one_initialize()
    proc_res = stage_two_process_data(init_res)
    val_res = stage_three_validate(proc_res)
    stage_four_cleanup(val_res)
