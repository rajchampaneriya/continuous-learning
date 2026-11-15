"""Task 4: Router rules — percent asks priced against the plan, human requests in any language."""
import pytest
from pytest_bdd import parsers, scenarios, then, when

from lab.version_d import route

scenarios("features/router_rules.feature")


@pytest.fixture
def world():
    return {}


@when(parsers.parse('customer {cid} writes "{message}"'))
def customer_writes(world, cid, message):
    case = {"id": "t-route", "customer_id": cid, "message": message}
    routed = route(case)
    world["rules"] = [t["rule"] for t in routed["envelope"]["escalation_triggers"]]
    world["path"] = routed["path"]


@then(parsers.parse("the router fires the rule {rule}"))
def router_fires(world, rule):
    assert rule in world["rules"], world["rules"]


@then(parsers.parse("the router does not fire the rule {rule}"))
def router_does_not_fire(world, rule):
    assert rule not in world["rules"], world["rules"]


@then("the router takes the fast path")
def router_fast_path(world):
    assert world["path"] == "fast"


def test_a_retention_repeat_on_a_cancellation_is_not_money():
    """The exception: cancelling and asking for the retention percent again (KB11 territory)
    is not a money ask — but the same percent ask without a cancellation is."""
    cancel = {"id": "t-exc", "customer_id": "AC1017",
              "message": "I want to cancel. Give me 50% off again like last time."}
    keep = {"id": "t-exc", "customer_id": "AC1017",
            "message": "Give me 50% off again like last time."}
    rules_cancel = [t["rule"] for t in route(cancel)["envelope"]["escalation_triggers"]]
    rules_keep = [t["rule"] for t in route(keep)["envelope"]["escalation_triggers"]]
    assert "percent_ask_above_headroom" not in rules_cancel, rules_cancel
    assert "percent_ask_above_headroom" in rules_keep, rules_keep
