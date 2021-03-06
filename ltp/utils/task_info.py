from collections import namedtuple

TaskInfo = namedtuple(
    "TaskInfo",
    [
        "task_name",
        "metric_name",
        "build_dataset",
        "validation_method"
    ]
)
