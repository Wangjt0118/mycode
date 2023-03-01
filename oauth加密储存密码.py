# 使用sha1加密用户密码，以及可以使用flask框架werkzeug验证密码是否一致
password = 'sa@123'
salt = 'OKcNSTGP'
iterations = 1000


prefix = 'pbkdf2:sha1:1000'


from hashlib import pbkdf2_hmac
import binascii
ser = binascii.hexlify(pbkdf2_hmac("sha1", password.encode('utf-8'), salt.encode('utf-8'), iterations, 20)).decode()

new_ser = '{}${}${}'.format(prefix, salt, ser)
print(new_ser)




from werkzeug.security import check_password_hash

print(check_password_hash(new_ser, password))


