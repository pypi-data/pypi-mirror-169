from . import act_template_typed_pb2_grpc as importStub

class ActTypedService(object):

    def __init__(self, router):
        self.connector = router.get_connection(ActTypedService, importStub.ActTypedStub)

    def placeOrderFIX(self, request, timeout=None, properties=None):
        return self.connector.create_request('placeOrderFIX', request, timeout, properties)