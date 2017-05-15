from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class LenTests(TranspileTestCase):
    pass


class BuiltinLenFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["len"]

    not_implemented = [
        'test_bool',
        'test_bytes',
        'test_bytearray',
        'test_class',
        'test_complex',
        'test_dict',
        'test_frozenset',
        'test_None',
        'test_NotImplemented',
        'test_set',
        'test_slice',
    ]
