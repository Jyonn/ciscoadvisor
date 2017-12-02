import grpc

from gRPCapi.suggestion import suggestion_pb2
from gRPCapi.suggestion import suggestion_pb2_grpc


def run(ip, port, o_study):
    channel = grpc.insecure_channel('%s:%s' % (ip, port))
    stub = suggestion_pb2_grpc.SuggestionStub(channel)
    response = stub.GetSuggestion(suggestion_pb2.Study(study_id=12))
    return response.message

# if __name__ == '__main__':
#     run('localhost', 10050)
