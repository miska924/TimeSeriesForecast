import enum


PROCESSES_COUNT = 5


class ExecType(enum.Enum):
    predict = 'predict'
    cross_validate = 'cross-validate'
