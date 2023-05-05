import unittest

class Money:
  def __init__(self, amount, currency):
    self.amount = amount
    self.currency = currency

  def times(self, multiplier):
    return Money(self.amount * multiplier, self.currency)

  # typing the other here!
  def __eq__(self, other):
    return self.amount == other.amount and self.currency == other.currency

  

# 5 USD x 2 = 10 USD
# 10 EUR x 3 = 30 EUR
class TestMoney(unittest.TestCase):
  def test_multiplication(self):
    for input, expected in [
      ((5,2), 10),
      ((10, 3), 30),
      ((20, 0.5), 10)
    ]:
      with self.subTest(input=input, expected=expected):
        # Arrange (Given)
        fiver = Money(input[0], "USD")
        # Act     (When)
        tenner = fiver.times(input[1])
        # Assert  (Then)
        self.assertEqual(expected, tenner.amount)
  
  def test_multiplication_in_euros(self):
    tenEuros = Money(10, "EUR")
    thirtyEuros = tenEuros.times(3)
    self.assertEqual(30, thirtyEuros.amount)
    self.assertEqual("EUR", thirtyEuros.currency)

  # def testDivision(self):
  #   originalMoney = Money(4002, "KRW") 
  #   actualMoneyAfterDivision = originalMoney.divide(4) 
  #   expectedMoneyAfterDivision = Money(1000.5, "KRW") 
  #   self.assertEqual(expectedMoneyAfterDivision.amount,
  #                       actualMoneyAfterDivision.amount)
  #   self.assertEqual(expectedMoneyAfterDivision.currency, actualMoneyAfterDivision.currency)

class MyClass:
  pass

class TestMyClass(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    cls.db_connection = "connected"
    print("I've been setup once and for all!")

  def setUp(self):
    self.my_instance = MyClass()
    print("I've been setup!")

  def tearDown(self):
    del self.my_instance
    print("I've been torn down!")

  @classmethod
  def tearDownClass(cls):
    del cls.db_connection
    print("I've cleaned up!")

  def test_method_1(self):
    print(TestMyClass.db_connection)
    pass
  def test_method_2(self):
    print(TestMyClass.db_connection)
    pass
  def test_method_3(self):
    print(TestMyClass.db_connection)
    
    pass

  

if __name__ == "__main__":
  unittest.main()

# direct from the command line
# python -m unittest money.py