# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from entity import request_pb2 as entity_dot_request__pb2
from entity import response_pb2 as entity_dot_response__pb2
from entity import stream_message_pb2 as entity_dot_stream__message__pb2


class NodeServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Register = channel.unary_unary(
                '/grpc.NodeService/Register',
                request_serializer=entity_dot_request__pb2.Request.SerializeToString,
                response_deserializer=entity_dot_response__pb2.Response.FromString,
                )
        self.SendHeartbeat = channel.unary_unary(
                '/grpc.NodeService/SendHeartbeat',
                request_serializer=entity_dot_request__pb2.Request.SerializeToString,
                response_deserializer=entity_dot_response__pb2.Response.FromString,
                )
        self.Ping = channel.unary_unary(
                '/grpc.NodeService/Ping',
                request_serializer=entity_dot_request__pb2.Request.SerializeToString,
                response_deserializer=entity_dot_response__pb2.Response.FromString,
                )
        self.Subscribe = channel.unary_stream(
                '/grpc.NodeService/Subscribe',
                request_serializer=entity_dot_request__pb2.Request.SerializeToString,
                response_deserializer=entity_dot_stream__message__pb2.StreamMessage.FromString,
                )
        self.Unsubscribe = channel.unary_unary(
                '/grpc.NodeService/Unsubscribe',
                request_serializer=entity_dot_request__pb2.Request.SerializeToString,
                response_deserializer=entity_dot_response__pb2.Response.FromString,
                )


class NodeServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Register(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendHeartbeat(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Ping(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Subscribe(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Unsubscribe(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NodeServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Register': grpc.unary_unary_rpc_method_handler(
                    servicer.Register,
                    request_deserializer=entity_dot_request__pb2.Request.FromString,
                    response_serializer=entity_dot_response__pb2.Response.SerializeToString,
            ),
            'SendHeartbeat': grpc.unary_unary_rpc_method_handler(
                    servicer.SendHeartbeat,
                    request_deserializer=entity_dot_request__pb2.Request.FromString,
                    response_serializer=entity_dot_response__pb2.Response.SerializeToString,
            ),
            'Ping': grpc.unary_unary_rpc_method_handler(
                    servicer.Ping,
                    request_deserializer=entity_dot_request__pb2.Request.FromString,
                    response_serializer=entity_dot_response__pb2.Response.SerializeToString,
            ),
            'Subscribe': grpc.unary_stream_rpc_method_handler(
                    servicer.Subscribe,
                    request_deserializer=entity_dot_request__pb2.Request.FromString,
                    response_serializer=entity_dot_stream__message__pb2.StreamMessage.SerializeToString,
            ),
            'Unsubscribe': grpc.unary_unary_rpc_method_handler(
                    servicer.Unsubscribe,
                    request_deserializer=entity_dot_request__pb2.Request.FromString,
                    response_serializer=entity_dot_response__pb2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'grpc.NodeService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class NodeService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Register(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.NodeService/Register',
            entity_dot_request__pb2.Request.SerializeToString,
            entity_dot_response__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendHeartbeat(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.NodeService/SendHeartbeat',
            entity_dot_request__pb2.Request.SerializeToString,
            entity_dot_response__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Ping(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.NodeService/Ping',
            entity_dot_request__pb2.Request.SerializeToString,
            entity_dot_response__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Subscribe(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/grpc.NodeService/Subscribe',
            entity_dot_request__pb2.Request.SerializeToString,
            entity_dot_stream__message__pb2.StreamMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Unsubscribe(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.NodeService/Unsubscribe',
            entity_dot_request__pb2.Request.SerializeToString,
            entity_dot_response__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
