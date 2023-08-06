# __main__.py

import json
import os
import urllib.request
from datetime import datetime, timedelta
from pprint import pprint

from wrapper_api import WrapperApi



def main():
    ip = "http://localhost:8050/v1/"
    token = "dac9b15187d71ccaf53cde76816bf9948ed77d87"
    token = "857bd5593e0729e7ea7be2b8bfd2ef37889f9d92"
    token = "ee3f64d8b6a16d568bc70aad5fd8b2fa2da43d0f"

    # headers = {"Authorization": f"Token {token}"}

    print("Export env variable")
    os.system("export DJANGO_SETTINGS_MODULE=massifs.settings")

    # raise an exception if the API url is down
    urllib.request.urlopen(ip + "zm/42/").getcode()

    # GET
    print("----------- GET -------------------------------")
    api_massifs = WrapperApi(base_url=ip)
    print("GET # 1")
    api_massifs.params = "zm/42/"
    api_get = api_massifs.get()
    if api_massifs.is_error():
        raise Exception("Invalid GET ({})".format(api_massifs.get_error()))

    pprint(json.loads(api_get[0]))

    print("GET # 2")
    api_massifs.params = "massif/name/castellane/"
    api_get = api_massifs.get()
    if api_massifs.is_error():
        raise Exception("Invalid GET ({})".format(api_massifs.get_error()))

    pprint(json.loads(api_get[0]))
    #
    # print("GET # 3")
    # api_massifs.params = "massif/id/20-204-8/"
    # api_get = api_massifs.get()
    # if api_massifs.is_error():
    #     raise Exception("Invalid GET ({})".format(api_massifs.get_error()))
    #
    # pprint(json.loads(api_get[0]))

    print("GET # 4")
    api_massifs.params = "massif/lat/42.3742/long/8.918/"
    api_get = api_massifs.get()
    if api_massifs.is_error():
        raise Exception("Invalid GET ({})".format(api_massifs.get_error()))

    pprint(json.loads(api_get[0]))

    print("GET # 5")
    api_massifs.params = "massif/lat/44.10/long/5.31/"
    api_get = api_massifs.get()
    if api_massifs.is_error():
        raise Exception("Invalid GET ({})".format(api_massifs.get_error()))

    pprint(json.loads(api_get[0]))

    # POST
    print("----------- POST -------------------------------")
    api_massifs.params = "level/add/"
    print("POST # 1")
    # 1
    api_massifs.data = {
        "target_date": datetime.now().strftime("%Y-%m-%d"),
        "value": "1",
        "origin": "auto",
        "zonemeteo": "42",
        "massif": "4-42-5",
        "create_date": datetime.now().strftime("%Y-%m-%d"),
    }
    api_massifs.token = token
    api_post = api_massifs.post()
    if api_massifs.is_error():
        raise Exception(
            "Invalid POST : {} ({}) ".format(api_massifs.data, api_massifs.get_error())
        )

    pprint(json.loads(api_post[0]))

    print("POST # 2")
    # 2
    api_massifs.data = {
        "target_date": (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d"),
        "value": "2",
        "origin": "admin",
        "zonemeteo": "42",
        "massif": "4-42-4",
        "create_date": (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d"),
    }
    api_post = api_massifs.post()
    if api_massifs.is_error():
        raise Exception(
            "Invalid POST : {} ({})".format(api_massifs.data, api_massifs.get_error())
        )

    pprint(json.loads(api_post[0]))

    # PUT
    print("----------- PUT -------------------------------")
    print("PUT # 1")
    api_massifs.params = (
            "level/update/zm/42/target_date/" + datetime.now().strftime("%Y-%m-%d") + "/"
    )
    api_massifs.data = {"value": 99, "origin": "admin"}
    api_put = api_massifs.put()
    if api_massifs.is_error():
        raise Exception(
            "Invalid PUT : {} ({})".format(api_massifs.data, api_massifs.get_error())
        )

    pprint(json.loads(api_put[0]))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Erreur : {e}")
    finally:
        print("That's all folks...")
