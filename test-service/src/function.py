import azure.functions as func
import logging


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("inside function")
    return func.HttpResponse()
