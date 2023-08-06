# request.py
import json
import logging
import requests
import ssl
import sys
from datetime import datetime
from datetime import timedelta
from pprint import pprint
from urllib.error import HTTPError
from urllib.error import URLError
from urllib.request import Request
from urllib.request import urlopen

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


class WrapperApi:
    def __init__(self, base_url="http://localhost"):
        """

        :param base_url:
        """
        self.base_url = base_url
        self.complete_url = ""
        self._data = {}
        self.header = ""
        self._token = None
        self.response = None
        self.status = None
        self._params = ""
        self._error = False
        self.error_message = ""
        self.verify_certificate = False
        self.status_ok = [200, 201]

        formatter = "%(asctime)s => %(name)s : %(message)s from %(filename)s:%(lineno)d in %(funcName)s()"
        logging.basicConfig(
            filename="wrapper_api.log",
            encoding="utf-8",
            level=logging.INFO,
            format=formatter,
        )

    @property
    def data(self):
        """

        :return:
        """
        return self._data

    @data.setter
    def data(self, datas):
        """

        :param data:
        :return:
        """
        if isinstance(datas, dict):
            self._data = datas
        else:
            raise Exception("data() : The data if required.")

    @property
    def params(self):
        """

        :return:
        """
        return self._params

    @params.setter
    def params(self, param):
        """

        :param param:
        :return:
        """
        if param and len(param) > 0:
            self._params = param
            self.complete_url = self.base_url + param
        else:
            raise Exception("params() : The param if required.")

    @property
    def token(self):
        """

        :return:
        """
        return self._token

    @token.setter
    def token(self, token):
        """

        :param token:
        :return:
        """
        logging.info("@token.setter")
        if token and len(token) > 0:
            self._token = token
        else:
            logging.error("@token.setter : The token if required")
            raise Exception("set_token() : The token if required.")

    def post(self):
        """

        :return:
        """
        logging.info("post()")
        self.response = {}, {}
        try:
            if self.token is not None and self.data:
                self.header = {"Authorization": "Token {}".format(self.token)}
                logging.info(
                    "post() : {}, {}, {}".format(
                        self.header, self.complete_url, self.data
                    )
                )

                response = requests.post(
                    self.complete_url,
                    headers=self.header,
                    data=self.data,
                    verify=self.verify_certificate,
                )
                if response:
                    logging.info(
                        "post(response) : status={}, response={} ".format(
                            response.status_code, response.text
                        )
                    )
                    self.status = response.status_code
                    self.response = response.text, response
        except Exception as e:
            logging.error("post() : Exception ({})".format(str(e)))
        finally:
            return self.response

    def get(self):
        """

        :return:
        """
        logging.info("get()")
        request = Request(self.complete_url, headers=self.header or {})
        logging.info(
            "get() : {}, {} => request={}".format(
                self.header, self.complete_url, request
            )
        )
        self.response = {}, {}
        try:
            with urlopen(request, timeout=10, context=ctx) as response:
                logging.info("get() : {} ".format(response.status))
                self.status = response.status
                self.response = response.read(), response
        except Exception as e:
            logging.error("get() : Exception ({})".format(e))
        finally:
            logging.info("get(finally) : {} ".format(self.response))
            return self.response

    def put(self):
        """

        :return:
        """
        logging.info("put()")
        self.response = {}, {}
        response = {}
        try:
            if self.token is not None and self.data:
                logging.info(
                    "put() : {}, {}, {}".format(
                        self.header, self.complete_url, self.data
                    )
                )
                self.header = {"Authorization": "Token {}".format(self.token)}

                response = requests.put(
                    self.complete_url,
                    headers=self.header,
                    data=self.data,
                    verify=self.verify_certificate,
                )
                if response:
                    logging.info("put(response) : {} ".format(response.status_code))
                    self.status = response.status_code
                    self.response = response.text, response
        except Exception as e:
            logging.error("put() : Exception ({})".format(str(e)))
        finally:
            logging.info(
                "put(finally) : self.response={}, response={} ".format(
                    self.response, response.content
                )
            )
            return self.response

    def is_error(self):
        # logging.info("is_error() : response={}".format(self.response))
        code_http = self.status
        self.error_message = None
        if self.response[0]:
            response = json.loads(self.response[0])
            if isinstance(response, dict):
                code_http = (
                    response.get("result").get("code_http")
                    if "result" in response
                    else self.status
                )
                self.error_message = response.get("message_error", "")

        self._error = (
                (self.status not in self.status_ok)
                or (code_http not in self.status_ok)
                or (len(self.error_message) > 0)
        )

        logging.info(
            "is_error() : status={}, self._error={}, error_message={}, len error_message={}, code_http={}".format(
                self.status,
                self._error,
                self.error_message,
                len(self.error_message),
                code_http,
            )
        )
        return self._error

    def get_error(self):
        try:
            msg_error = {"message_error": "", "code_http": ""}
            if self.response[0]:
                self.error_message = json.loads(self.response[0])
                # logging.info("get_error() : response={}".format(self.response))

                if "message_error" in self.error_message:
                    msg_error["message_error"] = self.error_message.get(
                        "message_error", None
                    )
                if "detail" in self.error_message:
                    msg_error["message_error"] = self.error_message.get("detail", None)
                if "result" in self.error_message:
                    result = self.error_message.get("result", None)
                    if "code_http" in result:
                        msg_error["code_http"] = result.get("code_http", None)

        except (TypeError, AttributeError, IndexError, KeyError):
            logging.error(
                "get_error() : 'TypeError, AttributeError, IndexError, KeyError'"
            )
            return None
        except Exception as e:
            logging.error("get_error() : Exception ({})".format(str(e)))
        finally:
            self.error_message = msg_error
            logging.info("get_error() : finally ({})".format(self.error_message))
            return self.error_message or None
