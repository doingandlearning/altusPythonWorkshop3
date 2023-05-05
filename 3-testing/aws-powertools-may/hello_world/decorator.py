## 


def add_exception_logging(logger):
  def wrapper(func):
      def inner(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except Exception as e:
                logger.error(f"{func.__name__}, {args}, {kwargs}, {e}")
                return {"message": "There was an error"}, 400
      return inner
  return wrapper