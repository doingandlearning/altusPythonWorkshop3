import unittest

class Money:
  def __init__(self, amount, currency):
    self.amount = amount
    self.currency = currency

  def times(self, multiplier):
    return Money(self.amount * multiplier, self.currency)

# 5 USD x 2 = 10 USD
# 10 EUR x 3 = 30 EUR
class TestMoney(unittest.TestCase):
  def test_multiplication(self):
    # Arrange (Given)
    fiver = Money(5, "USD")
    # Act     (When)
    tenner = fiver.times(2)
    # Assert  (Then)
    self.assertEqual(10, tenner.amount)
  
  def test_multiplication_in_euros(self):
    tenEuros = Money(10, "EUR")
    thirtyEuros = tenEuros.times(3)
    self.assertEqual(30, thirtyEuros.amount)
    self.assertEqual("EUR", thirtyEuros.currency)


if __name__ == "__main__":
  unittest.main()