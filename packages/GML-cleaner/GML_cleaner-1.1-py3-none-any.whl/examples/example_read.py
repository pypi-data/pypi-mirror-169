import os
from clean_gml.gml import Gml

filepath = 'examples/Blinde_inlaten copy.gml'
filepath = 'example.gml'

datatype_changes = {'OPENBARE_RUIMTE': 'xsd:float'}
datatype_changes = {'PROPERTY': 'xsd:float'}

gml = Gml(filepath)
gml.datatype_changes(changes=datatype_changes)
gml.replace_commas(ndigits=3)
gml.save()
