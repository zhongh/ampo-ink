__author__ = 'Hao'

import openpyxl
import json
from string import Template

wb = openpyxl.load_workbook("../data/Inkjet Printing Process File Repository/Droplet Ejection/Trigger Waveform Graph Master Sheet.xlsx", data_only=True)

waves = {key: {"id": key, "label": key} for key in wb.sheetnames}

for wave in waves:
    # print(wave)
    try:
        sheet = wb[wave]
        waves[wave]["line_type"] = sheet["A" + str(len(sheet["A"]) - 1)].value.strip()
        waves[wave]["waveform_type"] = sheet["A" + str(len(sheet["A"]))].value.strip()
        # print(waves[wave]["line_type"])
        # print(waves[wave]["waveform_type"])
    except:
        waves[wave]["line_type"] = ""
        waves[wave]["waveform_type"] = ""

    if waves[wave]["line_type"] == 'Bipolar Lines':

        waves[wave]["rise_time"] = sheet["B3"].value - sheet["B2"].value
        waves[wave]["dwell_time"] = sheet["B4"].value - sheet["B3"].value
        waves[wave]["fall_time"] = sheet["B5"].value - sheet["B4"].value
        waves[wave]["echo_time"] = sheet["B6"].value - sheet["B5"].value
        waves[wave]["final_rise_time"] = sheet["B7"].value - sheet["B6"].value
        waves[wave]["max_volt"] = max([x[0].value for x in sheet["C2":"C7"]])
        waves[wave]["min_volt"] = min([x[0].value for x in sheet["C2":"C7"]])
        waves[wave]["idle_volt"] = ""
        waves[wave]["amplitude"] = ""
        waves[wave]["period"] = ""

    elif waves[wave]["waveform_type"] == 'Sine Waveform':

        waves[wave]["rise_time"] = ""
        waves[wave]["dwell_time"] = ""
        waves[wave]["fall_time"] = ""
        waves[wave]["echo_time"] = ""
        waves[wave]["final_rise_time"] = ""
        waves[wave]["max_volt"] = max([x[0].value for x in sheet["C2":"C14"]])
        waves[wave]["min_volt"] = min([x[0].value for x in sheet["C2":"C14"]])
        waves[wave]["idle_volt"] = sheet["G1"].value
        waves[wave]["amplitude"] = sheet["G2"].value
        waves[wave]["period"] = sheet["G4"].value

    elif waves[wave]["waveform_type"] == 'Unipolar Waveform':

        waves[wave]["rise_time"] = sheet["B3"].value - sheet["B2"].value
        waves[wave]["dwell_time"] = sheet["B4"].value - sheet["B3"].value
        waves[wave]["fall_time"] = sheet["B5"].value - sheet["B4"].value
        waves[wave]["echo_time"] = ""
        waves[wave]["final_rise_time"] = ""
        waves[wave]["max_volt"] = max([x[0].value for x in sheet["C2":"C5"]])
        waves[wave]["min_volt"] = 0
        waves[wave]["idle_volt"] = ""
        waves[wave]["amplitude"] = ""
        waves[wave]["period"] = ""

    else:
        waves[wave]["rise_time"] = ""
        waves[wave]["dwell_time"] = ""
        waves[wave]["fall_time"] = ""
        waves[wave]["echo_time"] = ""
        waves[wave]["final_rise_time"] = ""
        waves[wave]["max_volt"] = ""
        waves[wave]["min_volt"] = ""
        waves[wave]["idle_volt"] = ""
        waves[wave]["amplitude"] = ""
        waves[wave]["period"] = ""


#print(json.dumps(waves, sort_keys=True, indent=4))

# Keys to use in constructing inks dictionary and template matching dictionary
d_keys = ["id", "label", "line_type", "waveform_type",
          "rise_time", "dwell_time", "fall_time", "echo_time", "final_rise_time",
          "max_volt", "min_volt", "idle_volt", "amplitude", "period"]


prefix_ampo = "https://tw.rpi.edu/web/project/ampo-ink#"

tt = """###  https://tw.rpi.edu/web/project/ampo-ink#DropletActuation_${id}

:DropletActuation_${id} rdf:type :Actuator_DropletActuation, owl:NamedIndividual ;

                       rdfs:label "${label}"^^xsd:string ;

                       ampo:hasAttribute [ rdf:type :DropletActuation_DwellTime ;
                                           rdfs:label "Dwell Time (μs)"^^xsd:string ;
                                           qudt:quantityValue [ qudt:numericValue "${dwell_time}"^^xsd:double ;
                                                                qudt:unit qudt-unit:MicroSecond
                                                              ]
                                         ] ,
                                         [ rdf:type :DropletActuation_FallTime ;
                                           rdfs:label "Fall Time (μs)"^^xsd:string ;
                                           qudt:quantityValue [ qudt:numericValue "${fall_time}"^^xsd:double ;
                                                                qudt:unit qudt-unit:MicroSecond
                                                              ]
                                         ] ,
                                         [ rdf:type :DropletActuation_RiseTime ;
                                           rdfs:label "Rise Time (μs)"^^xsd:string ;
                                           qudt:quantityValue [ qudt:numericValue "${rise_time}"^^xsd:double ;
                                                                qudt:unit qudt-unit:MicroSecond
                                                              ]
                                         ] ,
                                         [ rdf:type :DropletActuation_Amplitude ;
                                           rdfs:label "Amplitude (V)"^^xsd:string ;
                                           qudt:quantityValue [ qudt:numericValue "${amplitude}"^^xsd:double ;
                                                                qudt:unit qudt-unit:Volt
                                                              ]
                                         ] ,
                                         [ rdf:type :DropletActuation_WaveformType ;
                                           rdfs:label "Waveform Type"^^xsd:string ;
                                           ampo:descriptiveValue "${waveform_type}"^^xsd:string
                                         ] ,
                                         [ rdf:type :DropletActuation_FinalRiseTime ;
                                           rdfs:label "Final Rise Time (μs)"^^xsd:string ;
                                           qudt:quantityValue [ qudt:numericValue "${final_rise_time}"^^xsd:double ;
                                                                qudt:unit qudt-unit:MicroSecond
                                                              ]
                                         ] ,
                                         [ rdf:type :DropletActuation_LineType ;
                                           rdfs:label "Line Type"^^xsd:string ;
                                           ampo:descriptiveValue "${line_type}"^^xsd:string
                                         ] ,
                                         [ rdf:type :DropletActuation_EchoTime ;
                                           rdfs:label "Echo Time (μs)"^^xsd:string ;
                                           qudt:quantityValue [ qudt:numericValue "${echo_time}"^^xsd:double ;
                                                                qudt:unit qudt-unit:MicroSecond
                                                              ]
                                         ] ,
                                         [ rdf:type :DropletActuation_IdleVoltage ;
                                           rdfs:label "Idle Voltage (V)"^^xsd:string ;
                                           qudt:quantityValue [ qudt:numericValue "${idle_volt}"^^xsd:double ;
                                                                qudt:unit qudt-unit:Volt
                                                              ]
                                         ] ,
                                         [ rdf:type :DropletActuation_MaxVoltageAmplitude ;
                                           rdfs:label "Maximum Voltage Amplitude (V)"^^xsd:string ;
                                           qudt:quantityValue [ qudt:numericValue "${max_volt}"^^xsd:double ;
                                                                qudt:unit qudt-unit:Volt
                                                              ]
                                         ] ,
                                         [ rdf:type :DropletActuation_Period ;
                                           rdfs:label "Period (μs)"^^xsd:string ;
                                           qudt:quantityValue [ qudt:numericValue "${period}"^^xsd:double ;
                                                                qudt:unit qudt-unit:MicroSecond
                                                              ]
                                         ] ,
                                         [ rdf:type :DropletActuation_MinVoltageAmplitude ;
                                           rdfs:label "Minimum Voltage Amplitude (V)"^^xsd:string ;
                                           qudt:quantityValue [ qudt:numericValue "${min_volt}"^^xsd:double ;
                                                                qudt:unit qudt-unit:Volt
                                                              ]
                                         ] .
"""

t = Template(tt)

f = open("../output/waveforms.ttl", "w+")

f.write("""@prefix : <https://tw.rpi.edu/web/project/ampo-ink#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix sio: <http://semanticscience.org/resource/> .
@prefix xml: <http://www.w3.org/XML/1998/namespace> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix ampo: <https://tw.rpi.edu/web/project/ampo#> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix qudt: <http://data.nasa.gov/qudt/owl/qudt#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix qudt-unit: <http://qudt.org/1.1/vocab/unit#> .
@base <https://tw.rpi.edu/web/project/ampo-ink> .



""")

# for wave in waves:
for i in range(1, 119):
    wave = "TR-" + str(i)
    print(wave)
    d = {key: waves[wave][key] for key in d_keys}
    # print(d)
    # print(t.substitute(d))
    f.write(t.substitute(d) + "\n\n\n")

f.close()

print("All waveforms read.")
