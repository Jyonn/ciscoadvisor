from django.db import models

from base.error import Error
from base.response import Ret


class Algorithm(models.Model):
    L = {
        'aname': 100,
        'path': 255,
    }
    aname = models.CharField(
        max_length=L['aname'],
    )
    path = models.CharField(
        max_length=L['path'],
    )

    @classmethod
    def create(cls, aname, path):
        try:
            o_algo = cls(
                aname=aname,
                path=path,
            )
        except:
            return Ret(Error.ERROR_CREATE_ALGO)
        return Ret(Error.OK, o_algo)

    @staticmethod
    def get_algo_by_id(id):
        try:
            o_algo = Algorithm.objects.get(pk=id)
        except:
            return Ret(Error.NOT_FOUND_ALGO)
        return Ret(Error.OK, o_algo)

    def to_dict(self):
        return dict(
            algo_id=self.pk,
            name=self.aname,
        )

    @staticmethod
    def get_algo_list():
        algo_list = []
        for o_algo in Algorithm.objects.all():
            algo_list.append(o_algo.to_dict())
        return Ret(Error.OK, algo_list)
