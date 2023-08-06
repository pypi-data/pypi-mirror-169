from __future__ import annotations
import pytest
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pyonepassword import OP


from pyonepassword import OPSecureNoteItem
from pyonepassword.py_op_exceptions import OPItemGetException


def _lookup_note_data(data, note_identifier: str):
    item = data.data_for_note(note_identifier)
    return item


@pytest.mark.parametrize("note_identifier,vault",
                         [("Example Secure Note", "Test Data"),
                          ("Example Secure Note 2", None),
                          ("t4gp6e7s6xtsiu35xq5cewxqpi", None)])
def test_get_secure_note_item_01(signed_in_op: OP, expected_secure_note_item_data, note_identifier, vault):
    expected = _lookup_note_data(
        expected_secure_note_item_data, note_identifier)
    result: OPSecureNoteItem = signed_in_op.item_get(
        note_identifier, vault=vault)
    assert isinstance(result, OPSecureNoteItem)
    assert result.note_text == expected.note_text
    assert result.unique_id == expected.unique_id
    assert result.title == expected.title
    assert result.created_at == expected.created_at
    assert result.updated_at == expected.updated_at
    assert result.last_edited_by == expected.last_edited_by
    assert result.vault_id == expected.vault_id


@pytest.mark.parametrize("invalid_note,vault",
                         [("Example Secure Note 3", None),
                          ("Example Secure Note 4", "Test Data")])
def test_get_secure_note_item_02(signed_in_op: OP, expected_secure_note_item_data, invalid_note, vault):
    exception_class = OPItemGetException
    expected = _lookup_note_data(
        expected_secure_note_item_data, invalid_note)
    try:
        signed_in_op.item_get(invalid_note, vault=vault)
        assert False, f"We should have caught {exception_class.__name__}"
    except exception_class as e:
        assert e.returncode == expected.returncode
