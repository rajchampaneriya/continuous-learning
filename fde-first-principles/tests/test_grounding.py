"""Task 3: the envelope's grounded_kb_ids must cover each suite's kb_sources (KB ids only)."""
import pytest

from lab.acme import data_root, load_cases
from lab.grounding_report import SUITES, recall_for

FOUR_SUITES = ["base", "abuse", "multiturn", "regional"]


@pytest.mark.parametrize("suite", FOUR_SUITES)
def test_grounding_recall_at_least_90_percent_per_suite(suite):
    cases = load_cases(data_root() / SUITES[suite])
    recall, hits, total, misses = recall_for(cases)
    assert total > 0, suite
    assert recall >= 0.9, misses


def test_grounding_report_covers_every_suite_with_kb_sources():
    assert set(FOUR_SUITES) <= set(SUITES)
