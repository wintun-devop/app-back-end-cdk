#main heldler
import logging,json


# Python Logging Service
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
    logger.info(event)
    logger.info("authorization")
    return {"message":"success"}