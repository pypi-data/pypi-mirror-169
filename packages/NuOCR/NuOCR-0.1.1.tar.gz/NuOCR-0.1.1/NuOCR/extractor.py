import grpc, json
from .gRPC_proto.extractor_APIs_proto import extractor_pb2, extractor_pb2_grpc


class Extractor:
    def __init__(self, channel, metadata):
        self.stub = extractor_pb2_grpc.ExtractorControllerStub(channel)
        self.metadata = metadata

    def form_recognizer(self, base64, extractionType, mimeType="application/pdf", table=True, rawJson=False,
                        pages=None, subscriberId='', language=''):
        try:
            request = extractor_pb2.FormRequest(base64=base64,
                                                extractionType=extractionType,
                                                mimeType=mimeType,
                                                table=table,
                                                rawJson=rawJson,
                                                pages=pages,
                                                subscriberId=subscriberId,
                                                language=language)
            response = self.stub.FormRecognition(request, metadata=self.metadata)
            return json.loads(response.body)
        except grpc.RpcError as e:
            raise Exception('Error ' + str(e.code()) + ': ' + str(e.details()))

    def doc_recognizer(self, base64, extractionType, mimeType="application/pdf", extractionHints=False,
                       rawJson=False, subscriberId=''):
        try:
            request = extractor_pb2.DocRequest(
                base64=base64,
                extractionType=extractionType,
                mimeType=mimeType,
                extractionHints=extractionHints,
                rawJson=rawJson,
                subscriberId=subscriberId
            )
            response = self.stub.DocAI(request, metadata=self.metadata)
            return json.loads(response.body)
        except grpc.RpcError as e:
            raise Exception('Error ' + str(e.code()) + ': ' + str(e.details()))
