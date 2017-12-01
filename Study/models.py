from django.db import models

from base.error import Error
from base.response import Ret


class Study(models.Model):
    L = {

    }

    STATUS_READY = 0
    STATUS_RUNNING = 1
    STATUS_FINISH = 2

    STATUS_TUPLE = (
        (STATUS_READY, "study is ready"),
        (STATUS_RUNNING, "study is running"),
        (STATUS_FINISH, "study is finished"),
    )
    config = models.TextField()
    r_user = models.ForeignKey(
        'User.User',
    )
    r_algo = models.ForeignKey(
        'Algorithm.Algorithm',
    )
    status = models.IntegerField(
        choices=STATUS_TUPLE,
        default=STATUS_READY,
    )

    @classmethod
    def create(cls, o_user, o_algo, config):
        try:
            o_study = cls(
                config=config,
                r_user=o_user,
                r_algo=o_algo,
                status=Study.STATUS_READY,
            )
        except:
            return Ret(Error.ERROR_CREATE_STUDY)
        return Ret(Error.OK, o_study)


class Trail(models.Model):
    L = {

    }
    r_study = models.ForeignKey(
        'Study.Study',
    )
    trail = models.TextField()
    metric = models.TextField()

    @classmethod
    def create(cls, o_study, trail, metric):
        try:
            o_trail = cls(
                r_study=o_study,
                trail=trail,
                metric=metric,
            )
        except:
            return Ret(Error.ERROR_CREATE_TRAIL)
        return Ret(Error.OK, o_trail)
