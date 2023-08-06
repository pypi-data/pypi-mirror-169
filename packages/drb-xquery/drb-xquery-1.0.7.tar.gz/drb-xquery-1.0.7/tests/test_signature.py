import unittest

from drb.utils.logical_node import DrbLogicalNode

from drb_xquery.drb_xquery_signature import XquerySignature


class TestSignature(unittest.TestCase):
    def test_signature_ok(self):
        node = DrbLogicalNode('foobar')
        node.add_attribute('Content-Type',
                           'application/json;odata.metadata=minimal')
        node.value = 25
        node.append_child(DrbLogicalNode('child1'))
        node.append_child(DrbLogicalNode('child2'))

        # node match the signature
        # node match the signature
        code = """
                contains(data(@Content-Type), 'application/json')
            """

        signature = XquerySignature(code)
        self.assertTrue(signature.matches(node))

    def test_signature_ko(self):
        node = DrbLogicalNode('foobar')
        node.add_attribute('Content-Type',
                           'application/json;odata.metadata=minimal')
        node.value = 25
        node.append_child(DrbLogicalNode('child1'))
        node.append_child(DrbLogicalNode('child2'))

        code = """
                     contains(data(@Content-Type), 'applicatio/json')
                 """
        signature = XquerySignature(code)
        self.assertFalse(signature.matches(node))
