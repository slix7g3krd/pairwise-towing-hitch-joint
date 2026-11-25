import pytest
import gameplay.towing_hitch_joint as mod

CASES = [
    ("constraint_substep", (1,)),
    ("hitch_server_confirm", (1,)),
    ("damping_by_load", (1,)),
    ("quat_angle_limit", (1,)),
    ("trailer_state_sync", (1,)),
    ("replay_authoritative", (1,)),
    ("attach", (1,)),
    ("drive", (1,)),
    ("detach", (1,)),
    ("present", (1,)),
    ("validate_tow", (1,)),
    ("metrics", (1,)),
    ("audit", (1,)),
    ("fallback", (1,)),
    ("determinism", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
