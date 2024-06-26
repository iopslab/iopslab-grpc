# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from entity import model_service_v2_request_pb2 as entity_dot_model__service__v2__request__pb2
from entity import response_pb2 as entity_dot_response__pb2


class ModelBaseServiceV2Stub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetById = channel.unary_unary(
                '/grpc.ModelBaseServiceV2/GetById',
                request_serializer=entity_dot_model__service__v2__request__pb2.ModelServiceV2GetByIdRequest.SerializeToString,
                response_deserializer=entity_dot_response__pb2.Response.FromString,
                )
        self.GetOne = channel.unary_unary(
                '/grpc.ModelBaseServiceV2/GetOne',
                request_serializer=entity_dot_model__service__v2__request__pb2.ModelServiceV2GetOneRequest.SerializeToString,
                response_deserializer=entity_dot_response__pb2.Response.FromString,
                )
        self.GetMany = channel.unary_unary(
                '/grpc.ModelBaseServiceV2/GetMany',
                request_serializer=entity_dot_model__service__v2__request__pb2.ModelServiceV2GetManyRequest.SerializeToString,
                response_deserializer=entity_dot_response__pb2.Response.FromString,
                )
        self.DeleteById = channel.unary_unary(
                '/grpc.ModelBaseServiceV2/DeleteById',
                request_serializer=entity_dot_model__service__v2__request__pb2.ModelServiceV2DeleteByIdRequest.SerializeToString,
                response_deserializer=entity_dot_response__pb2.Response.FromString,
                )
        self.DeleteOne = channel.unary_unary(
                '/grpc.ModelBaseServiceV2/DeleteOne',
                request_serializer=entity_dot_model__service__v2__request__pb2.ModelServiceV2DeleteOneRequest.SerializeToString,
                response_deserializer=entity_dot_response__pb2.Response.FromString,
                )
        self.DeleteMany = channel.unary_unary(
                '/grpc.ModelBaseServiceV2/DeleteMany',
                request_serializer=entity_dot_model__service__v2__request__pb2.ModelServiceV2DeleteManyRequest.SerializeToString,
                response_deserializer=entity_dot_response__pb2.Response.FromString,
                )
        self.UpdateById = channel.unary_unary(
                '/grpc.ModelBaseServiceV2/UpdateById',
                request_serializer=entity_dot_model__service__v2__request__pb2.ModelServiceV2UpdateByIdRequest.SerializeToString,
                response_deserializer=entity_dot_response__pb2.Response.FromString,
                )
        self.UpdateOne = channel.unary_unary(
                '/grpc.ModelBaseServiceV2/UpdateOne',
                request_serializer=entity_dot_model__service__v2__request__pb2.ModelServiceV2UpdateOneRequest.SerializeToString,
                response_deserializer=entity_dot_response__pb2.Response.FromString,
                )
        self.UpdateMany = channel.unary_unary(
                '/grpc.ModelBaseServiceV2/UpdateMany',
                request_serializer=entity_dot_model__service__v2__request__pb2.ModelServiceV2UpdateManyRequest.SerializeToString,
                response_deserializer=entity_dot_response__pb2.Response.FromString,
                )
        self.ReplaceById = channel.unary_unary(
                '/grpc.ModelBaseServiceV2/ReplaceById',
                request_serializer=entity_dot_model__service__v2__request__pb2.ModelServiceV2ReplaceByIdRequest.SerializeToString,
                response_deserializer=entity_dot_response__pb2.Response.FromString,
                )
        self.ReplaceOne = channel.unary_unary(
                '/grpc.ModelBaseServiceV2/ReplaceOne',
                request_serializer=entity_dot_model__service__v2__request__pb2.ModelServiceV2ReplaceOneRequest.SerializeToString,
                response_deserializer=entity_dot_response__pb2.Response.FromString,
                )
        self.InsertOne = channel.unary_unary(
                '/grpc.ModelBaseServiceV2/InsertOne',
                request_serializer=entity_dot_model__service__v2__request__pb2.ModelServiceV2InsertOneRequest.SerializeToString,
                response_deserializer=entity_dot_response__pb2.Response.FromString,
                )
        self.InsertMany = channel.unary_unary(
                '/grpc.ModelBaseServiceV2/InsertMany',
                request_serializer=entity_dot_model__service__v2__request__pb2.ModelServiceV2InsertManyRequest.SerializeToString,
                response_deserializer=entity_dot_response__pb2.Response.FromString,
                )
        self.Count = channel.unary_unary(
                '/grpc.ModelBaseServiceV2/Count',
                request_serializer=entity_dot_model__service__v2__request__pb2.ModelServiceV2CountRequest.SerializeToString,
                response_deserializer=entity_dot_response__pb2.Response.FromString,
                )


class ModelBaseServiceV2Servicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetOne(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMany(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteOne(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteMany(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateOne(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateMany(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReplaceById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReplaceOne(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def InsertOne(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def InsertMany(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Count(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ModelBaseServiceV2Servicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetById': grpc.unary_unary_rpc_method_handler(
                    servicer.GetById,
                    request_deserializer=entity_dot_model__service__v2__request__pb2.ModelServiceV2GetByIdRequest.FromString,
                    response_serializer=entity_dot_response__pb2.Response.SerializeToString,
            ),
            'GetOne': grpc.unary_unary_rpc_method_handler(
                    servicer.GetOne,
                    request_deserializer=entity_dot_model__service__v2__request__pb2.ModelServiceV2GetOneRequest.FromString,
                    response_serializer=entity_dot_response__pb2.Response.SerializeToString,
            ),
            'GetMany': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMany,
                    request_deserializer=entity_dot_model__service__v2__request__pb2.ModelServiceV2GetManyRequest.FromString,
                    response_serializer=entity_dot_response__pb2.Response.SerializeToString,
            ),
            'DeleteById': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteById,
                    request_deserializer=entity_dot_model__service__v2__request__pb2.ModelServiceV2DeleteByIdRequest.FromString,
                    response_serializer=entity_dot_response__pb2.Response.SerializeToString,
            ),
            'DeleteOne': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteOne,
                    request_deserializer=entity_dot_model__service__v2__request__pb2.ModelServiceV2DeleteOneRequest.FromString,
                    response_serializer=entity_dot_response__pb2.Response.SerializeToString,
            ),
            'DeleteMany': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteMany,
                    request_deserializer=entity_dot_model__service__v2__request__pb2.ModelServiceV2DeleteManyRequest.FromString,
                    response_serializer=entity_dot_response__pb2.Response.SerializeToString,
            ),
            'UpdateById': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateById,
                    request_deserializer=entity_dot_model__service__v2__request__pb2.ModelServiceV2UpdateByIdRequest.FromString,
                    response_serializer=entity_dot_response__pb2.Response.SerializeToString,
            ),
            'UpdateOne': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateOne,
                    request_deserializer=entity_dot_model__service__v2__request__pb2.ModelServiceV2UpdateOneRequest.FromString,
                    response_serializer=entity_dot_response__pb2.Response.SerializeToString,
            ),
            'UpdateMany': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateMany,
                    request_deserializer=entity_dot_model__service__v2__request__pb2.ModelServiceV2UpdateManyRequest.FromString,
                    response_serializer=entity_dot_response__pb2.Response.SerializeToString,
            ),
            'ReplaceById': grpc.unary_unary_rpc_method_handler(
                    servicer.ReplaceById,
                    request_deserializer=entity_dot_model__service__v2__request__pb2.ModelServiceV2ReplaceByIdRequest.FromString,
                    response_serializer=entity_dot_response__pb2.Response.SerializeToString,
            ),
            'ReplaceOne': grpc.unary_unary_rpc_method_handler(
                    servicer.ReplaceOne,
                    request_deserializer=entity_dot_model__service__v2__request__pb2.ModelServiceV2ReplaceOneRequest.FromString,
                    response_serializer=entity_dot_response__pb2.Response.SerializeToString,
            ),
            'InsertOne': grpc.unary_unary_rpc_method_handler(
                    servicer.InsertOne,
                    request_deserializer=entity_dot_model__service__v2__request__pb2.ModelServiceV2InsertOneRequest.FromString,
                    response_serializer=entity_dot_response__pb2.Response.SerializeToString,
            ),
            'InsertMany': grpc.unary_unary_rpc_method_handler(
                    servicer.InsertMany,
                    request_deserializer=entity_dot_model__service__v2__request__pb2.ModelServiceV2InsertManyRequest.FromString,
                    response_serializer=entity_dot_response__pb2.Response.SerializeToString,
            ),
            'Count': grpc.unary_unary_rpc_method_handler(
                    servicer.Count,
                    request_deserializer=entity_dot_model__service__v2__request__pb2.ModelServiceV2CountRequest.FromString,
                    response_serializer=entity_dot_response__pb2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'grpc.ModelBaseServiceV2', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ModelBaseServiceV2(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.ModelBaseServiceV2/GetById',
            entity_dot_model__service__v2__request__pb2.ModelServiceV2GetByIdRequest.SerializeToString,
            entity_dot_response__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetOne(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.ModelBaseServiceV2/GetOne',
            entity_dot_model__service__v2__request__pb2.ModelServiceV2GetOneRequest.SerializeToString,
            entity_dot_response__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetMany(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.ModelBaseServiceV2/GetMany',
            entity_dot_model__service__v2__request__pb2.ModelServiceV2GetManyRequest.SerializeToString,
            entity_dot_response__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.ModelBaseServiceV2/DeleteById',
            entity_dot_model__service__v2__request__pb2.ModelServiceV2DeleteByIdRequest.SerializeToString,
            entity_dot_response__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteOne(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.ModelBaseServiceV2/DeleteOne',
            entity_dot_model__service__v2__request__pb2.ModelServiceV2DeleteOneRequest.SerializeToString,
            entity_dot_response__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteMany(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.ModelBaseServiceV2/DeleteMany',
            entity_dot_model__service__v2__request__pb2.ModelServiceV2DeleteManyRequest.SerializeToString,
            entity_dot_response__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.ModelBaseServiceV2/UpdateById',
            entity_dot_model__service__v2__request__pb2.ModelServiceV2UpdateByIdRequest.SerializeToString,
            entity_dot_response__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateOne(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.ModelBaseServiceV2/UpdateOne',
            entity_dot_model__service__v2__request__pb2.ModelServiceV2UpdateOneRequest.SerializeToString,
            entity_dot_response__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateMany(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.ModelBaseServiceV2/UpdateMany',
            entity_dot_model__service__v2__request__pb2.ModelServiceV2UpdateManyRequest.SerializeToString,
            entity_dot_response__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReplaceById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.ModelBaseServiceV2/ReplaceById',
            entity_dot_model__service__v2__request__pb2.ModelServiceV2ReplaceByIdRequest.SerializeToString,
            entity_dot_response__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReplaceOne(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.ModelBaseServiceV2/ReplaceOne',
            entity_dot_model__service__v2__request__pb2.ModelServiceV2ReplaceOneRequest.SerializeToString,
            entity_dot_response__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def InsertOne(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.ModelBaseServiceV2/InsertOne',
            entity_dot_model__service__v2__request__pb2.ModelServiceV2InsertOneRequest.SerializeToString,
            entity_dot_response__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def InsertMany(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.ModelBaseServiceV2/InsertMany',
            entity_dot_model__service__v2__request__pb2.ModelServiceV2InsertManyRequest.SerializeToString,
            entity_dot_response__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Count(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.ModelBaseServiceV2/Count',
            entity_dot_model__service__v2__request__pb2.ModelServiceV2CountRequest.SerializeToString,
            entity_dot_response__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
