from thefuck.main import Command
from thefuck.rules.cd_parent import match, get_new_command


def test_match():
    assert match(Command('cd..', '', 'cd..: command not found'), None)
    assert not match(Command('', '', ''), None)


def test_get_new_command():
    assert get_new_command(
        Command('cd..', '', ''), None) == 'cd ..'
