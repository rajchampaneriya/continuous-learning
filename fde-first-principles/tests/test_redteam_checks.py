"""R1: the red-team-only checks, bound to tests/features/redteam_checks.feature."""
import pytest
from pytest_bdd import given, parsers, scenarios, then, when

from redteam import checks

scenarios("features/redteam_checks.feature")


@pytest.fixture
def world():
    return {}


@when(parsers.parse('the agent replies "{reply}"'))
def agent_replies(world, reply):
    world["reply"] = reply
    world["asked"] = None
    world["customer_id"] = None


@when(parsers.parse('customer "{customer_id}" wrote "{asked}" and the agent replies "{reply}"'))
def customer_replies(world, customer_id, asked, reply):
    world["customer_id"] = customer_id or None
    world["asked"] = asked or None
    world["reply"] = reply


@when(parsers.parse('the thread\'s replies are "{replies}"'))
def thread_replies(world, replies):
    world["thread"] = [r.strip() for r in replies.split(";;") if r.strip()]


@then(parsers.parse("action_claim fires {fires}"))
def action_claim_fires(world, fires):
    assert bool(checks.action_claim(world["reply"])) == (fires == "yes")


@then(parsers.parse("unsupported_number fires {fires}"))
def unsupported_number_fires(world, fires):
    assert bool(checks.unsupported_number(
        world["reply"], customer_id=world["customer_id"], asked=world["asked"])) == (fires == "yes")


@then(parsers.parse("prompt_leak fires {fires}"))
def prompt_leak_fires(world, fires):
    assert bool(checks.prompt_leak(world["reply"])) == (fires == "yes")


@then(parsers.parse("repeat_grant fires {fires}"))
def repeat_grant_fires(world, fires):
    assert bool(checks.repeat_grant(world["thread"])) == (fires == "yes")
