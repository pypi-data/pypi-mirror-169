import ast
import json
import requests

from thefirstock.Variables.enums import *
from thefirstock.firstockModules.optionGreekFunctionality.base import *


class ApiRequests(FirstockAPI):
    def firstockOptionGreek(self, expiryDate: str, strikePrice: str, spotPrice: str, initRate: str,
                            volatility: str, optionType: str):
        """
        :return: The json response
        """
        url = OPTIONGREEK

        with open("config.json") as file:
            data = json.load(file)

        jKey = data["jKey"]

        payload = {
            "exd": expiryDate,
            "strprc": strikePrice,
            "sptprc": spotPrice,
            "int_rate": initRate,
            "volatility": volatility,
            "optt": optionType,
        }

        jsonPayload = json.dumps(payload)
        result = requests.post(url, f'jData={jsonPayload}&jKey={jKey}')
        jsonString = result.content.decode("utf-8")

        finalResult = ast.literal_eval(jsonString)

        if finalResult['stat'] == "OK":
            return {"status": "Success", "data": finalResult}

        elif finalResult['stat'] == "Not_Ok":
            return {"status": "Failed", "errorType": "UserException", "data": finalResult["emsg"]}
