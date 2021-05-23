import enum


class ExecType(enum.Enum):
    predict = 'predict'
    cross_validate = 'cross-validate'
