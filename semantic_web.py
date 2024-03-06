# Design an application to simulate semantic web.
#pip install rdflib
import rdflib
myGraph = rdflib.Graph()
myGraph.parse("myfoaf.rdf")
qres=myGraph.query(
"""SELECT DISTINCT ?fname ?lname
WHERE{
?a foaf:knows ?b .
?a foaf:name ?fname .
?b foaf:name ?lname .
}""")
for row in qres:
 print("%s knows %s"%row)
