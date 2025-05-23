# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import matrix_pb2 as matrix__pb2


class MatrixServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.MultiplyMatrices = channel.unary_unary(
                '/matrix.MatrixService/MultiplyMatrices',
                request_serializer=matrix__pb2.MatrixRequest.SerializeToString,
                response_deserializer=matrix__pb2.MatrixResponse.FromString,
                )


class MatrixServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def MultiplyMatrices(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MatrixServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'MultiplyMatrices': grpc.unary_unary_rpc_method_handler(
                    servicer.MultiplyMatrices,
                    request_deserializer=matrix__pb2.MatrixRequest.FromString,
                    response_serializer=matrix__pb2.MatrixResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'matrix.MatrixService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MatrixService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def MultiplyMatrices(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/matrix.MatrixService/MultiplyMatrices',
            matrix__pb2.MatrixRequest.SerializeToString,
            matrix__pb2.MatrixResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
