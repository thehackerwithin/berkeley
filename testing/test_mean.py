from nose.tools import assert_equal, assert_almost_equal, assert_true, \
    assert_false, assert_raises, assert_is_instance

from mean import mean

def test_mean_zero():
  obs = mean([0,0,0,0,0,0,0,0])
  exp = 0
  assert_equal(obs, exp)

def test_mean_tol():
  big = 10000000000000000000000000000000.
  obs = mean([big,1])
  exp = big/2
  tol = 0.00000000000000000000000001
  assert_almost_equal(obs, exp, tol)

def test_mean_neg():
  obs = mean([-1,1])
  exp = 0
  assert_equal(obs, exp)

def test_mean_basic():
  obs = mean([100,150,200])
  exp = 150
  assert_equal(obs, exp)

  obs = mean([0,2,0,2,0,2])
  exp = 1
  assert_equal(obs, exp)


def test_mean_float():
  obs = mean([0,1,2,3,4,5])
  exp = 2.5
  assert_equal(obs, exp)


def test_mean():
  assert_raises(TypeError, mean, "bob")
