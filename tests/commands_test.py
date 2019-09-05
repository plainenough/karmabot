#!/usr/bin/env python3
import pytest
import os
from collections import namedtuple


@pytest.fixture
def fixture_ban():
    import commands.ban as ban
    user = 'fred'
    channel = 'general'
    text = 'ban @<bob>'
    test = True
    kwargs = dict(text=text, test=test)
    banned = ban.ban_user(**kwargs)
    text = 'unban @<bob>'
    kwargs = dict(user=user, channel=channel, text=text, test=test)
    unbanned = ban.unban_user(**kwargs)
    kwargs = dict(user=user, channel=channel, text="unbanall", test=test)
    unbanall = ban.unban_all(**kwargs)
    return banned, unbanned, unbanall

def test_unban(fixture_ban):
    banned, unbanned, unbanall = fixture_ban
    assert unbanned == 'User bob is unbanned.\n'


def test_unbanall(fixture_ban):
    banned, unbanned, unbanall = fixture_ban
    assert unbanall == 'Cleared the ban list'
    
    
def test_ban(fixture_ban):
    banned, unbanned, unbanall = fixture_ban
    assert banned == 'User bob is banned.\n'


if __name__ == '__main__':
    print("run pytest")
