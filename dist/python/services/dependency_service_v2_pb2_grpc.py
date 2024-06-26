# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from entity import dependencies_service_v2_request_pb2 as entity_dot_dependencies__service__v2__request__pb2
from entity import response_pb2 as entity_dot_response__pb2


class DependencyServiceV2Stub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Connect = channel.stream_unary(
                '/grpc.DependencyServiceV2/Connect',
                request_serializer=entity_dot_dependencies__service__v2__request__pb2.DependenciesServiceV2ConnectRequest.SerializeToString,
                response_deserializer=entity_dot_response__pb2.Response.FromString,
                )
        self.Sync = channel.unary_unary(
                '/grpc.DependencyServiceV2/Sync',
                request_serializer=entity_dot_dependencies__service__v2__request__pb2.DependenciesServiceV2SyncRequest.SerializeToString,
                response_deserializer=entity_dot_response__pb2.Response.FromString,
                )
        self.Install = channel.stream_stream(
                '/grpc.DependencyServiceV2/Install',
                request_serializer=entity_dot_dependencies__service__v2__request__pb2.DependenciesServiceV2InstallRequest.SerializeToString,
                response_deserializer=entity_dot_response__pb2.Response.FromString,
                )
        self.UninstallDependencies = channel.stream_stream(
                '/grpc.DependencyServiceV2/UninstallDependencies',
                request_serializer=entity_dot_dependencies__service__v2__request__pb2.DependenciesServiceV2UninstallRequest.SerializeToString,
                response_deserializer=entity_dot_response__pb2.Response.FromString,
                )


class DependencyServiceV2Servicer(object):
    """Missing associated documentation comment in .proto file."""

    def Connect(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Sync(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Install(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UninstallDependencies(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DependencyServiceV2Servicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Connect': grpc.stream_unary_rpc_method_handler(
                    servicer.Connect,
                    request_deserializer=entity_dot_dependencies__service__v2__request__pb2.DependenciesServiceV2ConnectRequest.FromString,
                    response_serializer=entity_dot_response__pb2.Response.SerializeToString,
            ),
            'Sync': grpc.unary_unary_rpc_method_handler(
                    servicer.Sync,
                    request_deserializer=entity_dot_dependencies__service__v2__request__pb2.DependenciesServiceV2SyncRequest.FromString,
                    response_serializer=entity_dot_response__pb2.Response.SerializeToString,
            ),
            'Install': grpc.stream_stream_rpc_method_handler(
                    servicer.Install,
                    request_deserializer=entity_dot_dependencies__service__v2__request__pb2.DependenciesServiceV2InstallRequest.FromString,
                    response_serializer=entity_dot_response__pb2.Response.SerializeToString,
            ),
            'UninstallDependencies': grpc.stream_stream_rpc_method_handler(
                    servicer.UninstallDependencies,
                    request_deserializer=entity_dot_dependencies__service__v2__request__pb2.DependenciesServiceV2UninstallRequest.FromString,
                    response_serializer=entity_dot_response__pb2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'grpc.DependencyServiceV2', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DependencyServiceV2(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Connect(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/grpc.DependencyServiceV2/Connect',
            entity_dot_dependencies__service__v2__request__pb2.DependenciesServiceV2ConnectRequest.SerializeToString,
            entity_dot_response__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Sync(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.DependencyServiceV2/Sync',
            entity_dot_dependencies__service__v2__request__pb2.DependenciesServiceV2SyncRequest.SerializeToString,
            entity_dot_response__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Install(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/grpc.DependencyServiceV2/Install',
            entity_dot_dependencies__service__v2__request__pb2.DependenciesServiceV2InstallRequest.SerializeToString,
            entity_dot_response__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UninstallDependencies(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/grpc.DependencyServiceV2/UninstallDependencies',
            entity_dot_dependencies__service__v2__request__pb2.DependenciesServiceV2UninstallRequest.SerializeToString,
            entity_dot_response__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
