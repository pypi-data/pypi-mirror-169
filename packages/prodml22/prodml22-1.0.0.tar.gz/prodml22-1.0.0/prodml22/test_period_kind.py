from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class TestPeriodKind(Enum):
    """This is the type of test period: drawdowns or build up for producing
    flow tests and injection or fall-off for injecting well tests; or
    observation tests.

    Producing or injecting can be constant rate or variable rate. The
    periods where measurements are made but the testing tool is in
    motion, are covered by the "run in hole" and "pull out of hole"
    values.
    """
    BUILDUP = "buildup"
    CONSTANT_RATE_INJECTION = "constant rate injection"
    FALL_OFF = "fall-off"
    POST_TEST_PULL_OUT_OF_HOLE = "post-test pull out of hole"
    PRE_TEST_RUN_IN_HOLE = "pre-test run in hole"
    PRODUCTION_WELL_TEST = "production well test"
    VARIABLE_RATE_INJECTION = "variable rate injection"
    CONSTANT_RATE_DRAWDOWN = "constant rate drawdown"
    SHUT_IN_OBSERVATION = "shut-in observation"
    VARIABLE_RATE_DRAWDOWN = "variable rate drawdown"
