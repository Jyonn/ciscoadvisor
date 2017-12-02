from django.db import models

from base.error import Error
from base.response import Ret


class User(models.Model):
    L = {
        'username': 32,
        'password': 32,
    }
    username = models.CharField(
        max_length=L['username'],
        unique=True,
    )
    password = models.CharField(
        max_length=L['password'],
    )

    @staticmethod
    def _hash(s):
        import hashlib
        sha = hashlib.sha1()
        sha.update(s.encode())
        return sha.hexdigest()

    @classmethod
    def create(cls, username, password):
        ret = User.get_user_by_username(username)
        if ret.error is Error.OK:
            return Ret(Error.EXIST_USERNAME)

        try:
            o_user = cls(
                username=username,
                password=User._hash(password),
            )
        except:
            return Ret(Error.ERROR_CREATE_USER)
        return Ret(Error.OK, o_user)

    @staticmethod
    def authenticate(username, password):
        ret = User.get_user_by_username(username)
        if ret.error is not Error.OK:
            return Ret(ret.error)
        o_user = ret.body

        if o_user.password == User._hash(password):
            return Ret(Error.OK, o_user)
        return Ret(Error.ERROR_PASSWORD)

    @staticmethod
    def get_user_by_username(username):
        try:
            o_user = User.objects.get(username=username)
        except:
            return Ret(Error.NOT_FOUND_USERNAME)
        return Ret(Error.OK, o_user)

    def to_dict(self):
        return dict(
            user_id=self.pk,
            username=self.username,
        )
