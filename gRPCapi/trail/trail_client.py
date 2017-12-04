import grpc

from base.error import Error
from base.response import Ret
from gRPCapi.trail import trail_pb2
from gRPCapi.trail import trail_pb2_grpc


def run(ip, port, data):
    channel = grpc.insecure_channel('%s:%s' % (ip, port))
    stub = trail_pb2_grpc.TrailStub(channel)
    response = stub.RunTrail(trail_pb2.Data(data=data))
    return Ret(Error.OK, response.message)

# if __name__ == '__main__':
#     run('localhost', 10050)
