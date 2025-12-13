import json
from .utils.request import request_mmo as request
import os


def get_account(account: str):
    data = request(f"/accounts/{account}")
    return data
