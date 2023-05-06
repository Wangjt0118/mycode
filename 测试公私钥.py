# coding: utf-8

from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.asymmetric import utils
from cryptography.hazmat.primitives import serialization
import binascii

# 生成SM2密钥对
private_key = ec.generate_private_key(ec.SECP256K1())
public_key = private_key.public_key()

# 获取私钥DER编码格式的字节串，并将其转换为16进制字符串
private_key_der = private_key.private_bytes(
    encoding=serialization.Encoding.DER,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)
private_key_hex = binascii.hexlify(private_key_der)

# 获取公钥DER编码格式的字节串，并将其转换为16进制字符串
public_key_der = public_key.public_bytes(
    encoding=serialization.Encoding.DER,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)
public_key_hex = binascii.hexlify(public_key_der)

# 返回公钥和私钥的字符串表示形式
print '{{"publicKey":"{}","privateKey":"{}"}}'.format(public_key_hex, private_key_hex)


