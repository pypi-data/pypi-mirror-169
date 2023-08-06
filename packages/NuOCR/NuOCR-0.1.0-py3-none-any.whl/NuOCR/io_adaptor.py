from .gRPC_proto.io_adaptors_APIs_proto import io_adaptors_pb2, io_adaptors_pb2_grpc


class FTP:
    def __init__(self, channel, metadata, host, port, username, password, isSecure=False):
        self.stub = io_adaptors_pb2_grpc.IOAdaptorControllerStub(channel)
        self.metadata = metadata
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.isSecure = isSecure

    def inbound(self, remoteFolder, remoteFilename='', subscriberId='', base64=''):
        response = self.stub.FTPInBound(
            io_adaptors_pb2.FTPRequest(host=self.host, port=self.port, username=self.username, password=self.password,
                                       isSecure=self.isSecure, subscriberId=subscriberId, remoteFolder=remoteFolder,
                                       remoteFilename=remoteFilename, base64=base64), metadata=self.metadata)
        return response

    def outbound(self, base64, remoteFolder, remoteFilename, subscriberId=''):
        response = self.stub.FTPOutBound(
            io_adaptors_pb2.FTPRequest(host=self.host, port=self.port, username=self.username, password=self.password,
                                       isSecure=self.isSecure, subscriberId=subscriberId, remoteFolder=remoteFolder,
                                       remoteFilename=remoteFilename, base64=base64), metadata=self.metadata)
        return response.status


class S3:
    def __init__(self, channel, metadata, subscriberId, regionName, accessKey, secretKey, bucketName):
        self.stub = io_adaptors_pb2_grpc.IOAdaptorControllerStub(channel)
        self.metadata = metadata
        self.subscriberId = subscriberId
        self.regionName = regionName
        self.accessKey = accessKey
        self.secretKey = secretKey
        self.bucketName = bucketName

    def inbound(self, folderName, filename='', base64='', localFilename=''):
        response = self.stub.S3InBound(
            io_adaptors_pb2.S3Request(subscriberId=self.subscriberId, regionName=self.regionName,
                                      accessKey=self.accessKey, secretKey=self.secretKey, bucketName=self.bucketName,
                                      folderName=folderName, filename=filename, base64=base64,
                                      localFilename=localFilename), metadata=self.metadata
        )
        return response

    def outbound(self, base64, filename, folderName, localFilename=''):
        response = self.stub.S3OutBound(
            io_adaptors_pb2.S3Request(subscriberId=self.subscriberId, regionName=self.regionName,
                                      accessKey=self.accessKey, secretKey=self.secretKey, bucketName=self.bucketName,
                                      folderName=folderName, filename=filename, base64=base64,
                                      localFilename=localFilename), metadata=self.metadata
        )
        return response.status
