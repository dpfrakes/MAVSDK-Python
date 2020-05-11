# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import shell_pb2 as shell__pb2


class ShellServiceStub(object):
    """*
    Allow to communicate with the vehicle's system shell.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Send = channel.unary_unary(
                '/mavsdk.rpc.shell.ShellService/Send',
                request_serializer=shell__pb2.SendRequest.SerializeToString,
                response_deserializer=shell__pb2.SendResponse.FromString,
                )
        self.SubscribeReceive = channel.unary_stream(
                '/mavsdk.rpc.shell.ShellService/SubscribeReceive',
                request_serializer=shell__pb2.SubscribeReceiveRequest.SerializeToString,
                response_deserializer=shell__pb2.ReceiveResponse.FromString,
                )


class ShellServiceServicer(object):
    """*
    Allow to communicate with the vehicle's system shell.
    """

    def Send(self, request, context):
        """
        Send a command line.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeReceive(self, request, context):
        """
        Receive feedback from a sent command line.

        This subscription needs to be made before a command line is sent, otherwise, no response will be sent.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ShellServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Send': grpc.unary_unary_rpc_method_handler(
                    servicer.Send,
                    request_deserializer=shell__pb2.SendRequest.FromString,
                    response_serializer=shell__pb2.SendResponse.SerializeToString,
            ),
            'SubscribeReceive': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribeReceive,
                    request_deserializer=shell__pb2.SubscribeReceiveRequest.FromString,
                    response_serializer=shell__pb2.ReceiveResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'mavsdk.rpc.shell.ShellService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ShellService(object):
    """*
    Allow to communicate with the vehicle's system shell.
    """

    @staticmethod
    def Send(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mavsdk.rpc.shell.ShellService/Send',
            shell__pb2.SendRequest.SerializeToString,
            shell__pb2.SendResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubscribeReceive(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/mavsdk.rpc.shell.ShellService/SubscribeReceive',
            shell__pb2.SubscribeReceiveRequest.SerializeToString,
            shell__pb2.ReceiveResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
