from drb import DrbNode
from drb.factory import Signature
from drb_xquery import DrbXQuery
from drb_xquery.drb_xquery_utils import DrbQueryFuncUtil


class XquerySignature(Signature):
    """
    Allowing to check if a DRB Node match a specific XQuery.
    """
    def __init__(self, query: str):
        self._query_str = query
        self._xquery = DrbXQuery(self._query_str)

    def matches(self, node: DrbNode) -> bool:

        result = self._xquery.execute(node)
        if result is not None and len(result) > 0:
            return DrbQueryFuncUtil.get_effective_boolean_value(result)
        return False

    def to_dict(self) -> dict:
        return {self.get_name(): self._query_str}

    @staticmethod
    def get_name():
        return 'xquery'
