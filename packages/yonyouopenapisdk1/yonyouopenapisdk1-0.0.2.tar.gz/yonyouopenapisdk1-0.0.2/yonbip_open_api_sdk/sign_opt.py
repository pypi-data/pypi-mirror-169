import base64
import hmac
import random
import re
from hashlib import sha256
from Cryptodome.Cipher import AES


def opt_sort_data(dics):
    """
    对数据进行升序排序，并拼接返回字符串
    :param dics: 要排序的集合 字典类型
    :return:
    """
    dic = ""
    if dics is None:
        return dic
    cust = sorted(dics.keys(), reverse=False)
    for da in cust:
        dic = dic + da + dics.get(da)
    return dic


def opt_sort_array_data(dics):
    """
    对数据进行升序排序，并拼接返回字符串
    :param dics: 要排序的集合 字典类型
    :return:
    """
    dic = ""
    if dics is None:
        return dic
    cust = sorted(dics, reverse=False)
    for da in cust:
        dic = dic + da
    return dic


def opt_sha256(key, data):
    """
    基于base64加密的sha256加密
    :param key: key
    :param data: 要加密的数据
    :return: 加密结果
    """
    return base64.b64encode(
        hmac.new(key.encode('utf-8'), data.encode('utf-8'), digestmod=sha256).digest())


def opt_aes_encrypt(app_secret, msg, app_key):
    """
    对消息进行AES加密
    :param app_secret: appSecret
    :param msg: 要加密的消息体
    :param app_key:appKey
    :return:
    """
    key = build_aes_key_from_secret(app_secret) + "="
    random_str = get_random_str()
    randomStrBytes = random_str.encode('utf-8')
    textBytes = msg.encode('utf-8')
    network_bytes_order = get_network_bytes_order(len(textBytes))
    suiteKeyBytes = app_key.encode('utf-8')
    byte_collector = randomStrBytes + network_bytes_order + textBytes + suiteKeyBytes
    amountToPad = AES.block_size - (len(byte_collector) % AES.block_size)
    if amountToPad == 0:
        amountToPad = AES.block_size
    padChr = amountToPad & 0xFF
    for index in range(amountToPad):
        byte_collector += str(padChr).encode("utf-8")
    aes_key = base64.b64decode(key)
    cryptor = AES.new(aes_key, AES.MODE_CBC, aes_key[:16])
    ciphertext = cryptor.encrypt(byte_collector)
    return str(base64.b64encode(ciphertext), encoding='utf-8')


def get_network_bytes_order(source_number):
    """
    生成4个字节的网络字节序
    :param source_number:
    :return:
    """
    tmp_3 = bytes(source_number & 0xFF)
    tmp_2 = bytes(source_number >> 8 & 0xFF)
    tmp_1 = bytes(source_number >> 16 & 0xFF)
    tmp_0 = bytes(source_number >> 24 & 0xFF)
    order_bytes = tmp_3
    order_bytes = tmp_2 + order_bytes
    order_bytes = tmp_1 + order_bytes
    order_bytes = tmp_0 + order_bytes
    return order_bytes


def opt_aes_decrypt(app_secret, encrypt):
    """
    进行aes解密
    :param app_secret:
    :param encrypt: 密文
    :return:
    """
    aes_key = build_aes_key_from_secret(app_secret) + "="
    key = base64.b64decode(aes_key)
    base_text = base64.b64decode(encrypt)  # 没有用到16进制转码的我们需要base64 ,这个地方小坑
    cryptor = AES.new(key, AES.MODE_CBC, key[:16])
    plain_text = cryptor.decrypt(base_text)
    pad_index = plain_text[len(plain_text) - 1]
    if pad_index < 1 or pad_index > 32:
        pad_index = 0
    plain_text = plain_text[0:len(plain_text) - pad_index]
    # 分离16位随机字符串, 网络字节序和corpId
    network_order = plain_text[16:20]
    xmlLength = recover_network_bytes_order(network_order)
    plain_info = plain_text[20:20 + xmlLength]
    suit_key = plain_text[20 + xmlLength:]
    return {"event_info": plain_info.decode("utf-8"), "suit_key": suit_key.decode("utf-8")}


def get_random_str():
    """
    获取随机数
    :return:
    """
    base = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    random.randint(0, len(base))
    ran_str = ""
    for i in range(0, 16):
        ran_str = ran_str + base[(random.randint(0, len(base) - 1))]
    return ran_str


def recover_network_bytes_order(order_bytes):
    """
    还原4个字节的网络字节序
    :param order_bytes:
    :return:
    """
    source_number = 0
    for i in range(0, 4):
        source_number <<= 8
        source_number |= int(order_bytes[i]) & 0xff
    return source_number


def build_aes_key_from_secret(app_secret):
    """
    通过AppSecret获取aesKey
    :param app_secret: AppSecret
    :return:
    """
    encoding_aes_key = re.sub('-', '', app_secret)
    if len(encoding_aes_key) == 43:
        return encoding_aes_key
    if len(encoding_aes_key) > 43:
        return encoding_aes_key[:43]
    while len(encoding_aes_key) < 43:
        encoding_aes_key = encoding_aes_key + "0"
    return encoding_aes_key
