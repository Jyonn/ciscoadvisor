import grpc

from base.error import Error
from base.response import Ret
from gRPCapi.suggestion import suggestion_pb2
from gRPCapi.suggestion import suggestion_pb2_grpc


def run(ip, port, study_id):
    channel = grpc.insecure_channel('%s:%s' % (ip, port))
    stub = suggestion_pb2_grpc.SuggestionStub(channel)
    response = stub.GetSuggestion(suggestion_pb2.Study(study_id=study_id))
    return Ret(Error.OK, response.message)

# if __name__ == '__main__':
#     run('localhost', 10050)
