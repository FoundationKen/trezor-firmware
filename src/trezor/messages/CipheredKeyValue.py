# Automatically generated by pb2py
import protobuf as p


class CipheredKeyValue(p.MessageType):
    FIELDS = {
        1: ('value', p.BytesType, 0),
    }
    MESSAGE_WIRE_TYPE = 48

    def __init__(
        self,
        value: bytes = None,
        **kwargs,
    ):
        self.value = value
        p.MessageType.__init__(self, **kwargs)