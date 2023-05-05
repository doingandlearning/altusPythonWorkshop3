from aws_xray_sdk.core import xray_recorder
from aws_lambda_powertools.event_handler import APIGatewayRestResolver
from aws_lambda_powertools import Logger
from decorator import add_exception_logging

logger = Logger(service="HELLO")

app = APIGatewayRestResolver()

@app.get("/hello/<name>")
@xray_recorder.capture('hello_name')
@add_exception_logging(logger=logger)
def hello_name(name):
  raise Exception("This is an error!")
  logger.info(f"Request from {name}.")
  return {"message": f"Hello {name}!"}

@app.get("/hello")
@xray_recorder.capture('hello')
def hello():
    logger.info("Request without name")
    return {
            "message": "hello world",
        }

@app.get("/add/<int:a>/<int:b>")
def add(a,b):
    result = a + b
    if result < 0:
        logger.error(f"A less than zero error happened: {a} and {b}")
        raise Exception("Less zero")
    return {"result": result}

@xray_recorder.capture('handler')
def lambda_handler(event, context):
    logger.info(event)
    return app.resolve(event, context)