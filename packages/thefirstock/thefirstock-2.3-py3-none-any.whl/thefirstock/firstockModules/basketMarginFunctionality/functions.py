import ast
import json
import requests

from thefirstock.Variables.enums import *
from thefirstock.firstockModules.basketMarginFunctionality.base import *


class ApiRequests(FirstockAPI):
    def firstockBasketMargin(self, listData):
        """
        :return: The json response
        """
        url = BASKETMARGIN

        with open("config.json") as file:
            data = json.load(file)

        uid = data["uid"]
        jKey = data["jKey"]

        payload = {
            "uid": uid,
            "actid": uid,
            "data": listData,
        }

        jsonPayload = json.dumps(payload)
        result = requests.post(url, f'jData={jsonPayload}&jKey={jKey}')
        jsonString = result.content.decode("utf-8")

        finalResult = ast.literal_eval(jsonString)

        if finalResult['stat'] == "Not_Ok":
            return {"status": "Failed", "errorType": "UserException", "data": finalResult["emsg"]}

        elif finalResult['stat'] == "Ok":
            return {"status": "Success", "data": finalResult}
