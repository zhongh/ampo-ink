__author__ = 'Hao'

import openpyxl
import json
from string import Template

# Initialize the inks list
inks = {
    "DI_Water": {
        "filepath": "../data/Inkjet Printing Process File Repository/Droplet Ejection/DI Water Ink-A/Fluid Properties-DI Water.xlsx"
    },
    "Fifty_Glycerol": {
        "filepath": "../data/Inkjet Printing Process File Repository/Droplet Ejection/50 Glycerol Ink-A/Fluid Properties-50 Glycerol.xlsx"
    },
    "Eighty_Glycerol": {
        "filepath": "../data/Inkjet Printing Process File Repository/Droplet Ejection/80 Glycerol Ink-A/Fluid Properties-80 Glycerol.xlsx"
    },
    "TangoBlack": {
        "filepath": "../data/Inkjet Printing Process File Repository/Droplet Ejection/TangoBlack Ink-A/Fluid Properties-TangoBlack.xlsx"
    },
    "VeroClear": {
        "filepath": "../data/Inkjet Printing Process File Repository/Droplet Ejection/VeroClear Ink-A/Fluid Properties-VeroClear.xlsx"
    }
}

# Helper function
def process_empty_values(x):
    try:
        return float(x)
    except:
        return ""

# Keys to use in constructing inks dictionary and template matching dictionary
d_keys = ["ink_id", "ink_label", "density", "dynamic_viscosity", "color", "surface_tension"]

# Populate inks list
for ink in inks:
    wb = openpyxl.load_workbook(inks[ink]["filepath"], data_only=True)
    sheet = wb.active
    inks[ink]["ink_id"] = ink
    inks[ink]["ink_label"] = sheet["B1"].value
    inks[ink]["density"] = process_empty_values(sheet["B2"].value)
    inks[ink]["dynamic_viscosity"] = process_empty_values(sheet["B3"].value)
    inks[ink]["surface_tension"] = process_empty_values(sheet["B4"].value)
    inks[ink]["color"] = sheet["B5"].value


prefix_ampo = "https://tw.rpi.edu/web/project/ampo-ink#"

tt = """###  https://tw.rpi.edu/web/project/ampo-ink#${ink_id}

:${ink_id} rdf:type :Ink ;

          rdfs:label "${ink_label}"^^xsd:string ;

          ampo:hasAttribute [ rdf:type :Ink_Density ;
                              rdfs:label "Density"^^xsd:string ;
                              qudt:quantityValue [ rdf:type qudt:QuantityValue ;
                                                   qudt:numericValue "${density}"^^xsd:double ;
                                                   qudt:unit qudt-unit:KilogramPerCubicMeter
                                                 ]
                            ] ,
                            [ rdf:type :Ink_DynamicViscosity ;
                              rdfs:label "Dynamic Viscosity"^^xsd:string ;
                              qudt:quantityValue [ rdf:type qudt:QuantityValue ;
                                                   qudt:numericValue "${dynamic_viscosity}"^^xsd:double ;
                                                   qudt:unit qudt-unit:PascalSecond
                                                 ]
                            ] ,
                            [ rdf:type :Ink_Color ;
                              rdfs:label "Color"^^xsd:string ;
                              ampo:descriptiveValue "${color}"^^xsd:string
                            ] ,
                            [ rdf:type :Ink_SurfaceTension ;
                              rdfs:label "Surface Tension"^^xsd:string ;
                              qudt:quantityValue [ rdf:type qudt:QuantityValue ;
                                                   qudt:numericValue "${surface_tension}"^^xsd:double ;
                                                   qudt:unit qudt-unit:NewtonPerMeter
                                                 ]
                            ] .
"""

f = open("../output/inks.ttl", "w+")

for ink in inks:
    t = Template(tt)
    d = {key: inks[ink][key] for key in d_keys}
    # print(t.substitute(d))
    f.write(t.substitute(d) + "\n\n\n")

f.close()

print("All inks read.")