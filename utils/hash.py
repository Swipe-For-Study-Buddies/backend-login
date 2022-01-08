import hashlib
import base64
import uuid
import bcrypt



def get_hash(password: str):
    # salt = base64.urlsafe_b64encode(uuid.uuid4().bytes).decode('UTF-8')
    # print(salt)

    # t_sha = hashlib.sha512()
    # t_sha.update(password+salt)
    # hashed_password =  base64.urlsafe_b64encode(t_sha.digest())
    # return hashed_password, salt
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password, salt), salt

