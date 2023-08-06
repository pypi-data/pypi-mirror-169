"""
search handler
"""

from dataclasses import dataclass
from typing import List

from sanic import Blueprint
from sanic.log import logger
from sanic.response import json
from sanic_ext import openapi, validate

from python_signal_cli_rest_api.dataclasses import Error
from python_signal_cli_rest_api.lib.helper import is_phone_number
from python_signal_cli_rest_api.lib.jsonrpc import jsonrpc

search_v1 = Blueprint("search_v1", url_prefix="/search")


@dataclass
class SearchV1GetParams:
    """
    SearchV1GetParams
    """

    numbers: List[str]


@dataclass
class SearchV1GetResponse:
    """
    SearchV1GetResponse
    """

    number: str
    registered: bool


@search_v1.get("/", version=1)
@openapi.tag("Search")
@openapi.parameter(
    "numbers",
    List[str],
    required=True,
    location="query",
    description="Numbers to check",
)
@openapi.response(
    200,
    {
        "application/json": List[SearchV1GetResponse],
    },
    description="OK",
)
@openapi.response(400, {"application/json": Error}, description="Bad Request")
@openapi.description(
    "Check if one or more phone numbers are registered with the Signal Service."
)
@validate(query=SearchV1GetParams)
async def search_v1_get(
    request, query: SearchV1GetParams
):  # pylint: disable=unused-argument
    """
    Check if one or more phone numbers are registered with the Signal Service.
    """
    numbers = request.args.getlist("numbers")
    try:
        accounts = jsonrpc({"method": "listAccounts"}).get("result", [])
        network_result = []
        result = []
        for account in accounts:
            network_result = is_phone_number(
                recipients=numbers, number=account.get("number")
            )
            if network_result:
                break
        data = dict(zip(numbers, network_result))
        for key, value in data.items():
            result.append({"number": key, "registered": bool(value)})
        return json(result, 200)
    # pylint: disable=broad-except
    except Exception as err:
        error = getattr(err, "message", repr(err))
        logger.error(error)
        return json({"error": error}, 400)
