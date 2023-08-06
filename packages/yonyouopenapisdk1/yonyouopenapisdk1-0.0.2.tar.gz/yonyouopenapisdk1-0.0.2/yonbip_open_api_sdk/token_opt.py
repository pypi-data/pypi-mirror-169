import time

import requests

from .cache import MemoryCache
from .sign_opt import opt_sort_data, opt_sha256

memory_cache = MemoryCache()


def opt_self_token(app_key, app_secret, request_url):
    """
    自建token生成
    :param app_key: 自建应用app_key
    :param app_secret: 自建应用app_secret
    :param request_url: token生成请求url
    :return: token结果  json
    """
    token_param_dic = {"appKey": app_key, "timestamp": str(int(time.time() * 1000))}
    sort_data = opt_sort_data(token_param_dic)
    sign = opt_sha256(app_secret, sort_data)
    token_param_dic["signature"] = sign
    headers = {'content-type': 'application/json; charset=UTF-8'}
    http_response = requests.get(url=request_url + "/iuap-api-auth/open-auth/selfAppAuth/getAccessToken", params=token_param_dic, headers=headers)
    if http_response.status_code == 200:
        json_data = http_response.json()
        if '00000' == json_data["code"]:
            return json_data["data"]
        else:
            raise Exception("获取 accessToken 失败" + http_response.text)
    else:
        raise Exception("获取 accessToken 请求失败" + http_response.text)


def opt_self_token_with_cache(app_key, app_secret, request_url):
    """
    自建token生成，有缓存则直接返回缓存，否则请求token生成服务
    :param app_key: 自建应用app_key
    :param app_secret: 自建应用app_secret
    :param request_url: token生成请求url
    :return: token结果  json
    """
    key = app_key
    value = memory_cache.get_value(key)
    if value is None:
        value = opt_self_token(app_key, app_secret, request_url)
        if value["expire"] > 10:
            memory_cache.set_value(key, value, value["expire"] - 10)
    return value


def opt_suit_token(suite_key, suit_secret, tenant_id, request_url):
    """
    获取生态应用token
    :param suite_key: 生态应用suite_key
    :param suit_secret: 生态应用suit_secret
    :param tenant_id: 购买租户Id
    :param request_url: 获取token请求地址
    :return: token结果  json
    """
    token_param_dic = {"suiteKey": suite_key, "tenantId": tenant_id, "timestamp": str(int(time.time() * 1000))}
    sort_data = opt_sort_data(token_param_dic)
    sign = opt_sha256(suit_secret, sort_data)
    token_param_dic["signature"] = sign
    headers = {'content-type': 'application/json; charset=UTF-8'}
    http_response = requests.get(url=request_url+"/iuap-api-auth/open-auth/suiteApp/getAccessToken", params=token_param_dic, headers=headers)
    if http_response.status_code == 200:
        json_data = http_response.json()
        if '00000' == json_data["code"]:
            return json_data["data"]
        else:
            raise Exception("获取 accessToken 失败" + http_response.text)
    else:
        raise Exception("获取 accessToken 请求失败" + http_response.text)


def opt_suit_token_with_cache(suite_key, suit_secret, tenant_id, request_url):
    """
    获取生态应用token，如果有缓存则直接返回 否则会请求token生成服务
    :param suite_key: 生态应用suite_key
    :param suit_secret: 生态应用suit_secret
    :param tenant_id: 购买租户Id
    :param request_url: 获取token请求地址
    :return: token结果  json
    """
    key = suite_key + tenant_id
    value = memory_cache.get_value(key)
    if value is None:
        value = opt_suit_token(suite_key, suit_secret, tenant_id, request_url)
        if value["expire"] > 10:
            memory_cache.set_value(key, value, value["expire"])
    return value
