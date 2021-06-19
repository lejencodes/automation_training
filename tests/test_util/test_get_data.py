from util.gettestdata import get_test_data
import os

def test_get_data():
    result = get_test_data(os.path.join('data', 'case.xlsx'), 'Login')
    # print(result)
    assert result == [
        {'id': 'login3', 'username': 'tissue@gmail.com', 'pwd': '123', 'suc': '0', 'assert': 'Invalid password.'},
        {'id': 'login1', 'username': 'li22@gmail.com', 'pwd': 'li', 'suc': '0', 'assert': 'Invalid password.'},
        {'id': 'login2', 'username': 'tissue@gmail.com', 'pwd': 'tissue123', 'suc': '1', 'assert': 'MY ACCOUNT'},
    ]
