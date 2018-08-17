__author__ = 'Hao'

import openpyxl
import json
from string import Template

file_path = "../data/Inkjet Printing Process File Repository/Droplet Ejection/Droplet Trigger Data Sheet.xlsx"
procs = {
    "DI_Water_A": {
        "sheet_name": "Ink-DI Water-Trial A",
        "ink_id": "DI_Water"
    },
    "Fifty_Glycerol_A": {
        "sheet_name": "Ink-50 Glycerol-Trial A",
        "ink_id": "Fifty_Glycerol"
    },
    "Eighty_Glycerol_A": {
        "sheet_name": "Ink-80 Glycerol-Trial A",
        "ink_id": "Eighty_Glycerol"
    },
    "TangoBlack_A": {
        "sheet_name": "Ink-TangoBlack-Trial A",
        "ink_id": "TangoBlack"
    },
    "TangoBlack_B": {
        "sheet_name": "Ink-TangoBlack-Trial B",
        "ink_id": "TangoBlack"
    },
    "VeroClear_A": {
        "sheet_name": "Ink-VeroClear-Trial A",
        "ink_id": "VeroClear"
    },
    "VeroClear_B": {
        "sheet_name": "Ink-VeroClear-Trial B",
        "ink_id": "VeroClear"
    }
}

wb = openpyxl.load_workbook(file_path, data_only=True)

# experiments = {x: {"id": x} for x in procs}

f = open("../output/experiments.ttl", "w+")

tt_process = """###  https://tw.rpi.edu/web/project/ampo-ink#Proc_${id}

:Proc_${id} rdf:type owl:NamedIndividual ,
                     :DropletProductionProcess .



"""

tt_step = """###  https://tw.rpi.edu/web/project/ampo-ink#Step_${id}_Ejection_${index}_of_118

:Step_${id}_Ejection_${index}_of_118 rdf:type  owl:NamedIndividual ,
                                        :MaterialDeposition ;

                                        rdfs:label "Step_${id}_Ejection_${index}_of_118"^^xsd:string ;

                                        ampo:hasParticipant :${ink_id} ;

                                        ampo:produces :Prod_${id}_Droplet_${index}_of_118 ;

                                        ampo:hasParticipant :Nozzle_BC ;

                                        ampo:qualifiedEquipmentUsage [ rdf:type ampo:EquipmentUsage ;
                                                                       ampo:requiresInput :DropletActuation_${wave_id} ;
                                                                       ampo:equipment :Nozzle_BC ;
                                                                       ampo:requiresInput [ rdf:type :ActuatorNozzle_HeaterBlockTemperature ;
                                                                                            ampo:isInputOf :Nozzle_BC ;
                                                                                            qudt:quantityValue [ rdf:type qudt:QuantityValue ;
                                                                                                                 qudt:numericValue "${heat_block_temp}"^^xsd:double ;
                                                                                                                 qudt:unit qudt-unit:DegreeCelsius
                                                                                                               ]
                                                                                          ]
                                                                     ] .



###  https://tw.rpi.edu/web/project/ampo-ink#Prod_${id}_Droplet_${index}_of_118

:Prod_${id}_Droplet_${index}_of_118 rdf:type owl:NamedIndividual ,
                                                 :Droplet ;

                                        rdfs:label "Prod_${id}_Droplet_${index}_of_118"^^xsd:string ;

                                        ampo:hasAttribute [ rdf:type :Droplet_Visible ;
                                                           rdf:value "${visible}"^^xsd:boolean
                                                          ] ,
                                                         [ rdf:type :Droplet_Ejected ;
                                                           rdf:value "${ejected}"^^xsd:boolean
                                                         ] ,
                                                         [ rdf:type :Droplet_DistanceTraveled ;
                                                           qudt:quantityValue [ rdf:type qudt:QuantityValue ;
                                                                                qudt:numericValue "${distance_traveled}"^^xsd:double ;
                                                                                qudt:unit qudt-unit:Micrometer
                                                                              ]
                                                         ] ,
                                                         [ rdf:type :Droplet_TimeFrame_2 ;
                                                           qudt:quantityValue [ rdf:type qudt:QuantityValue ;
                                                                                qudt:numericValue "${t2}"^^xsd:double ;
                                                                                qudt:unit qudt-unit:MicroSecond
                                                                              ]
                                                         ] ,
                                                         [ rdf:type :Droplet_Velocity ;
                                                           qudt:quantityValue [ rdf:type qudt:QuantityValue ;
                                                                                qudt:numericValue "${velocity}"^^xsd:double ;
                                                                                qudt:unit qudt-unit:MeterPerSecond
                                                                              ]
                                                         ] ,
                                                         [ rdf:type :Droplet_TimeFrame_1 ;
                                                           qudt:quantityValue [ rdf:type qudt:QuantityValue ;
                                                                                qudt:numericValue "${t1}"^^xsd:double ;
                                                                                qudt:unit qudt-unit:MicroSecond
                                                                              ]
                                                         ] ,
                                                         [ rdf:type :Droplet_Diameter ;
                                                           qudt:quantityValue [ rdf:type qudt:QuantityValue ;
                                                                                qudt:numericValue "${diameter}"^^xsd:double ;
                                                                                qudt:unit qudt-unit:Micrometer
                                                                              ]
                                                         ] ,
                                                         [ rdf:type :Droplet_Tail ;
                                                           rdf:value "${tail}"^^xsd:boolean
                                                         ] ,
                                                         [ rdf:type :Droplet_Satellites ;
                                                           rdf:value "${satellites}"^^xsd:boolean
                                                         ] .



:Proc_${id} ampo:hasStep :Step_${id}_Ejection_${index}_of_118 .

:${ink_id} ampo:isParticipantIn :Step_${id}_Ejection_${index}_of_118 .

:Nozzle_BC ampo:isParticipantIn :Step_${id}_Ejection_${index}_of_118 .

:Nozzle_BC ampo:hasInput :DropletActuation_${wave_id} .

:DropletActuation_${wave_id} ampo:isInputOf :Nozzle_BC .



"""

t_process = Template(tt_process)
t_step = Template(tt_step)

# Helper function for transfering into booleans
def to_boolean(s):
    if s == "Y" or s=="Yes" or s=="True":
        return "true"
    else:
        return "false"

# Helper function for transfering into numbers
def to_number(s):
    try:
        return float(s)
    except:
        return ""


for x in procs:
# for x in {"TangoBlack_A": procs["TangoBlack_A"]}:

    print("Processing process " + str(x) + " ...")

    sheet = wb[procs[x]["sheet_name"]]

    total_steps = 0

    for i in range(2, len(sheet["A"])+1):
        if sheet["A" + str(i)].value:
            total_steps += 1
        else:
            break


    f.write(t_process.substitute({
        "id": x
    }))

    for i in range(1, total_steps + 1):
    # for i in range(1, 3):

        print("  Processing step " + str(i) + " of " + str(total_steps) + " total steps ...")
        row = i
        # print(i)
        # print(row)
        # print(str(sheet["A"][row].value))

        f.write(t_step.substitute({
            "id": x,
            "index": i,
            "ink_id": procs[x]["ink_id"],
            "wave_id": "TR-" + str(sheet["A"][row].value),
            "heat_block_temp": to_number(sheet["D"][row].value),
            "visible": to_boolean(sheet["F"][row].value),
            "ejected": to_boolean(sheet["G"][row].value),
            "tail": to_boolean(sheet["M"][row].value),
            "satellites": to_boolean(sheet["N"][row].value),
            "distance_traveled": to_number(sheet["K"][row].value),
            "t1": to_number(sheet["I"][row].value),
            "t2": to_number(sheet["J"][row].value),
            "velocity": to_number(sheet["L"][row].value),
            "diameter": to_number(sheet["H"][row].value)

        }))

        print("    Writing finished. Proceed to the next entry ...")


f.close()



