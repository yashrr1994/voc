from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class BytearrayTests(TranspileTestCase):
    pass


class BuiltinBytearrayFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["bytearray"]

    not_implemented = [
        'test_bool',
        'test_class',
        'test_complex',
        'test_dict',
        'test_float',
        'test_frozenset',
        'test_int',
        'test_list',
        'test_None',
        'test_NotImplemented',
        'test_set',
        'test_slice',
        'test_str',
        'test_tuple',
    ]
