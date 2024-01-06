import pytest
import mymodule

def test_returnhello():
  name = 'name'
  res = mymodule.return_hello(name)

  assert res == 'Hello name'
