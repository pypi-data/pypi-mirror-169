from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pyonepassword import OP

from pyonepassword import OPUserGetException


def _lookup_user_data(data, user_identifier: str):
    item = data.data_for_user(user_identifier)
    return item


def test_get_user_01(signed_in_op: OP, expected_user_data):
    # get vault "Test Data"
    user_identifier = "Example User"
    expected = _lookup_user_data(expected_user_data, user_identifier)
    result = signed_in_op.user_get(user_identifier)

    assert result.unique_id == expected.unique_id
    assert result.name == expected.name
    assert result.email == expected.email
    assert result.updated_at == expected.updated_at
    assert result.created_at == expected.created_at
    assert result.last_auth_at == expected.last_auth_at


def test_get_invalid_user_01(signed_in_op: OP, expected_user_data):
    user_identifier = "No Such User"
    expected = _lookup_user_data(expected_user_data, user_identifier)
    try:
        signed_in_op.user_get(user_identifier)
        assert False, "We should have caught an OPGetUserException"
    except OPUserGetException as e:
        assert e.returncode == expected.returncode
