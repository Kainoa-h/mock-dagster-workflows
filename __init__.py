from dagster import Definitions
from .jobs.workflow_one import run_workflow_one
from .jobs.workflow_two import run_workflow_two

defs = Definitions(
    jobs=[run_workflow_one, run_workflow_two]
)