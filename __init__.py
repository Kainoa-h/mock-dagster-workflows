from dagster import Definitions
from .jobs.workflow_one import run_workflow_one
from .jobs.workflow_two import run_workflow_two
from .jobs.workflow_three import run_workflow_three
from .jobs.workflow_four import run_workflow_four
from .jobs.workflow_demo import run_workflow_demo

defs = Definitions(
    jobs=[
        run_workflow_one,
        run_workflow_two,
        run_workflow_three,
        run_workflow_four,
        run_workflow_demo,
    ]
)
