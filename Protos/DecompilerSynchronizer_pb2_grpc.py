# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import DecompilerSynchronizer_pb2 as DecompilerSynchronizer__pb2


class DecompilerSynchronizerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Initialize = channel.unary_unary(
                '/DecompilerSynchronizer/Initialize',
                request_serializer=DecompilerSynchronizer__pb2.EmptyRequestReply.SerializeToString,
                response_deserializer=DecompilerSynchronizer__pb2.EmptyRequestReply.FromString,
                )
        self.GetDecompiledModuleName = channel.unary_unary(
                '/DecompilerSynchronizer/GetDecompiledModuleName',
                request_serializer=DecompilerSynchronizer__pb2.EmptyRequestReply.SerializeToString,
                response_deserializer=DecompilerSynchronizer__pb2.DecompiledModuleNameReply.FromString,
                )
        self.GeneratePdbForCallstack = channel.unary_unary(
                '/DecompilerSynchronizer/GeneratePdbForCallstack',
                request_serializer=DecompilerSynchronizer__pb2.GeneratePdbForCallstackRequest.SerializeToString,
                response_deserializer=DecompilerSynchronizer__pb2.GeneratePdbForCallstackReply.FromString,
                )
        self.GetPdbPath = channel.unary_unary(
                '/DecompilerSynchronizer/GetPdbPath',
                request_serializer=DecompilerSynchronizer__pb2.EmptyRequestReply.SerializeToString,
                response_deserializer=DecompilerSynchronizer__pb2.GetPdbPathReply.FromString,
                )
        self.ShouldUpdateSymbols = channel.unary_unary(
                '/DecompilerSynchronizer/ShouldUpdateSymbols',
                request_serializer=DecompilerSynchronizer__pb2.EmptyRequestReply.SerializeToString,
                response_deserializer=DecompilerSynchronizer__pb2.ShouldUpdateSymbolsReply.FromString,
                )


class DecompilerSynchronizerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Initialize(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDecompiledModuleName(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GeneratePdbForCallstack(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPdbPath(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ShouldUpdateSymbols(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DecompilerSynchronizerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Initialize': grpc.unary_unary_rpc_method_handler(
                    servicer.Initialize,
                    request_deserializer=DecompilerSynchronizer__pb2.EmptyRequestReply.FromString,
                    response_serializer=DecompilerSynchronizer__pb2.EmptyRequestReply.SerializeToString,
            ),
            'GetDecompiledModuleName': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDecompiledModuleName,
                    request_deserializer=DecompilerSynchronizer__pb2.EmptyRequestReply.FromString,
                    response_serializer=DecompilerSynchronizer__pb2.DecompiledModuleNameReply.SerializeToString,
            ),
            'GeneratePdbForCallstack': grpc.unary_unary_rpc_method_handler(
                    servicer.GeneratePdbForCallstack,
                    request_deserializer=DecompilerSynchronizer__pb2.GeneratePdbForCallstackRequest.FromString,
                    response_serializer=DecompilerSynchronizer__pb2.GeneratePdbForCallstackReply.SerializeToString,
            ),
            'GetPdbPath': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPdbPath,
                    request_deserializer=DecompilerSynchronizer__pb2.EmptyRequestReply.FromString,
                    response_serializer=DecompilerSynchronizer__pb2.GetPdbPathReply.SerializeToString,
            ),
            'ShouldUpdateSymbols': grpc.unary_unary_rpc_method_handler(
                    servicer.ShouldUpdateSymbols,
                    request_deserializer=DecompilerSynchronizer__pb2.EmptyRequestReply.FromString,
                    response_serializer=DecompilerSynchronizer__pb2.ShouldUpdateSymbolsReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'DecompilerSynchronizer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DecompilerSynchronizer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Initialize(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DecompilerSynchronizer/Initialize',
            DecompilerSynchronizer__pb2.EmptyRequestReply.SerializeToString,
            DecompilerSynchronizer__pb2.EmptyRequestReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDecompiledModuleName(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DecompilerSynchronizer/GetDecompiledModuleName',
            DecompilerSynchronizer__pb2.EmptyRequestReply.SerializeToString,
            DecompilerSynchronizer__pb2.DecompiledModuleNameReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GeneratePdbForCallstack(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DecompilerSynchronizer/GeneratePdbForCallstack',
            DecompilerSynchronizer__pb2.GeneratePdbForCallstackRequest.SerializeToString,
            DecompilerSynchronizer__pb2.GeneratePdbForCallstackReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPdbPath(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DecompilerSynchronizer/GetPdbPath',
            DecompilerSynchronizer__pb2.EmptyRequestReply.SerializeToString,
            DecompilerSynchronizer__pb2.GetPdbPathReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ShouldUpdateSymbols(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DecompilerSynchronizer/ShouldUpdateSymbols',
            DecompilerSynchronizer__pb2.EmptyRequestReply.SerializeToString,
            DecompilerSynchronizer__pb2.ShouldUpdateSymbolsReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
