# -*- coding: utf-8 -*-
import unittest
import nose
import pytest

from selenium.webdriver.firefox.webdriver import WebDriver
from TestBase import UserLogin
from group_lib import Group, Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.off)
    return fixture


def test_create_group(app):
    """Validation of correct create test group"""
    app.open_home_page()
    app.login(UserLogin.name, UserLogin.password)
    app.create_group(Group(group_name='test', group_header='test', group_footer='test'))
    app.click_group_page()



if __name__ == '__main__': # if run as a script or by 'python -m pytest'
    # we trigger the below "else" condition by the following import
    import pytest
    raise SystemExit(pytest.main())


'''
if __name__ == "__main__":
    nose.run(argv=["nosetests", "tests_group.py", "--verbosity=2"])'''