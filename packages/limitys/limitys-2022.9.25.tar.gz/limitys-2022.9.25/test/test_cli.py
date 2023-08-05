import pathlib

import pytest

import limitys.cli as cli
import limitys.limitys as api

TEST_PREFIX = pathlib.Path('test', 'fixtures', 'basic')
DEFAULT_DOCUMENTS_PATH = TEST_PREFIX / api.DEFAULT_DOCUMENTS_NAME
TEST_MAKE_MISSING = 'missing-this-file-for-'


def test_parse_request(capsys):
    options = cli.parse_request([])
    assert options == 0  # type: ignore
    out, err = capsys.readouterr()
    assert 'usage: limitys [-h] [--language LANGUAGE] [--documents DOCUMENTS]' in out
    assert not err


def test_parse_request_doc_root_option(capsys):
    options = cli.parse_request(['-l', 'english', '-d', f'{DEFAULT_DOCUMENTS_PATH}', '-q'])
    assert options.documents_pos == ''  # type: ignore
    assert options.documents == str(DEFAULT_DOCUMENTS_PATH)  # type: ignore
    out, err = capsys.readouterr()
    assert not out
    assert not err


def test_parse_request_pos(capsys):
    options = cli.parse_request([f'{DEFAULT_DOCUMENTS_PATH}', '-l', 'english', '-q'])
    assert options.documents_pos == f'{DEFAULT_DOCUMENTS_PATH}'  # type: ignore
    assert options.documents == options.documents_pos  # type: ignore
    out, err = capsys.readouterr()
    assert not out
    assert not err


def test_parse_request_pos_doc_root_not_present(capsys):
    with pytest.raises(SystemExit) as err:
        cli.parse_request([f'{TEST_MAKE_MISSING}{DEFAULT_DOCUMENTS_PATH}', '-l', 'english'])
    assert err.value.code == 2
    out, err = capsys.readouterr()
    assert not out
    message_part = (
        f'limitys: error: requested documents file at ({TEST_MAKE_MISSING}{DEFAULT_DOCUMENTS_PATH}) does not exist'
    )
    assert message_part in err
