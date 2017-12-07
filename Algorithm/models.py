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
            o_algo.save()
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


class AlgoServer(models.Model):
    ip = models.GenericIPAddressField(
        default=None,
    )
    port = models.IntegerField(
        default=0,
    )

    @classmethod
    def create(cls, ip, port):
        try:
            o_algo_server = cls(ip=ip, port=port)
        except:
            return Ret(Error.ERROR_CREATE_ALGO_SERVER)
        return o_algo_server

    def to_dict(self):
        return dict(id=self.pk, ip=self.ip, port=self.port)

    @staticmethod
    def get_server_list(raw=False):
        _server_list = AlgoServer.objects.all()
        if raw:
            return Ret(Error.OK, _server_list)
        print('len', len(_server_list))
        server_list = []
        for o_server in _server_list:
            server_list.append(o_server.to_dict())
        return Ret(Error.OK, server_list)

    @staticmethod
    def choose_server():
        ret = AlgoServer.get_server_list(raw=True)
        if ret.error is not Error.OK:
            return Ret(ret.error)
        server_list = ret.body
        if len(server_list) == 0:
            return Ret(Error.NO_SERVER_AVAILABLE)
        return Ret(Error.OK, server_list[0])
