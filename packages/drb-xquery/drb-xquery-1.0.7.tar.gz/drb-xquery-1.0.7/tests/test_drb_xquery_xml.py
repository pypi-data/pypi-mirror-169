import os
import unittest

from pathlib import Path

from drb_impl_xml import XmlNodeFactory
from drb_xquery.drb_xquery import DrbXQuery
from drb_xquery.drb_xquery_res_to_string import XQueryResToString
from drb_xquery.drb_xquery_utils import DrbQueryFuncUtil


class NodeTest:
    def __init__(self):
        self.value = 'test'


class TestDrbXQueryXml(unittest.TestCase):
    current_path = Path(os.path.dirname(os.path.realpath(__file__)))

    xml_file = current_path / "files" / "MTD_TL.xml"
    xml_file = str(xml_file)

    def test_xml_itme_to_xml(self):
        xml = """
          <frameset>
              <footprint>
                  <posList>0 1 2 3 4 5 6 7 8 9</posList>
              </footprint>
          </frameset>

          """
        node = XmlNodeFactory().create(xml)
        query = """
        let $frameset := footprint
        let $tokens := tokenize(data($frameset/posList)," ")
          return
          <gml:Polygon xmlns:gml="http://www.opengis.net/gml"
                       srsName="http://www.opengis.net/gml/srs/epsg.xml#4326">
            <gml:outerBoundaryIs>
              <gml:LinearRing>
                <gml:coordinates>
                { string-join(
                for $i at $index in $tokens return concat($i,  "," )
                    , " " )
                }
                </gml:coordinates>
              </gml:LinearRing>
            </gml:outerBoundaryIs>
          </gml:Polygon>
        """
        drb_query = DrbXQuery(query)
        result = drb_query.execute(node)

        node = DrbQueryFuncUtil.get_node(result)
        result_xml = XQueryResToString.drb_item_to_xml(
            node,
            context=drb_query.static_context,
            dynamic_context=None,
            namespace_declared=[])
        self.assertTrue(result_xml.startswith(
            '<gml:Polygon srsName='
            '"http://www.opengis.net/gml/srs/epsg.xml#4326"')
        )
        self.assertIn('oordinates>0, 1, 2, 3, 4, 5, 6, 7, 8, 9', result_xml)

    def test_func_xml_node(self):
        xml = """
          <frameset>
              <footprint>
                  <posList>0 1 2 3 4 5 6 7 8 9</posList>
              </footprint>
          </frameset>

          """
        node = XmlNodeFactory().create(xml)
        query = """
        let $frameset := footprint
        let $tokens := tokenize(data($frameset/posList)," ")
          return
            drb:xml(
          <gml:Polygon xmlns:gml="http://www.opengis.net/gml"
                       srsName="http://www.opengis.net/gml/srs/epsg.xml#4326">
            <gml:outerBoundaryIs>
              <gml:LinearRing>
                <gml:coordinates>
                { string-join(
                for $i at $index in $tokens return concat($i,  "," )
                    , " " )
                }
                </gml:coordinates>
              </gml:LinearRing>
            </gml:outerBoundaryIs>
          </gml:Polygon>
          )
        """
        drb_query = DrbXQuery(query)
        result = drb_query.execute(node)

        result_xml = DrbQueryFuncUtil.get_node(result)

        self.assertTrue(result_xml.startswith(
            '<gml:Polygon srsName='
            '"http://www.opengis.net/gml/srs/epsg.xml#4326"')
        )
        self.assertIn('oordinates>0, 1, 2, 3, 4, 5, 6, 7, 8, 9', result_xml)

    def test_func_xml_var(self):
        xml = """
          <frameset>
              <footprint>
                  <posList>0 1 2 3 4 5 6 7 8 9</posList>
              </footprint>
          </frameset>

          """
        node = XmlNodeFactory().create(xml)
        query = """
        let $frameset := footprint
        let $tokens := tokenize(data($frameset/posList)," ")
          return
            drb:xml($tokens)
          )
        """
        drb_query = DrbXQuery(query)
        result = drb_query.execute(node)

        result_xml = DrbQueryFuncUtil.get_node(result)

        self.assertEqual(result_xml, '0 1 2 3 4 5 6 7 8 9')

    def test_func_xml_string(self):
        xml = """
          <frameset>
              <footprint id="attr">
                  <posList>0 1 2 3 4 5 6 7 8 9</posList>
              </footprint>
          </frameset>
          """
        node = XmlNodeFactory().create(xml)
        query = """
        let $frameset := 'footprint'
          return
            drb:xml($frameset)
          )
        """
        drb_query = DrbXQuery(query)
        result = drb_query.execute(node)

        result_xml = DrbQueryFuncUtil.get_node(result)

        self.assertEqual(result_xml, 'footprint')

    def test_func_xml_ns(self):
        xml = """
             <gml:frameset xmlns:gml="http://www.opengis.net/gml"
                 xmlns:toto="dummyURI" xmlns:tiit="http://titi">
                 <toto:footprint name="Test example">
                     <posList>0 1 2 3 4 5 6 7 8 9</posList>
                 </toto:footprint>
             </gml:frameset>
             """
        node = XmlNodeFactory().create(xml)
        query = """
           let $frameset := footprint
             return
               drb:xml($frameset)
             )
           """
        drb_query = DrbXQuery(query)
        result = drb_query.execute(node)

        result_xml = DrbQueryFuncUtil.get_node(result)

        self.assertEqual(
            '<footprint xmlns="dummyURI" name="Test example">'
            '<posList>0 1 2 3 4 5 6 7 8 9</posList></footprint>',
            result_xml.strip())

    def test_func_xml_ns_declared(self):
        query = """
        declare namespace ns = "dummyURI";

         let $frameset :=
          <gml:Polygon xmlns:test="dummyURI" xmlns:titi="nstiti"
                       srsName="http://www.opengis.net/gml/srs/epsg.xml#4326">

                <test:coordinates>test</test:coordinates>
                <titi:coordinates>titi</titi:coordinates>
          </gml:Polygon>


          return
            drb:xml($frameset/ns:coordinates)

        """

        drb_query = DrbXQuery(query)
        result = drb_query.execute()

        result_xml = DrbQueryFuncUtil.get_node(result)

        self.assertEqual(
            '<test:coordinates xmlns:test="dummyURI">test</test:coordinates>',
            result_xml)

    def test_func_xml_ns_not_declared(self):
        query = """
           let $frameset :=
            <gml:Polygon xmlns:test="dummyURI" xmlns:titi="nstiti"
                         srsName="http://www.opengis.net/gml/srs/epsg.xml#4326">
                  <test:coordinates>test</test:coordinates>
                  <titi:coordinates>titi</titi:coordinates>
            </gml:Polygon>
            return
              drb:xml($frameset/test:coordinates)

          """

        drb_query = DrbXQuery(query)
        result = drb_query.execute()

        result_xml = DrbQueryFuncUtil.get_node(result)

        self.assertEqual('<test:coordinates '
                         'xmlns:test="dummyURI">test</test:coordinates>',
                         result_xml)

    def test_func_to_str_drb_xquery_node(self):
        query = """
           let $frameset :=
            <gml:Polygon xmlns:test="dummyURI" xmlns:titi="nstiti"
                         srsName="http://www.opengis.net/gml/srs/epsg.xml#4326">
                  <test:coordinates>test</test:coordinates>
                  <titi:coordinates>titi</titi:coordinates>
            </gml:Polygon>
            return
              $frameset/test:coordinates

          """

        drb_query = DrbXQuery(query)
        result = drb_query.execute()

        result_node = DrbQueryFuncUtil.get_node(result)

        self.assertEqual('<test:coordinates '
                         'xmlns:test="dummyURI">test</test:coordinates>',
                         str(result_node))

    def test_func_to_str_drb_node(self):
        xml = """
                <frameset>
                    <footprint>
                        <posList>0 1 2 3 4 5 6 7 8 9</posList>
                    </footprint>
                </frameset>
                """
        node = XmlNodeFactory().create(xml)
        drb_query = DrbXQuery('drb:xml(footprint/posList)')
        result = drb_query.execute(node)

        result_node = DrbQueryFuncUtil.get_node(result)

        self.assertEqual('<posList>0 1 2 3 4 5 6 7 8 9</posList>',
                         result_node.strip())

    def test_func_xml_attribute(self):
        xml = """
            <gml:frameset xmlns:gml="http://www.opengis.net/gml"
            xmlns:toto="http://toto" xmlns:attr_ns="url_attr">
                <toto:footprint attr_ns:name="Test example">
                    <posList>0 1 2 3 4 5 6 7 8 9</posList>
                </toto:footprint>
            </gml:frameset>
            """
        node = XmlNodeFactory().create(xml)
        query = """
          declare namespace ns_req = "url_attr";
          let $frameset := footprint/@ns_req:name
            return
              drb:xml($frameset)
            )
          """
        drb_query = DrbXQuery(query)
        result = drb_query.execute(node)

        result_xml = DrbQueryFuncUtil.get_node(result)

        self.assertEqual('<ns_req:name xmlns:ns_req="url_attr">'
                         'Test example</ns_req:name>', result_xml)

    def test_func_xml_attribute(self):
        xml = """
            <gml:frameset xmlns:gml="http://www.opengis.net/gml"
            xmlns:toto="http://toto" xmlns:attr_ns="url_attr">
                <toto:footprint attr_ns:name="Test example">
                    <posList>0 1 2 3 4 5 6 7 8 9</posList>
                </toto:footprint>
            </gml:frameset>
            """
        node = XmlNodeFactory().create(xml)
        query = """
          declare namespace ns_req = "url_attr";
          let $frameset := footprint/@ns_req:name
            return
              drb:xml($frameset)
            )
          """
        drb_query = DrbXQuery(query)
        result = drb_query.execute(node)

        result_xml = DrbQueryFuncUtil.get_node(result)

        self.assertEqual('<ns_req:name xmlns:ns_req="url_attr">'
                         'Test example</ns_req:name>', result_xml)

    def test_func_xml_node_ns_diff_attribute(self):

        query = """
        declare namespace ns_req = "url_attr";

        let $frameset :=  <gml:frameset xmlns:gml="http://www.opengis.net/gml"
          xmlns:toto="http://toto" xmlns:attr_ns="url_attr">
              <toto:footprint attr_ns:name="Test example">
                  <posList>0 1 2 3 4 5 6 7 8 9</posList>
              </toto:footprint>
          </gml:frameset>
          return
            drb:xml($frameset/footprint)
          )
        """
        drb_query = DrbXQuery(query)
        result = drb_query.execute()

        result_xml = DrbQueryFuncUtil.get_node(result)

        self.assertEqual('<toto:footprint ns_req:name="Test example" '
                         'xmlns:toto="http://toto" '
                         'xmlns:ns_req="url_attr">'
                         '<posList>0 1 2 3 4 5 6 7 8 9</posList>'
                         '</toto:footprint>', result_xml)

    def test_func_xml_node_ns_diff_attribute_no_declared(self):

        query = """
        let $frameset :=  <gml:frameset xmlns:gml="http://www.opengis.net/gml"
          xmlns:toto="http://toto" xmlns:attr_ns="url_attr">
              <toto:footprint attr_ns:name="Test example">
                  <posList>0 1 2 3 4 5 6 7 8 9</posList>
              </toto:footprint>
          </gml:frameset>
          return
            drb:xml($frameset/footprint)
          )
        """
        drb_query = DrbXQuery(query)
        result = drb_query.execute()

        result_xml = DrbQueryFuncUtil.get_node(result)

        self.assertEqual('<toto:footprint ns0:name="Test example" '
                         'xmlns:toto="http://toto" '
                         'xmlns:ns0="url_attr">'
                         '<posList>0 1 2 3 4 5 6 7 8 9</posList>'
                         '</toto:footprint>', result_xml)

    def test_func_xml_int(self):
        xml = """
          <frameset>
              <footprint>
                  <posList>0 1 2 3 4 5 6 7 8 9</posList>
              </footprint>
          </frameset>

          """
        node = XmlNodeFactory().create(xml)
        query = """
        let $frameset := footprint
        let $tokens := tokenize(data($frameset/posList), " ")
          return
            drb:xml($tokens[4])
          )
        """
        drb_query = DrbXQuery(query)
        result = drb_query.execute(node)

        result_xml = DrbQueryFuncUtil.get_node(result)

        self.assertEqual(result_xml, '3')
