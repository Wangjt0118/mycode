import rsa
import base64

private_key = """-----BEGIN RSA PRIVATE KEY-----
MIICXAIBAAKBgQC/cQ2XqNR7jbMrfVyHsQRyw670Cf+WIWtrg7Xs9IO4qaLbETnv
QPwzmQIHykt1Daea7uuo4qKRv3GnVxJzvt4hwql7krN1mBNDMribupN7S9LtA1bw
I2uMuvrm3BNxB9ZSKJvanLBseu61XVtDexpZMQ+iA7mHBa2jDHlsRDxc8QIDAQAB
AoGAV1UylzH8pNSSnM9Wi8w0NEqSoF+DSjC6uVRfhNZS1MYGNhuYq02g/8TYSUd+
vspY4HQH64ZgFU8ZgPZWw5iZ6lCEqYZCOlfc/iEdpXNRnvv+fAIgh14vmLSYgoAI
HT2HlQ0PeZtyPhbA0yMgc5jh9B3tUqokp3MP+Ta36YCarEECQQDptBNdlksexoYV
G8OrkoM40KHb9EPuZZPK93HkcMn8d0Chkp25CL4PtVvBYG8/JlC7PotEEPqUWsYL
6+ocVkL5AkEA0bTIpEKjzGO/MguW6eRtRpHZBkb+YtfCoY0lEojBqRKdjF/uBvXf
Idv5cREg9kPYpZ5kdcSRwQWgBWGN1LxvuQJALyDBRv4n5+zg3SDcNJ03GR35hgGc
MVcKlsOPlCGqmd7yiaKna8j3ivNnrXdk97ciUKAsNW23GnOzvHO2okBDAQJAGooM
km00mZtOCSFaWgNkqPewRZEahJvVr+hS9sOD7sfCVI+Xah4XvQs/yEVorIHtmxgu
kpDr+Uei9stfzbqDUQJBAJ7UaeAYEtyK4Ufi830VuJmtYQ/zkxPIC+D6HUtM7IDD
/RnIJP1KRcJHhY7wDx9az5vxAPk8FVZfaTR6vgMTsoQ=
-----END RSA PRIVATE KEY-----"""
public_key = """-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC/cQ2XqNR7jbMrfVyHsQRyw670
Cf+WIWtrg7Xs9IO4qaLbETnvQPwzmQIHykt1Daea7uuo4qKRv3GnVxJzvt4hwql7
krN1mBNDMribupN7S9LtA1bwI2uMuvrm3BNxB9ZSKJvanLBseu61XVtDexpZMQ+i
A7mHBa2jDHlsRDxc8QIDAQAB
-----END PUBLIC KEY-----"""

string_sign_temp = 'ni hao a!!'



private_key = rsa.PrivateKey.load_pkcs1(private_key.encode())

sign = base64.b64encode(rsa.sign(string_sign_temp.encode(), private_key, 'SHA-1')).decode('utf-8')

print('get sign is :')
print(sign)

print('==' * 20)

public_key = rsa.PublicKey.load_pkcs1_openssl_pem(public_key)
# ori_str = rsa.decrypt(base64.b64decode(sign.encode('utf-8')), public_key).decode()
# print(ori_str)
print(base64.b64decode(sign.encode('utf-8')))
# r = rsa.verify(string_sign_temp, base64.b64decode(sign.encode('utf-8')), public_key)
# print(r)

print(rsa.decrypt(base64.b64decode(sign.encode('utf-8')), public_key))