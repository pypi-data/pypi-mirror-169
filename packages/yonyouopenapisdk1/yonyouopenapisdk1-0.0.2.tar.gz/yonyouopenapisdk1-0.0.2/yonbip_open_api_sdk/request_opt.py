import requests

from . import token_opt


def opt_self_app_request(method, request_url, header, data, params, token_info):
    """
    直接使用内置access_token获取方式调用自建应用业务请求
    :param method: http请求方式 支持 post get
    :param request_url: 要请求的业务url
    :param header: 业务url请求需要的header业务信息（目前仅默认设置 application/json，和access_token）
    :param data: 业务请求参数
    :param params: url拼接参数
    :param token_info: 获取access_token需要的参数 app_key，app_secret，token_url（token请求域名）
    :return: response
    """
    response = token_opt.opt_self_token(token_info["app_key"], token_info["app_secret"], token_info["token_url"])
    header["access_token"] = response["access_token"]
    header['content-type'] = 'application/json; charset=UTF-8'
    if "post" == method.lower():
        return requests.post(url=request_url, headers=header, data=data, params=params)
    if "get" == method.lower():
        return requests.get(url=request_url, headers=header, params=params)


def opt_self_app_request_with_access_token(method, request_url, header, data, params, access_token):
    """
    通过access_token 调用自建应用业务请求
    :param method: http请求方式 支持 post get
    :param request_url: 要请求的业务url
    :param header: 业务url请求需要的header业务信息（目前仅默认设置 application/json，和access_token）
    :param data: 业务请求参数
    :param params: url拼接参数
    :param access_token: access_token
    :return: 接口抵用结果，response
    """
    header["access_token"] = access_token
    header['content-type'] = 'application/json; charset=UTF-8'
    if "post" == method.lower():
        return requests.post(url=request_url, headers=header, data=data, params=params)
    if "get" == method.lower():
        return requests.get(url=request_url, headers=header, params=params)


def opt_self_app_request_with_cache(method, request_url, header, data, params, token_info):
    """
    使用缓存的access_token 调用自建应用业务请求调用 -- 推荐
    :param method: http请求方式 支持 post get
    :param request_url: 要请求的业务url
    :param header: 业务url请求需要的header业务信息（目前仅默认设置 application/json，和access_token）
    :param data: 业务请求参数
    :param params: url拼接参数
    :param token_info: 获取access_token需要的参数 app_key，app_secret，token_url（token请求域名）
    :return: response
    """
    response = token_opt.opt_self_token_with_cache(token_info["app_key"], token_info["app_secret"],
                                                   token_info["token_url"])
    return opt_self_app_request_with_access_token(method, request_url, header, data, params, response["access_token"])


def opt_suit_request(method, request_url, header, data, params, token_info):
    """
    直接使用内置access_token获取方式调用生态应用业务请求
    :param method: http请求方式 支持 post get
    :param request_url: 要请求的业务url
    :param header: 业务url请求需要的header业务信息（目前仅默认设置 application/json，和access_token）
    :param data: 业务请求参数
    :param params: url拼接参数
    :param token_info: 获取access_token需要的参数 包括suit_key，suite_secret，tenant_id，token_url（token请求地址）
    :return: response
    """
    response = token_opt.opt_suit_token(token_info["suite_key"], token_info["suite_secret"], token_info["tenant_id"],
                                        token_info["token_url"])
    header["access_token"] = response["access_token"]
    header['content-type'] = 'application/json; charset=UTF-8'
    if "post" == method.lower():
        return requests.post(url=request_url, headers=header, data=data, params=params)
    if "get" == method.lower():
        return requests.get(url=request_url, headers=header, params=params)


def opt_suit_request_with_access_token(method, request_url, header, data, params, access_token):
    """
    通过access_token 调用生态应用业务请求
    :param method: http请求方式 支持 post get
    :param request_url: 要请求的业务url
    :param header: 业务url请求需要的header业务信息（目前仅默认设置 application/json，和access_token）
    :param data: 业务请求参数
    :param params: url拼接参数
    :param access_token: access_token
    :return: 接口抵用结果，response
    """
    header["access_token"] = access_token
    header['content-type'] = 'application/json; charset=UTF-8'
    if "post" == method.lower():
        return requests.post(url=request_url, headers=header, data=data, params=params)
    if "get" == method.lower():
        return requests.get(url=request_url, headers=header, params=params)


def opt_suit_request_with_cache(method, request_url, header, data, params, token_info):
    """
    使用缓存的access_token 调用生态应用业务请求调用 -- 推荐
    :param method: http请求方式 支持 post get
    :param request_url: 要请求的业务url
    :param header: 业务url请求需要的header业务信息（目前仅默认设置 application/json，和access_token）
    :param data: 业务请求参数
    :param params: url拼接参数
    :param token_info: 获取access_token需要的参数 包括suit_key，suite_secret，tenant_id，token_url（token请求地址）
    :return: response
    """
    response = token_opt.opt_suit_token_with_cache(token_info["suite_key"], token_info["suite_secret"],
                                                   token_info["tenant_id"],
                                                   token_info["token_url"])
    return opt_suit_request_with_access_token(method, request_url, header, data, params, response["access_token"])
