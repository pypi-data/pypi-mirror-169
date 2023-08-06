from yonbip_open_api_sdk.sign_opt import opt_sha256, opt_aes_decrypt, opt_sort_array_data, opt_aes_encrypt


def decrypt_event_encrypt(app_secret, holder):
    """
    对消息体进行解密
    :param app_secret: appSecret
    :param holder: 接收到的消息体
    :return:
    """
    holder_info = [holder["nonce"], holder["encrypt"], str(holder["timestamp"])]
    sorted_holder = opt_sort_array_data(holder_info)
    tmp_sign = opt_sha256(app_secret, sorted_holder)
    tmp_Sign_str = tmp_sign.decode("UTF-8")
    if holder["signature"] == str(tmp_Sign_str):
        return opt_aes_decrypt(app_secret, holder["encrypt"])
    else:
        raise Exception("消息体验签失败")


def encrypt_event_plain(app_key, app_secret, plain_info):
    """
    对字符串进行加密
    :param app_key: appKey
    :param app_secret: appSecret
    :param plain_info: 待加密字符串
    :return:
    """
    return opt_aes_encrypt(app_secret, plain_info, app_key)
