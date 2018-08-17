# Sample Query Questions for Droplet Ejection Data

### (1) Select Trigger Waveforms that 

    (a) ejected a droplet
    (b) did not produce a satellite droplet
    (c) did not produce a tail 
    (d) have a symmetric bipolar waveform

```
prefix : <https://tw.rpi.edu/web/project/ampo-ink#> 
prefix owl: <http://www.w3.org/2002/07/owl#> 
prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
prefix sio: <http://semanticscience.org/resource/> 
prefix xml: <http://www.w3.org/XML/1998/namespace> 
prefix xsd: <http://www.w3.org/2001/XMLSchema#> 
prefix ampo: <https://tw.rpi.edu/web/project/ampo#> 
prefix ampo-ink: <https://tw.rpi.edu/web/project/ampo-ink#> 
prefix foaf: <http://xmlns.com/foaf/0.1/> 
prefix prov: <http://www.w3.org/ns/prov#> 
prefix qudt: <http://data.nasa.gov/qudt/owl/qudt#> 
prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
prefix dcterms: <http://purl.org/dc/terms/> 
prefix qudt-unit: <http://qudt.org/1.1/vocab/unit#> 

SELECT ?Trigger_Waveform ?Rise_Time ?Dwell_Time ?Fall_Time ?Echo_Time ?Final_Rise_Time 
?Max_Voltage_Amplitude ?Min_Voltage_Amplitude ?Period ?Idle_Voltage ?Amplitude ?Waveform_Type
?nozzle ?Nozzle_Temp 
?Droplet_Ejected ?Droplet_Visible ?Droplet_Tail ?Droplet_Satellites
?Droplet_T1 ?Droplet_T2 ?Droplet_Diameter ?Droplet_Velocity ?Droplet_Distance_Traveled ?Ink
WHERE { 
?step rdf:type :MaterialDeposition .
?step ampo:qualifiedEquipmentUsage ?nozzle_usage .
?nozzle_usage ampo:requiresInput ?subject .
?subject rdf:type :Actuator_DropletActuation .
?subject rdfs:label ?subject_label .
BIND( STR(?subject_label) AS ?Trigger_Waveform ) .
OPTIONAL {
    ?subject ampo:hasAttribute ?rise_time .
	?rise_time rdf:type :DropletActuation_RiseTime .
	?rise_time qudt:quantityValue ?rise_time_QV .
	?rise_time_QV qudt:numericValue ?rise_time_value .
	BIND(STR(?rise_time_value) AS ?Rise_Time) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?dwell_time .
	?dwell_time rdf:type :DropletActuation_DwellTime .
	?dwell_time qudt:quantityValue ?dwell_time_QV .
	?dwell_time_QV qudt:numericValue ?dwell_time_value .
	BIND(STR(?dwell_time_value) AS ?Dwell_Time) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?fall_time .
	?fall_time rdf:type :DropletActuation_FallTime .
	?fall_time qudt:quantityValue ?fall_time_QV .
	?fall_time_QV qudt:numericValue ?fall_time_value .
	BIND(STR(?fall_time_value) AS ?Fall_Time) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?echo_time .
	?echo_time rdf:type :DropletActuation_EchoTime .
	?echo_time qudt:quantityValue ?echo_time_QV .
	?echo_time_QV qudt:numericValue ?echo_time_value .
	BIND(STR(?echo_time_value) AS ?Echo_Time) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?final_rise_time .
	?final_rise_time rdf:type :DropletActuation_FinalRiseTime .
	?final_rise_time qudt:quantityValue ?final_rise_time_QV .
	?final_rise_time_QV qudt:numericValue ?final_rise_time_value .
	BIND(STR(?final_rise_time_value) AS ?Final_Rise_Time) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?max_voltage_amplitude .
	?max_voltage_amplitude rdf:type :DropletActuation_MaxVoltageAmplitude .
	?max_voltage_amplitude qudt:quantityValue ?max_voltage_amplitude_QV .
	?max_voltage_amplitude_QV qudt:numericValue ?max_voltage_amplitude_value .
	BIND(STR(?max_voltage_amplitude_value) AS ?Max_Voltage_Amplitude) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?min_voltage_amplitude .
	?min_voltage_amplitude rdf:type :DropletActuation_MinVoltageAmplitude .
	?min_voltage_amplitude qudt:quantityValue ?min_voltage_amplitude_QV .
	?min_voltage_amplitude_QV qudt:numericValue ?min_voltage_amplitude_value .
	BIND(STR(?min_voltage_amplitude_value) AS ?Min_Voltage_Amplitude) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?period .
	?period rdf:type :DropletActuation_Period .
	?period qudt:quantityValue ?period_QV .
	?period_QV qudt:numericValue ?period_value .
	BIND(STR(?period_value) AS ?Period) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?amplitude .
	?amplitude rdf:type :DropletActuation_Amplitude .
	?amplitude qudt:quantityValue ?amplitude_QV .
	?amplitude_QV qudt:numericValue ?amplitude_value .
	BIND(STR(?amplitude_value) AS ?Amplitude) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?idle_voltage .
	?idle_voltage rdf:type :DropletActuation_IdleVoltage .
	?idle_voltage qudt:quantityValue ?idle_voltage_QV .
	?idle_voltage_QV qudt:numericValue ?idle_voltage_value .
	BIND(STR(?idle_voltage_value) AS ?Idle_Voltage) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?line_type .
	?line_type rdf:type :DropletActuation_LineType .
	?line_type ampo:descriptiveValue ?line_type_value .
	BIND(STR(?line_type_value) AS ?Line_Type) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?waveform_type .
	?waveform_type rdf:type :DropletActuation_WaveformType .
	?waveform_type ampo:descriptiveValue ?waveform_type_value .
	BIND(STR(?waveform_type_value) AS ?Waveform_Type) .
}
?nozzle_usage ampo:equipment ?nozzle .
?nozzle_usage ampo:requiresInput ?nozzle_temp_input .
?nozzle_temp_input a :ActuatorNozzle_HeaterBlockTemperature .
?nozzle_temp_input qudt:quantityValue ?nozzle_temp_QV .
?nozzle_temp_QV qudt:numericValue ?nozzle_temp .
BIND ( STR(?nozzle_temp) AS ?Nozzle_Temp ) .
?step ampo:produces ?droplet .
?droplet a :Droplet .
OPTIONAL {?droplet rdfs:label ?droplet_label . }
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_ejected_attr . 
	?droplet_ejected_attr a :Droplet_Ejected .
	?droplet_ejected_attr rdf:value ?droplet_ejected .
	BIND ( STR(?droplet_ejected) AS ?Droplet_Ejected) .
}
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_visible_attr . 
	?droplet_visible_attr a :Droplet_Visible .
	?droplet_visible_attr rdf:value ?droplet_visible . 
	BIND ( STR(?droplet_visible) AS ?Droplet_Visible) .
}
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_tail_attr . 
	?droplet_tail_attr a :Droplet_Tail .
	?droplet_tail_attr rdf:value ?droplet_tail . 
	BIND ( STR(?droplet_tail) AS ?Droplet_Tail) .
}
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_satellites_attr . 
	?droplet_satellites_attr a :Droplet_Satellites .
	?droplet_satellites_attr rdf:value ?droplet_satellites . 
	BIND ( STR(?droplet_satellites) AS ?Droplet_Satellites) .
}
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_t1_attr . 
	?droplet_t1_attr a :Droplet_TimeFrame_1 .
	?droplet_t1_attr qudt:quantityValue ?droplet_t1_QV . 
	?droplet_t1_QV qudt:numericValue ?droplet_t1 .
	BIND ( STR(?droplet_t1) AS ?Droplet_T1) .

}
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_t2_attr . 
	?droplet_t2_attr a :Droplet_TimeFrame_2 .
	?droplet_t2_attr qudt:quantityValue ?droplet_t2_QV . 
	?droplet_t2_QV qudt:numericValue ?droplet_t2 .
	BIND ( STR(?droplet_t2) AS ?Droplet_T2) .
}
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_diameter_attr . 
	?droplet_diameter_attr a :Droplet_Diameter .
	?droplet_diameter_attr qudt:quantityValue ?droplet_diameter_QV . 
	?droplet_diameter_QV qudt:numericValue ?droplet_diameter .
	BIND ( STR(?droplet_diameter) AS ?Droplet_Diameter) .
}
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_velocity_attr . 
	?droplet_velocity_attr a :Droplet_Velocity .
	?droplet_velocity_attr qudt:quantityValue ?droplet_velocity_QV . 
	?droplet_velocity_QV qudt:numericValue ?droplet_velocity .
	BIND ( STR(?droplet_velocity) AS ?Droplet_Velocity) .
}
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_distance_traveled_attr . 
	?droplet_distance_traveled_attr a :Droplet_DistanceTraveled .
	?droplet_distance_traveled_attr qudt:quantityValue ?droplet_distance_traveled_QV . 
	?droplet_distance_traveled_QV qudt:numericValue ?droplet_distance_traveled .
	BIND ( STR(?droplet_distance_traveled) AS ?Droplet_Distance_Traveled) .
}
?step ampo:hasParticipant ?ink .
?ink a ampo-ink:Ink .
?ink rdfs:label ?ink_label .
BIND ( STR(?ink_label) AS ?Ink) .
FILTER (STR(?waveform_type_value) = "Symmetric Bipolar Waveform") .
FILTER ( ?droplet_ejected ) .
FILTER ( !(?droplet_satellites) ) .
FILTER ( !(?droplet_tail) ) .
}
ORDER BY ?ink_label
```
	
### (2) Select Trigger Waveforms that 
	(a) ejected a droplet
	(b) did not produce a satellite droplet
	(c) did not produce a tail 
	(d) have a sine waveform
	
```
prefix : <https://tw.rpi.edu/web/project/ampo-ink#> 
prefix owl: <http://www.w3.org/2002/07/owl#> 
prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
prefix sio: <http://semanticscience.org/resource/> 
prefix xml: <http://www.w3.org/XML/1998/namespace> 
prefix xsd: <http://www.w3.org/2001/XMLSchema#> 
prefix ampo: <https://tw.rpi.edu/web/project/ampo#> 
prefix ampo-ink: <https://tw.rpi.edu/web/project/ampo-ink#> 
prefix foaf: <http://xmlns.com/foaf/0.1/> 
prefix prov: <http://www.w3.org/ns/prov#> 
prefix qudt: <http://data.nasa.gov/qudt/owl/qudt#> 
prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
prefix dcterms: <http://purl.org/dc/terms/> 
prefix qudt-unit: <http://qudt.org/1.1/vocab/unit#> 

SELECT ?Trigger_Waveform ?Rise_Time ?Dwell_Time ?Fall_Time ?Echo_Time ?Final_Rise_Time 
?Max_Voltage_Amplitude ?Min_Voltage_Amplitude ?Period ?Idle_Voltage ?Amplitude ?Waveform_Type
?nozzle ?Nozzle_Temp 
?Droplet_Ejected ?Droplet_Visible ?Droplet_Tail ?Droplet_Satellites
?Droplet_T1 ?Droplet_T2 ?Droplet_Diameter ?Droplet_Velocity ?Droplet_Distance_Traveled ?Ink
WHERE { 
?step rdf:type :MaterialDeposition .
?step ampo:qualifiedEquipmentUsage ?nozzle_usage .
?nozzle_usage ampo:requiresInput ?subject .
?subject rdf:type :Actuator_DropletActuation .
?subject rdfs:label ?subject_label .
BIND( STR(?subject_label) AS ?Trigger_Waveform ) .
OPTIONAL {
    ?subject ampo:hasAttribute ?rise_time .
	?rise_time rdf:type :DropletActuation_RiseTime .
	?rise_time qudt:quantityValue ?rise_time_QV .
	?rise_time_QV qudt:numericValue ?rise_time_value .
	BIND(STR(?rise_time_value) AS ?Rise_Time) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?dwell_time .
	?dwell_time rdf:type :DropletActuation_DwellTime .
	?dwell_time qudt:quantityValue ?dwell_time_QV .
	?dwell_time_QV qudt:numericValue ?dwell_time_value .
	BIND(STR(?dwell_time_value) AS ?Dwell_Time) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?fall_time .
	?fall_time rdf:type :DropletActuation_FallTime .
	?fall_time qudt:quantityValue ?fall_time_QV .
	?fall_time_QV qudt:numericValue ?fall_time_value .
	BIND(STR(?fall_time_value) AS ?Fall_Time) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?echo_time .
	?echo_time rdf:type :DropletActuation_EchoTime .
	?echo_time qudt:quantityValue ?echo_time_QV .
	?echo_time_QV qudt:numericValue ?echo_time_value .
	BIND(STR(?echo_time_value) AS ?Echo_Time) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?final_rise_time .
	?final_rise_time rdf:type :DropletActuation_FinalRiseTime .
	?final_rise_time qudt:quantityValue ?final_rise_time_QV .
	?final_rise_time_QV qudt:numericValue ?final_rise_time_value .
	BIND(STR(?final_rise_time_value) AS ?Final_Rise_Time) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?max_voltage_amplitude .
	?max_voltage_amplitude rdf:type :DropletActuation_MaxVoltageAmplitude .
	?max_voltage_amplitude qudt:quantityValue ?max_voltage_amplitude_QV .
	?max_voltage_amplitude_QV qudt:numericValue ?max_voltage_amplitude_value .
	BIND(STR(?max_voltage_amplitude_value) AS ?Max_Voltage_Amplitude) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?min_voltage_amplitude .
	?min_voltage_amplitude rdf:type :DropletActuation_MinVoltageAmplitude .
	?min_voltage_amplitude qudt:quantityValue ?min_voltage_amplitude_QV .
	?min_voltage_amplitude_QV qudt:numericValue ?min_voltage_amplitude_value .
	BIND(STR(?min_voltage_amplitude_value) AS ?Min_Voltage_Amplitude) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?period .
	?period rdf:type :DropletActuation_Period .
	?period qudt:quantityValue ?period_QV .
	?period_QV qudt:numericValue ?period_value .
	BIND(STR(?period_value) AS ?Period) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?amplitude .
	?amplitude rdf:type :DropletActuation_Amplitude .
	?amplitude qudt:quantityValue ?amplitude_QV .
	?amplitude_QV qudt:numericValue ?amplitude_value .
	BIND(STR(?amplitude_value) AS ?Amplitude) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?idle_voltage .
	?idle_voltage rdf:type :DropletActuation_IdleVoltage .
	?idle_voltage qudt:quantityValue ?idle_voltage_QV .
	?idle_voltage_QV qudt:numericValue ?idle_voltage_value .
	BIND(STR(?idle_voltage_value) AS ?Idle_Voltage) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?line_type .
	?line_type rdf:type :DropletActuation_LineType .
	?line_type ampo:descriptiveValue ?line_type_value .
	BIND(STR(?line_type_value) AS ?Line_Type) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?waveform_type .
	?waveform_type rdf:type :DropletActuation_WaveformType .
	?waveform_type ampo:descriptiveValue ?waveform_type_value .
	BIND(STR(?waveform_type_value) AS ?Waveform_Type) .
}
?nozzle_usage ampo:equipment ?nozzle .
?nozzle_usage ampo:requiresInput ?nozzle_temp_input .
?nozzle_temp_input a :ActuatorNozzle_HeaterBlockTemperature .
?nozzle_temp_input qudt:quantityValue ?nozzle_temp_QV .
?nozzle_temp_QV qudt:numericValue ?nozzle_temp .
BIND ( STR(?nozzle_temp) AS ?Nozzle_Temp ) .
?step ampo:produces ?droplet .
?droplet a :Droplet .
OPTIONAL {?droplet rdfs:label ?droplet_label . }
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_ejected_attr . 
	?droplet_ejected_attr a :Droplet_Ejected .
	?droplet_ejected_attr rdf:value ?droplet_ejected .
	BIND ( STR(?droplet_ejected) AS ?Droplet_Ejected) .
}
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_visible_attr . 
	?droplet_visible_attr a :Droplet_Visible .
	?droplet_visible_attr rdf:value ?droplet_visible . 
	BIND ( STR(?droplet_visible) AS ?Droplet_Visible) .
}
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_tail_attr . 
	?droplet_tail_attr a :Droplet_Tail .
	?droplet_tail_attr rdf:value ?droplet_tail . 
	BIND ( STR(?droplet_tail) AS ?Droplet_Tail) .
}
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_satellites_attr . 
	?droplet_satellites_attr a :Droplet_Satellites .
	?droplet_satellites_attr rdf:value ?droplet_satellites . 
	BIND ( STR(?droplet_satellites) AS ?Droplet_Satellites) .
}
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_t1_attr . 
	?droplet_t1_attr a :Droplet_TimeFrame_1 .
	?droplet_t1_attr qudt:quantityValue ?droplet_t1_QV . 
	?droplet_t1_QV qudt:numericValue ?droplet_t1 .
	BIND ( STR(?droplet_t1) AS ?Droplet_T1) .

}
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_t2_attr . 
	?droplet_t2_attr a :Droplet_TimeFrame_2 .
	?droplet_t2_attr qudt:quantityValue ?droplet_t2_QV . 
	?droplet_t2_QV qudt:numericValue ?droplet_t2 .
	BIND ( STR(?droplet_t2) AS ?Droplet_T2) .
}
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_diameter_attr . 
	?droplet_diameter_attr a :Droplet_Diameter .
	?droplet_diameter_attr qudt:quantityValue ?droplet_diameter_QV . 
	?droplet_diameter_QV qudt:numericValue ?droplet_diameter .
	BIND ( STR(?droplet_diameter) AS ?Droplet_Diameter) .
}
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_velocity_attr . 
	?droplet_velocity_attr a :Droplet_Velocity .
	?droplet_velocity_attr qudt:quantityValue ?droplet_velocity_QV . 
	?droplet_velocity_QV qudt:numericValue ?droplet_velocity .
	BIND ( STR(?droplet_velocity) AS ?Droplet_Velocity) .
}
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_distance_traveled_attr . 
	?droplet_distance_traveled_attr a :Droplet_DistanceTraveled .
	?droplet_distance_traveled_attr qudt:quantityValue ?droplet_distance_traveled_QV . 
	?droplet_distance_traveled_QV qudt:numericValue ?droplet_distance_traveled .
	BIND ( STR(?droplet_distance_traveled) AS ?Droplet_Distance_Traveled) .
}
?step ampo:hasParticipant ?ink .
?ink a ampo-ink:Ink .
?ink rdfs:label ?ink_label .
BIND ( STR(?ink_label) AS ?Ink) .
FILTER (STR(?waveform_type_value) = "Sine Waveform") .
FILTER ( ?droplet_ejected ) .
FILTER ( !(?droplet_satellites) ) .
FILTER ( !(?droplet_tail) ) .
}
ORDER BY ?ink_label
```

### (3) Select Trigger Waveforms that 
	(a) ejected a droplet
	(b) did not produce a satellite droplet
	(c) did not produce a tail 
	(d) have a unipolar waveform

```
prefix : <https://tw.rpi.edu/web/project/ampo-ink#> 
prefix owl: <http://www.w3.org/2002/07/owl#> 
prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
prefix sio: <http://semanticscience.org/resource/> 
prefix xml: <http://www.w3.org/XML/1998/namespace> 
prefix xsd: <http://www.w3.org/2001/XMLSchema#> 
prefix ampo: <https://tw.rpi.edu/web/project/ampo#> 
prefix ampo-ink: <https://tw.rpi.edu/web/project/ampo-ink#> 
prefix foaf: <http://xmlns.com/foaf/0.1/> 
prefix prov: <http://www.w3.org/ns/prov#> 
prefix qudt: <http://data.nasa.gov/qudt/owl/qudt#> 
prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
prefix dcterms: <http://purl.org/dc/terms/> 
prefix qudt-unit: <http://qudt.org/1.1/vocab/unit#> 

SELECT ?Trigger_Waveform ?Rise_Time ?Dwell_Time ?Fall_Time ?Echo_Time ?Final_Rise_Time 
?Max_Voltage_Amplitude ?Min_Voltage_Amplitude ?Period ?Idle_Voltage ?Amplitude ?Waveform_Type
?nozzle ?Nozzle_Temp 
?Droplet_Ejected ?Droplet_Visible ?Droplet_Tail ?Droplet_Satellites
?Droplet_T1 ?Droplet_T2 ?Droplet_Diameter ?Droplet_Velocity ?Droplet_Distance_Traveled ?Ink
WHERE { 
?step rdf:type :MaterialDeposition .
?step ampo:qualifiedEquipmentUsage ?nozzle_usage .
?nozzle_usage ampo:requiresInput ?subject .
?subject rdf:type :Actuator_DropletActuation .
?subject rdfs:label ?subject_label .
BIND( STR(?subject_label) AS ?Trigger_Waveform ) .
OPTIONAL {
    ?subject ampo:hasAttribute ?rise_time .
	?rise_time rdf:type :DropletActuation_RiseTime .
	?rise_time qudt:quantityValue ?rise_time_QV .
	?rise_time_QV qudt:numericValue ?rise_time_value .
	BIND(STR(?rise_time_value) AS ?Rise_Time) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?dwell_time .
	?dwell_time rdf:type :DropletActuation_DwellTime .
	?dwell_time qudt:quantityValue ?dwell_time_QV .
	?dwell_time_QV qudt:numericValue ?dwell_time_value .
	BIND(STR(?dwell_time_value) AS ?Dwell_Time) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?fall_time .
	?fall_time rdf:type :DropletActuation_FallTime .
	?fall_time qudt:quantityValue ?fall_time_QV .
	?fall_time_QV qudt:numericValue ?fall_time_value .
	BIND(STR(?fall_time_value) AS ?Fall_Time) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?echo_time .
	?echo_time rdf:type :DropletActuation_EchoTime .
	?echo_time qudt:quantityValue ?echo_time_QV .
	?echo_time_QV qudt:numericValue ?echo_time_value .
	BIND(STR(?echo_time_value) AS ?Echo_Time) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?final_rise_time .
	?final_rise_time rdf:type :DropletActuation_FinalRiseTime .
	?final_rise_time qudt:quantityValue ?final_rise_time_QV .
	?final_rise_time_QV qudt:numericValue ?final_rise_time_value .
	BIND(STR(?final_rise_time_value) AS ?Final_Rise_Time) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?max_voltage_amplitude .
	?max_voltage_amplitude rdf:type :DropletActuation_MaxVoltageAmplitude .
	?max_voltage_amplitude qudt:quantityValue ?max_voltage_amplitude_QV .
	?max_voltage_amplitude_QV qudt:numericValue ?max_voltage_amplitude_value .
	BIND(STR(?max_voltage_amplitude_value) AS ?Max_Voltage_Amplitude) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?min_voltage_amplitude .
	?min_voltage_amplitude rdf:type :DropletActuation_MinVoltageAmplitude .
	?min_voltage_amplitude qudt:quantityValue ?min_voltage_amplitude_QV .
	?min_voltage_amplitude_QV qudt:numericValue ?min_voltage_amplitude_value .
	BIND(STR(?min_voltage_amplitude_value) AS ?Min_Voltage_Amplitude) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?period .
	?period rdf:type :DropletActuation_Period .
	?period qudt:quantityValue ?period_QV .
	?period_QV qudt:numericValue ?period_value .
	BIND(STR(?period_value) AS ?Period) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?amplitude .
	?amplitude rdf:type :DropletActuation_Amplitude .
	?amplitude qudt:quantityValue ?amplitude_QV .
	?amplitude_QV qudt:numericValue ?amplitude_value .
	BIND(STR(?amplitude_value) AS ?Amplitude) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?idle_voltage .
	?idle_voltage rdf:type :DropletActuation_IdleVoltage .
	?idle_voltage qudt:quantityValue ?idle_voltage_QV .
	?idle_voltage_QV qudt:numericValue ?idle_voltage_value .
	BIND(STR(?idle_voltage_value) AS ?Idle_Voltage) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?line_type .
	?line_type rdf:type :DropletActuation_LineType .
	?line_type ampo:descriptiveValue ?line_type_value .
	BIND(STR(?line_type_value) AS ?Line_Type) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?waveform_type .
	?waveform_type rdf:type :DropletActuation_WaveformType .
	?waveform_type ampo:descriptiveValue ?waveform_type_value .
	BIND(STR(?waveform_type_value) AS ?Waveform_Type) .
}
?nozzle_usage ampo:equipment ?nozzle .
?nozzle_usage ampo:requiresInput ?nozzle_temp_input .
?nozzle_temp_input a :ActuatorNozzle_HeaterBlockTemperature .
?nozzle_temp_input qudt:quantityValue ?nozzle_temp_QV .
?nozzle_temp_QV qudt:numericValue ?nozzle_temp .
BIND ( STR(?nozzle_temp) AS ?Nozzle_Temp ) .
?step ampo:produces ?droplet .
?droplet a :Droplet .
OPTIONAL {?droplet rdfs:label ?droplet_label . }
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_ejected_attr . 
	?droplet_ejected_attr a :Droplet_Ejected .
	?droplet_ejected_attr rdf:value ?droplet_ejected .
	BIND ( STR(?droplet_ejected) AS ?Droplet_Ejected) .
}
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_visible_attr . 
	?droplet_visible_attr a :Droplet_Visible .
	?droplet_visible_attr rdf:value ?droplet_visible . 
	BIND ( STR(?droplet_visible) AS ?Droplet_Visible) .
}
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_tail_attr . 
	?droplet_tail_attr a :Droplet_Tail .
	?droplet_tail_attr rdf:value ?droplet_tail . 
	BIND ( STR(?droplet_tail) AS ?Droplet_Tail) .
}
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_satellites_attr . 
	?droplet_satellites_attr a :Droplet_Satellites .
	?droplet_satellites_attr rdf:value ?droplet_satellites . 
	BIND ( STR(?droplet_satellites) AS ?Droplet_Satellites) .
}
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_t1_attr . 
	?droplet_t1_attr a :Droplet_TimeFrame_1 .
	?droplet_t1_attr qudt:quantityValue ?droplet_t1_QV . 
	?droplet_t1_QV qudt:numericValue ?droplet_t1 .
	BIND ( STR(?droplet_t1) AS ?Droplet_T1) .

}
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_t2_attr . 
	?droplet_t2_attr a :Droplet_TimeFrame_2 .
	?droplet_t2_attr qudt:quantityValue ?droplet_t2_QV . 
	?droplet_t2_QV qudt:numericValue ?droplet_t2 .
	BIND ( STR(?droplet_t2) AS ?Droplet_T2) .
}
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_diameter_attr . 
	?droplet_diameter_attr a :Droplet_Diameter .
	?droplet_diameter_attr qudt:quantityValue ?droplet_diameter_QV . 
	?droplet_diameter_QV qudt:numericValue ?droplet_diameter .
	BIND ( STR(?droplet_diameter) AS ?Droplet_Diameter) .
}
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_velocity_attr . 
	?droplet_velocity_attr a :Droplet_Velocity .
	?droplet_velocity_attr qudt:quantityValue ?droplet_velocity_QV . 
	?droplet_velocity_QV qudt:numericValue ?droplet_velocity .
	BIND ( STR(?droplet_velocity) AS ?Droplet_Velocity) .
}
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_distance_traveled_attr . 
	?droplet_distance_traveled_attr a :Droplet_DistanceTraveled .
	?droplet_distance_traveled_attr qudt:quantityValue ?droplet_distance_traveled_QV . 
	?droplet_distance_traveled_QV qudt:numericValue ?droplet_distance_traveled .
	BIND ( STR(?droplet_distance_traveled) AS ?Droplet_Distance_Traveled) .
}
?step ampo:hasParticipant ?ink .
?ink a ampo-ink:Ink .
?ink rdfs:label ?ink_label .
BIND ( STR(?ink_label) AS ?Ink) .
FILTER (STR(?waveform_type_value) = "Unipolar Waveform") .
FILTER ( ?droplet_ejected ) .
FILTER ( !(?droplet_satellites) ) .
FILTER ( !(?droplet_tail) ) .
}
ORDER BY ?ink_label
```

### (4) Select Trigger Waveforms that 
	(a) ejected a droplet
	(b) did not produce a satellite droplet
	(c) did not produce a tail 
	(d) have an unsymmetric bipolar waveform
	
```
prefix : <https://tw.rpi.edu/web/project/ampo-ink#> 
prefix owl: <http://www.w3.org/2002/07/owl#> 
prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
prefix sio: <http://semanticscience.org/resource/> 
prefix xml: <http://www.w3.org/XML/1998/namespace> 
prefix xsd: <http://www.w3.org/2001/XMLSchema#> 
prefix ampo: <https://tw.rpi.edu/web/project/ampo#> 
prefix ampo-ink: <https://tw.rpi.edu/web/project/ampo-ink#> 
prefix foaf: <http://xmlns.com/foaf/0.1/> 
prefix prov: <http://www.w3.org/ns/prov#> 
prefix qudt: <http://data.nasa.gov/qudt/owl/qudt#> 
prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
prefix dcterms: <http://purl.org/dc/terms/> 
prefix qudt-unit: <http://qudt.org/1.1/vocab/unit#> 

SELECT ?Trigger_Waveform ?Rise_Time ?Dwell_Time ?Fall_Time ?Echo_Time ?Final_Rise_Time 
?Max_Voltage_Amplitude ?Min_Voltage_Amplitude ?Period ?Idle_Voltage ?Amplitude ?Waveform_Type
?nozzle ?Nozzle_Temp 
?Droplet_Ejected ?Droplet_Visible ?Droplet_Tail ?Droplet_Satellites
?Droplet_T1 ?Droplet_T2 ?Droplet_Diameter ?Droplet_Velocity ?Droplet_Distance_Traveled ?Ink
WHERE { 
?step rdf:type :MaterialDeposition .
?step ampo:qualifiedEquipmentUsage ?nozzle_usage .
?nozzle_usage ampo:requiresInput ?subject .
?subject rdf:type :Actuator_DropletActuation .
?subject rdfs:label ?subject_label .
BIND( STR(?subject_label) AS ?Trigger_Waveform ) .
OPTIONAL {
    ?subject ampo:hasAttribute ?rise_time .
	?rise_time rdf:type :DropletActuation_RiseTime .
	?rise_time qudt:quantityValue ?rise_time_QV .
	?rise_time_QV qudt:numericValue ?rise_time_value .
	BIND(STR(?rise_time_value) AS ?Rise_Time) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?dwell_time .
	?dwell_time rdf:type :DropletActuation_DwellTime .
	?dwell_time qudt:quantityValue ?dwell_time_QV .
	?dwell_time_QV qudt:numericValue ?dwell_time_value .
	BIND(STR(?dwell_time_value) AS ?Dwell_Time) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?fall_time .
	?fall_time rdf:type :DropletActuation_FallTime .
	?fall_time qudt:quantityValue ?fall_time_QV .
	?fall_time_QV qudt:numericValue ?fall_time_value .
	BIND(STR(?fall_time_value) AS ?Fall_Time) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?echo_time .
	?echo_time rdf:type :DropletActuation_EchoTime .
	?echo_time qudt:quantityValue ?echo_time_QV .
	?echo_time_QV qudt:numericValue ?echo_time_value .
	BIND(STR(?echo_time_value) AS ?Echo_Time) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?final_rise_time .
	?final_rise_time rdf:type :DropletActuation_FinalRiseTime .
	?final_rise_time qudt:quantityValue ?final_rise_time_QV .
	?final_rise_time_QV qudt:numericValue ?final_rise_time_value .
	BIND(STR(?final_rise_time_value) AS ?Final_Rise_Time) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?max_voltage_amplitude .
	?max_voltage_amplitude rdf:type :DropletActuation_MaxVoltageAmplitude .
	?max_voltage_amplitude qudt:quantityValue ?max_voltage_amplitude_QV .
	?max_voltage_amplitude_QV qudt:numericValue ?max_voltage_amplitude_value .
	BIND(STR(?max_voltage_amplitude_value) AS ?Max_Voltage_Amplitude) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?min_voltage_amplitude .
	?min_voltage_amplitude rdf:type :DropletActuation_MinVoltageAmplitude .
	?min_voltage_amplitude qudt:quantityValue ?min_voltage_amplitude_QV .
	?min_voltage_amplitude_QV qudt:numericValue ?min_voltage_amplitude_value .
	BIND(STR(?min_voltage_amplitude_value) AS ?Min_Voltage_Amplitude) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?period .
	?period rdf:type :DropletActuation_Period .
	?period qudt:quantityValue ?period_QV .
	?period_QV qudt:numericValue ?period_value .
	BIND(STR(?period_value) AS ?Period) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?amplitude .
	?amplitude rdf:type :DropletActuation_Amplitude .
	?amplitude qudt:quantityValue ?amplitude_QV .
	?amplitude_QV qudt:numericValue ?amplitude_value .
	BIND(STR(?amplitude_value) AS ?Amplitude) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?idle_voltage .
	?idle_voltage rdf:type :DropletActuation_IdleVoltage .
	?idle_voltage qudt:quantityValue ?idle_voltage_QV .
	?idle_voltage_QV qudt:numericValue ?idle_voltage_value .
	BIND(STR(?idle_voltage_value) AS ?Idle_Voltage) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?line_type .
	?line_type rdf:type :DropletActuation_LineType .
	?line_type ampo:descriptiveValue ?line_type_value .
	BIND(STR(?line_type_value) AS ?Line_Type) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?waveform_type .
	?waveform_type rdf:type :DropletActuation_WaveformType .
	?waveform_type ampo:descriptiveValue ?waveform_type_value .
	BIND(STR(?waveform_type_value) AS ?Waveform_Type) .
}
?nozzle_usage ampo:equipment ?nozzle .
?nozzle_usage ampo:requiresInput ?nozzle_temp_input .
?nozzle_temp_input a :ActuatorNozzle_HeaterBlockTemperature .
?nozzle_temp_input qudt:quantityValue ?nozzle_temp_QV .
?nozzle_temp_QV qudt:numericValue ?nozzle_temp .
BIND ( STR(?nozzle_temp) AS ?Nozzle_Temp ) .
?step ampo:produces ?droplet .
?droplet a :Droplet .
OPTIONAL {?droplet rdfs:label ?droplet_label . }
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_ejected_attr . 
	?droplet_ejected_attr a :Droplet_Ejected .
	?droplet_ejected_attr rdf:value ?droplet_ejected .
	BIND ( STR(?droplet_ejected) AS ?Droplet_Ejected) .
}
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_visible_attr . 
	?droplet_visible_attr a :Droplet_Visible .
	?droplet_visible_attr rdf:value ?droplet_visible . 
	BIND ( STR(?droplet_visible) AS ?Droplet_Visible) .
}
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_tail_attr . 
	?droplet_tail_attr a :Droplet_Tail .
	?droplet_tail_attr rdf:value ?droplet_tail . 
	BIND ( STR(?droplet_tail) AS ?Droplet_Tail) .
}
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_satellites_attr . 
	?droplet_satellites_attr a :Droplet_Satellites .
	?droplet_satellites_attr rdf:value ?droplet_satellites . 
	BIND ( STR(?droplet_satellites) AS ?Droplet_Satellites) .
}
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_t1_attr . 
	?droplet_t1_attr a :Droplet_TimeFrame_1 .
	?droplet_t1_attr qudt:quantityValue ?droplet_t1_QV . 
	?droplet_t1_QV qudt:numericValue ?droplet_t1 .
	BIND ( STR(?droplet_t1) AS ?Droplet_T1) .

}
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_t2_attr . 
	?droplet_t2_attr a :Droplet_TimeFrame_2 .
	?droplet_t2_attr qudt:quantityValue ?droplet_t2_QV . 
	?droplet_t2_QV qudt:numericValue ?droplet_t2 .
	BIND ( STR(?droplet_t2) AS ?Droplet_T2) .
}
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_diameter_attr . 
	?droplet_diameter_attr a :Droplet_Diameter .
	?droplet_diameter_attr qudt:quantityValue ?droplet_diameter_QV . 
	?droplet_diameter_QV qudt:numericValue ?droplet_diameter .
	BIND ( STR(?droplet_diameter) AS ?Droplet_Diameter) .
}
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_velocity_attr . 
	?droplet_velocity_attr a :Droplet_Velocity .
	?droplet_velocity_attr qudt:quantityValue ?droplet_velocity_QV . 
	?droplet_velocity_QV qudt:numericValue ?droplet_velocity .
	BIND ( STR(?droplet_velocity) AS ?Droplet_Velocity) .
}
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_distance_traveled_attr . 
	?droplet_distance_traveled_attr a :Droplet_DistanceTraveled .
	?droplet_distance_traveled_attr qudt:quantityValue ?droplet_distance_traveled_QV . 
	?droplet_distance_traveled_QV qudt:numericValue ?droplet_distance_traveled .
	BIND ( STR(?droplet_distance_traveled) AS ?Droplet_Distance_Traveled) .
}
?step ampo:hasParticipant ?ink .
?ink a ampo-ink:Ink .
?ink rdfs:label ?ink_label .
BIND ( STR(?ink_label) AS ?Ink) .
FILTER (STR(?waveform_type_value) = "Unsymmetric Bipolar Waveform") .
FILTER ( ?droplet_ejected ) .
FILTER ( !(?droplet_satellites) ) .
FILTER ( !(?droplet_tail) ) .
}
ORDER BY ?ink_label
```

### (5) Select Trigger Waveforms that resulted in:
    (a) droplet that was ejected and 
    (b) droplet velocity less than 2 m/s
    (c) Bin based on Waveform pattern (Symmetric Bipolar, Sine, Unipolar, Unsymmetric Bipolar)
    
```
prefix : <https://tw.rpi.edu/web/project/ampo-ink#> 
prefix owl: <http://www.w3.org/2002/07/owl#> 
prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
prefix sio: <http://semanticscience.org/resource/> 
prefix xml: <http://www.w3.org/XML/1998/namespace> 
prefix xsd: <http://www.w3.org/2001/XMLSchema#> 
prefix ampo: <https://tw.rpi.edu/web/project/ampo#> 
prefix ampo-ink: <https://tw.rpi.edu/web/project/ampo-ink#> 
prefix foaf: <http://xmlns.com/foaf/0.1/> 
prefix prov: <http://www.w3.org/ns/prov#> 
prefix qudt: <http://data.nasa.gov/qudt/owl/qudt#> 
prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
prefix dcterms: <http://purl.org/dc/terms/> 
prefix qudt-unit: <http://qudt.org/1.1/vocab/unit#> 

SELECT ?Trigger_Waveform ?Rise_Time ?Dwell_Time ?Fall_Time ?Echo_Time ?Final_Rise_Time 
?Max_Voltage_Amplitude ?Min_Voltage_Amplitude ?Period ?Idle_Voltage ?Amplitude ?Waveform_Type
?nozzle ?Nozzle_Temp 
?Droplet_Ejected ?Droplet_Visible ?Droplet_Tail ?Droplet_Satellites
?Droplet_T1 ?Droplet_T2 ?Droplet_Diameter ?Droplet_Velocity ?Droplet_Distance_Traveled ?Ink
WHERE { 
?step rdf:type :MaterialDeposition .
?step ampo:qualifiedEquipmentUsage ?nozzle_usage .
?nozzle_usage ampo:requiresInput ?subject .
?subject rdf:type :Actuator_DropletActuation .
?subject rdfs:label ?subject_label .
BIND( STR(?subject_label) AS ?Trigger_Waveform ) .
OPTIONAL {
    ?subject ampo:hasAttribute ?rise_time .
	?rise_time rdf:type :DropletActuation_RiseTime .
	?rise_time qudt:quantityValue ?rise_time_QV .
	?rise_time_QV qudt:numericValue ?rise_time_value .
	BIND(STR(?rise_time_value) AS ?Rise_Time) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?dwell_time .
	?dwell_time rdf:type :DropletActuation_DwellTime .
	?dwell_time qudt:quantityValue ?dwell_time_QV .
	?dwell_time_QV qudt:numericValue ?dwell_time_value .
	BIND(STR(?dwell_time_value) AS ?Dwell_Time) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?fall_time .
	?fall_time rdf:type :DropletActuation_FallTime .
	?fall_time qudt:quantityValue ?fall_time_QV .
	?fall_time_QV qudt:numericValue ?fall_time_value .
	BIND(STR(?fall_time_value) AS ?Fall_Time) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?echo_time .
	?echo_time rdf:type :DropletActuation_EchoTime .
	?echo_time qudt:quantityValue ?echo_time_QV .
	?echo_time_QV qudt:numericValue ?echo_time_value .
	BIND(STR(?echo_time_value) AS ?Echo_Time) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?final_rise_time .
	?final_rise_time rdf:type :DropletActuation_FinalRiseTime .
	?final_rise_time qudt:quantityValue ?final_rise_time_QV .
	?final_rise_time_QV qudt:numericValue ?final_rise_time_value .
	BIND(STR(?final_rise_time_value) AS ?Final_Rise_Time) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?max_voltage_amplitude .
	?max_voltage_amplitude rdf:type :DropletActuation_MaxVoltageAmplitude .
	?max_voltage_amplitude qudt:quantityValue ?max_voltage_amplitude_QV .
	?max_voltage_amplitude_QV qudt:numericValue ?max_voltage_amplitude_value .
	BIND(STR(?max_voltage_amplitude_value) AS ?Max_Voltage_Amplitude) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?min_voltage_amplitude .
	?min_voltage_amplitude rdf:type :DropletActuation_MinVoltageAmplitude .
	?min_voltage_amplitude qudt:quantityValue ?min_voltage_amplitude_QV .
	?min_voltage_amplitude_QV qudt:numericValue ?min_voltage_amplitude_value .
	BIND(STR(?min_voltage_amplitude_value) AS ?Min_Voltage_Amplitude) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?period .
	?period rdf:type :DropletActuation_Period .
	?period qudt:quantityValue ?period_QV .
	?period_QV qudt:numericValue ?period_value .
	BIND(STR(?period_value) AS ?Period) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?amplitude .
	?amplitude rdf:type :DropletActuation_Amplitude .
	?amplitude qudt:quantityValue ?amplitude_QV .
	?amplitude_QV qudt:numericValue ?amplitude_value .
	BIND(STR(?amplitude_value) AS ?Amplitude) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?idle_voltage .
	?idle_voltage rdf:type :DropletActuation_IdleVoltage .
	?idle_voltage qudt:quantityValue ?idle_voltage_QV .
	?idle_voltage_QV qudt:numericValue ?idle_voltage_value .
	BIND(STR(?idle_voltage_value) AS ?Idle_Voltage) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?line_type .
	?line_type rdf:type :DropletActuation_LineType .
	?line_type ampo:descriptiveValue ?line_type_value .
	BIND(STR(?line_type_value) AS ?Line_Type) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?waveform_type .
	?waveform_type rdf:type :DropletActuation_WaveformType .
	?waveform_type ampo:descriptiveValue ?waveform_type_value .
	BIND(STR(?waveform_type_value) AS ?Waveform_Type) .
}
?nozzle_usage ampo:equipment ?nozzle .
?nozzle_usage ampo:requiresInput ?nozzle_temp_input .
?nozzle_temp_input a :ActuatorNozzle_HeaterBlockTemperature .
?nozzle_temp_input qudt:quantityValue ?nozzle_temp_QV .
?nozzle_temp_QV qudt:numericValue ?nozzle_temp .
BIND ( STR(?nozzle_temp) AS ?Nozzle_Temp ) .
?step ampo:produces ?droplet .
?droplet a :Droplet .
OPTIONAL {?droplet rdfs:label ?droplet_label . }
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_ejected_attr . 
	?droplet_ejected_attr a :Droplet_Ejected .
	?droplet_ejected_attr rdf:value ?droplet_ejected .
	BIND ( STR(?droplet_ejected) AS ?Droplet_Ejected) .
}
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_visible_attr . 
	?droplet_visible_attr a :Droplet_Visible .
	?droplet_visible_attr rdf:value ?droplet_visible . 
	BIND ( STR(?droplet_visible) AS ?Droplet_Visible) .
}
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_tail_attr . 
	?droplet_tail_attr a :Droplet_Tail .
	?droplet_tail_attr rdf:value ?droplet_tail . 
	BIND ( STR(?droplet_tail) AS ?Droplet_Tail) .
}
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_satellites_attr . 
	?droplet_satellites_attr a :Droplet_Satellites .
	?droplet_satellites_attr rdf:value ?droplet_satellites . 
	BIND ( STR(?droplet_satellites) AS ?Droplet_Satellites) .
}
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_t1_attr . 
	?droplet_t1_attr a :Droplet_TimeFrame_1 .
	?droplet_t1_attr qudt:quantityValue ?droplet_t1_QV . 
	?droplet_t1_QV qudt:numericValue ?droplet_t1 .
	BIND ( STR(?droplet_t1) AS ?Droplet_T1) .

}
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_t2_attr . 
	?droplet_t2_attr a :Droplet_TimeFrame_2 .
	?droplet_t2_attr qudt:quantityValue ?droplet_t2_QV . 
	?droplet_t2_QV qudt:numericValue ?droplet_t2 .
	BIND ( STR(?droplet_t2) AS ?Droplet_T2) .
}
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_diameter_attr . 
	?droplet_diameter_attr a :Droplet_Diameter .
	?droplet_diameter_attr qudt:quantityValue ?droplet_diameter_QV . 
	?droplet_diameter_QV qudt:numericValue ?droplet_diameter .
	BIND ( STR(?droplet_diameter) AS ?Droplet_Diameter) .
}
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_velocity_attr . 
	?droplet_velocity_attr a :Droplet_Velocity .
	?droplet_velocity_attr qudt:quantityValue ?droplet_velocity_QV . 
	?droplet_velocity_QV qudt:numericValue ?droplet_velocity .
	BIND ( STR(?droplet_velocity) AS ?Droplet_Velocity) .
}
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_distance_traveled_attr . 
	?droplet_distance_traveled_attr a :Droplet_DistanceTraveled .
	?droplet_distance_traveled_attr qudt:quantityValue ?droplet_distance_traveled_QV . 
	?droplet_distance_traveled_QV qudt:numericValue ?droplet_distance_traveled .
	BIND ( STR(?droplet_distance_traveled) AS ?Droplet_Distance_Traveled) .
}
?step ampo:hasParticipant ?ink .
?ink a ampo-ink:Ink .
?ink rdfs:label ?ink_label .
BIND ( STR(?ink_label) AS ?Ink) .
FILTER ( ?droplet_ejected ) .
FILTER ( ?droplet_velocity < 2 ) .
}
ORDER BY ?ink_label ?waveform_type_value
```
### (6) Select Trigger Waveform and Velocity values where:
	(a) droplet was ejected
	(b) satellite droplet formed OR 
    (c) tail formed
    (d) Bin based on Waveform pattern (Symmetric Bipolar, Sine, Unipolar, Unsymmetric Bipolar)
    
```
prefix : <https://tw.rpi.edu/web/project/ampo-ink#> 
prefix owl: <http://www.w3.org/2002/07/owl#> 
prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
prefix sio: <http://semanticscience.org/resource/> 
prefix xml: <http://www.w3.org/XML/1998/namespace> 
prefix xsd: <http://www.w3.org/2001/XMLSchema#> 
prefix ampo: <https://tw.rpi.edu/web/project/ampo#> 
prefix ampo-ink: <https://tw.rpi.edu/web/project/ampo-ink#> 
prefix foaf: <http://xmlns.com/foaf/0.1/> 
prefix prov: <http://www.w3.org/ns/prov#> 
prefix qudt: <http://data.nasa.gov/qudt/owl/qudt#> 
prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
prefix dcterms: <http://purl.org/dc/terms/> 
prefix qudt-unit: <http://qudt.org/1.1/vocab/unit#> 

SELECT ?Trigger_Waveform ?Rise_Time ?Dwell_Time ?Fall_Time ?Echo_Time ?Final_Rise_Time 
?Max_Voltage_Amplitude ?Min_Voltage_Amplitude ?Period ?Idle_Voltage ?Amplitude ?Waveform_Type
?nozzle ?Nozzle_Temp 
?Droplet_Ejected ?Droplet_Visible ?Droplet_Tail ?Droplet_Satellites
?Droplet_T1 ?Droplet_T2 ?Droplet_Diameter ?Droplet_Velocity ?Droplet_Distance_Traveled ?Ink
WHERE { 
?step rdf:type :MaterialDeposition .
?step ampo:qualifiedEquipmentUsage ?nozzle_usage .
?nozzle_usage ampo:requiresInput ?subject .
?subject rdf:type :Actuator_DropletActuation .
?subject rdfs:label ?subject_label .
BIND( STR(?subject_label) AS ?Trigger_Waveform ) .
OPTIONAL {
    ?subject ampo:hasAttribute ?rise_time .
	?rise_time rdf:type :DropletActuation_RiseTime .
	?rise_time qudt:quantityValue ?rise_time_QV .
	?rise_time_QV qudt:numericValue ?rise_time_value .
	BIND(STR(?rise_time_value) AS ?Rise_Time) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?dwell_time .
	?dwell_time rdf:type :DropletActuation_DwellTime .
	?dwell_time qudt:quantityValue ?dwell_time_QV .
	?dwell_time_QV qudt:numericValue ?dwell_time_value .
	BIND(STR(?dwell_time_value) AS ?Dwell_Time) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?fall_time .
	?fall_time rdf:type :DropletActuation_FallTime .
	?fall_time qudt:quantityValue ?fall_time_QV .
	?fall_time_QV qudt:numericValue ?fall_time_value .
	BIND(STR(?fall_time_value) AS ?Fall_Time) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?echo_time .
	?echo_time rdf:type :DropletActuation_EchoTime .
	?echo_time qudt:quantityValue ?echo_time_QV .
	?echo_time_QV qudt:numericValue ?echo_time_value .
	BIND(STR(?echo_time_value) AS ?Echo_Time) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?final_rise_time .
	?final_rise_time rdf:type :DropletActuation_FinalRiseTime .
	?final_rise_time qudt:quantityValue ?final_rise_time_QV .
	?final_rise_time_QV qudt:numericValue ?final_rise_time_value .
	BIND(STR(?final_rise_time_value) AS ?Final_Rise_Time) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?max_voltage_amplitude .
	?max_voltage_amplitude rdf:type :DropletActuation_MaxVoltageAmplitude .
	?max_voltage_amplitude qudt:quantityValue ?max_voltage_amplitude_QV .
	?max_voltage_amplitude_QV qudt:numericValue ?max_voltage_amplitude_value .
	BIND(STR(?max_voltage_amplitude_value) AS ?Max_Voltage_Amplitude) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?min_voltage_amplitude .
	?min_voltage_amplitude rdf:type :DropletActuation_MinVoltageAmplitude .
	?min_voltage_amplitude qudt:quantityValue ?min_voltage_amplitude_QV .
	?min_voltage_amplitude_QV qudt:numericValue ?min_voltage_amplitude_value .
	BIND(STR(?min_voltage_amplitude_value) AS ?Min_Voltage_Amplitude) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?period .
	?period rdf:type :DropletActuation_Period .
	?period qudt:quantityValue ?period_QV .
	?period_QV qudt:numericValue ?period_value .
	BIND(STR(?period_value) AS ?Period) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?amplitude .
	?amplitude rdf:type :DropletActuation_Amplitude .
	?amplitude qudt:quantityValue ?amplitude_QV .
	?amplitude_QV qudt:numericValue ?amplitude_value .
	BIND(STR(?amplitude_value) AS ?Amplitude) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?idle_voltage .
	?idle_voltage rdf:type :DropletActuation_IdleVoltage .
	?idle_voltage qudt:quantityValue ?idle_voltage_QV .
	?idle_voltage_QV qudt:numericValue ?idle_voltage_value .
	BIND(STR(?idle_voltage_value) AS ?Idle_Voltage) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?line_type .
	?line_type rdf:type :DropletActuation_LineType .
	?line_type ampo:descriptiveValue ?line_type_value .
	BIND(STR(?line_type_value) AS ?Line_Type) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?waveform_type .
	?waveform_type rdf:type :DropletActuation_WaveformType .
	?waveform_type ampo:descriptiveValue ?waveform_type_value .
	BIND(STR(?waveform_type_value) AS ?Waveform_Type) .
}
?nozzle_usage ampo:equipment ?nozzle .
?nozzle_usage ampo:requiresInput ?nozzle_temp_input .
?nozzle_temp_input a :ActuatorNozzle_HeaterBlockTemperature .
?nozzle_temp_input qudt:quantityValue ?nozzle_temp_QV .
?nozzle_temp_QV qudt:numericValue ?nozzle_temp .
BIND ( STR(?nozzle_temp) AS ?Nozzle_Temp ) .
?step ampo:produces ?droplet .
?droplet a :Droplet .
OPTIONAL {?droplet rdfs:label ?droplet_label . }
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_ejected_attr . 
	?droplet_ejected_attr a :Droplet_Ejected .
	?droplet_ejected_attr rdf:value ?droplet_ejected .
	BIND ( STR(?droplet_ejected) AS ?Droplet_Ejected) .
}
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_visible_attr . 
	?droplet_visible_attr a :Droplet_Visible .
	?droplet_visible_attr rdf:value ?droplet_visible . 
	BIND ( STR(?droplet_visible) AS ?Droplet_Visible) .
}
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_tail_attr . 
	?droplet_tail_attr a :Droplet_Tail .
	?droplet_tail_attr rdf:value ?droplet_tail . 
	BIND ( STR(?droplet_tail) AS ?Droplet_Tail) .
}
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_satellites_attr . 
	?droplet_satellites_attr a :Droplet_Satellites .
	?droplet_satellites_attr rdf:value ?droplet_satellites . 
	BIND ( STR(?droplet_satellites) AS ?Droplet_Satellites) .
}
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_t1_attr . 
	?droplet_t1_attr a :Droplet_TimeFrame_1 .
	?droplet_t1_attr qudt:quantityValue ?droplet_t1_QV . 
	?droplet_t1_QV qudt:numericValue ?droplet_t1 .
	BIND ( STR(?droplet_t1) AS ?Droplet_T1) .

}
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_t2_attr . 
	?droplet_t2_attr a :Droplet_TimeFrame_2 .
	?droplet_t2_attr qudt:quantityValue ?droplet_t2_QV . 
	?droplet_t2_QV qudt:numericValue ?droplet_t2 .
	BIND ( STR(?droplet_t2) AS ?Droplet_T2) .
}
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_diameter_attr . 
	?droplet_diameter_attr a :Droplet_Diameter .
	?droplet_diameter_attr qudt:quantityValue ?droplet_diameter_QV . 
	?droplet_diameter_QV qudt:numericValue ?droplet_diameter .
	BIND ( STR(?droplet_diameter) AS ?Droplet_Diameter) .
}
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_velocity_attr . 
	?droplet_velocity_attr a :Droplet_Velocity .
	?droplet_velocity_attr qudt:quantityValue ?droplet_velocity_QV . 
	?droplet_velocity_QV qudt:numericValue ?droplet_velocity .
	BIND ( STR(?droplet_velocity) AS ?Droplet_Velocity) .
}
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_distance_traveled_attr . 
	?droplet_distance_traveled_attr a :Droplet_DistanceTraveled .
	?droplet_distance_traveled_attr qudt:quantityValue ?droplet_distance_traveled_QV . 
	?droplet_distance_traveled_QV qudt:numericValue ?droplet_distance_traveled .
	BIND ( STR(?droplet_distance_traveled) AS ?Droplet_Distance_Traveled) .
}
?step ampo:hasParticipant ?ink .
?ink a ampo-ink:Ink .
?ink rdfs:label ?ink_label .
BIND ( STR(?ink_label) AS ?Ink) .
FILTER ( ?droplet_ejected ) .
FILTER ( ?droplet_satellites || ?droplet_tail ) .
}
ORDER BY ?ink_label ?waveform_type_value
```

### (7) Select all Trigger Waveforms where droplet was NOT ejected for each ink
    (a) Bin based on Waveform pattern (Symmetric Bipolar, Sine, Unipolar, Unsymmetric Bipolar).
    
```
prefix : <https://tw.rpi.edu/web/project/ampo-ink#> 
prefix owl: <http://www.w3.org/2002/07/owl#> 
prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
prefix sio: <http://semanticscience.org/resource/> 
prefix xml: <http://www.w3.org/XML/1998/namespace> 
prefix xsd: <http://www.w3.org/2001/XMLSchema#> 
prefix ampo: <https://tw.rpi.edu/web/project/ampo#> 
prefix ampo-ink: <https://tw.rpi.edu/web/project/ampo-ink#> 
prefix foaf: <http://xmlns.com/foaf/0.1/> 
prefix prov: <http://www.w3.org/ns/prov#> 
prefix qudt: <http://data.nasa.gov/qudt/owl/qudt#> 
prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
prefix dcterms: <http://purl.org/dc/terms/> 
prefix qudt-unit: <http://qudt.org/1.1/vocab/unit#> 

SELECT ?Trigger_Waveform ?Rise_Time ?Dwell_Time ?Fall_Time ?Echo_Time ?Final_Rise_Time 
?Max_Voltage_Amplitude ?Min_Voltage_Amplitude ?Period ?Idle_Voltage ?Amplitude ?Waveform_Type
?nozzle ?Nozzle_Temp 
?Droplet_Ejected ?Droplet_Visible ?Droplet_Tail ?Droplet_Satellites
?Droplet_T1 ?Droplet_T2 ?Droplet_Diameter ?Droplet_Velocity ?Droplet_Distance_Traveled ?Ink
WHERE { 
?step rdf:type :MaterialDeposition .
?step ampo:qualifiedEquipmentUsage ?nozzle_usage .
?nozzle_usage ampo:requiresInput ?subject .
?subject rdf:type :Actuator_DropletActuation .
?subject rdfs:label ?subject_label .
BIND( STR(?subject_label) AS ?Trigger_Waveform ) .
OPTIONAL {
    ?subject ampo:hasAttribute ?rise_time .
	?rise_time rdf:type :DropletActuation_RiseTime .
	?rise_time qudt:quantityValue ?rise_time_QV .
	?rise_time_QV qudt:numericValue ?rise_time_value .
	BIND(STR(?rise_time_value) AS ?Rise_Time) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?dwell_time .
	?dwell_time rdf:type :DropletActuation_DwellTime .
	?dwell_time qudt:quantityValue ?dwell_time_QV .
	?dwell_time_QV qudt:numericValue ?dwell_time_value .
	BIND(STR(?dwell_time_value) AS ?Dwell_Time) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?fall_time .
	?fall_time rdf:type :DropletActuation_FallTime .
	?fall_time qudt:quantityValue ?fall_time_QV .
	?fall_time_QV qudt:numericValue ?fall_time_value .
	BIND(STR(?fall_time_value) AS ?Fall_Time) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?echo_time .
	?echo_time rdf:type :DropletActuation_EchoTime .
	?echo_time qudt:quantityValue ?echo_time_QV .
	?echo_time_QV qudt:numericValue ?echo_time_value .
	BIND(STR(?echo_time_value) AS ?Echo_Time) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?final_rise_time .
	?final_rise_time rdf:type :DropletActuation_FinalRiseTime .
	?final_rise_time qudt:quantityValue ?final_rise_time_QV .
	?final_rise_time_QV qudt:numericValue ?final_rise_time_value .
	BIND(STR(?final_rise_time_value) AS ?Final_Rise_Time) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?max_voltage_amplitude .
	?max_voltage_amplitude rdf:type :DropletActuation_MaxVoltageAmplitude .
	?max_voltage_amplitude qudt:quantityValue ?max_voltage_amplitude_QV .
	?max_voltage_amplitude_QV qudt:numericValue ?max_voltage_amplitude_value .
	BIND(STR(?max_voltage_amplitude_value) AS ?Max_Voltage_Amplitude) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?min_voltage_amplitude .
	?min_voltage_amplitude rdf:type :DropletActuation_MinVoltageAmplitude .
	?min_voltage_amplitude qudt:quantityValue ?min_voltage_amplitude_QV .
	?min_voltage_amplitude_QV qudt:numericValue ?min_voltage_amplitude_value .
	BIND(STR(?min_voltage_amplitude_value) AS ?Min_Voltage_Amplitude) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?period .
	?period rdf:type :DropletActuation_Period .
	?period qudt:quantityValue ?period_QV .
	?period_QV qudt:numericValue ?period_value .
	BIND(STR(?period_value) AS ?Period) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?amplitude .
	?amplitude rdf:type :DropletActuation_Amplitude .
	?amplitude qudt:quantityValue ?amplitude_QV .
	?amplitude_QV qudt:numericValue ?amplitude_value .
	BIND(STR(?amplitude_value) AS ?Amplitude) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?idle_voltage .
	?idle_voltage rdf:type :DropletActuation_IdleVoltage .
	?idle_voltage qudt:quantityValue ?idle_voltage_QV .
	?idle_voltage_QV qudt:numericValue ?idle_voltage_value .
	BIND(STR(?idle_voltage_value) AS ?Idle_Voltage) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?line_type .
	?line_type rdf:type :DropletActuation_LineType .
	?line_type ampo:descriptiveValue ?line_type_value .
	BIND(STR(?line_type_value) AS ?Line_Type) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?waveform_type .
	?waveform_type rdf:type :DropletActuation_WaveformType .
	?waveform_type ampo:descriptiveValue ?waveform_type_value .
	BIND(STR(?waveform_type_value) AS ?Waveform_Type) .
}
?nozzle_usage ampo:equipment ?nozzle .
?nozzle_usage ampo:requiresInput ?nozzle_temp_input .
?nozzle_temp_input a :ActuatorNozzle_HeaterBlockTemperature .
?nozzle_temp_input qudt:quantityValue ?nozzle_temp_QV .
?nozzle_temp_QV qudt:numericValue ?nozzle_temp .
BIND ( STR(?nozzle_temp) AS ?Nozzle_Temp ) .
?step ampo:produces ?droplet .
?droplet a :Droplet .
OPTIONAL {?droplet rdfs:label ?droplet_label . }
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_ejected_attr . 
	?droplet_ejected_attr a :Droplet_Ejected .
	?droplet_ejected_attr rdf:value ?droplet_ejected .
	BIND ( STR(?droplet_ejected) AS ?Droplet_Ejected) .
}
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_visible_attr . 
	?droplet_visible_attr a :Droplet_Visible .
	?droplet_visible_attr rdf:value ?droplet_visible . 
	BIND ( STR(?droplet_visible) AS ?Droplet_Visible) .
}
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_tail_attr . 
	?droplet_tail_attr a :Droplet_Tail .
	?droplet_tail_attr rdf:value ?droplet_tail . 
	BIND ( STR(?droplet_tail) AS ?Droplet_Tail) .
}
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_satellites_attr . 
	?droplet_satellites_attr a :Droplet_Satellites .
	?droplet_satellites_attr rdf:value ?droplet_satellites . 
	BIND ( STR(?droplet_satellites) AS ?Droplet_Satellites) .
}
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_t1_attr . 
	?droplet_t1_attr a :Droplet_TimeFrame_1 .
	?droplet_t1_attr qudt:quantityValue ?droplet_t1_QV . 
	?droplet_t1_QV qudt:numericValue ?droplet_t1 .
	BIND ( STR(?droplet_t1) AS ?Droplet_T1) .

}
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_t2_attr . 
	?droplet_t2_attr a :Droplet_TimeFrame_2 .
	?droplet_t2_attr qudt:quantityValue ?droplet_t2_QV . 
	?droplet_t2_QV qudt:numericValue ?droplet_t2 .
	BIND ( STR(?droplet_t2) AS ?Droplet_T2) .
}
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_diameter_attr . 
	?droplet_diameter_attr a :Droplet_Diameter .
	?droplet_diameter_attr qudt:quantityValue ?droplet_diameter_QV . 
	?droplet_diameter_QV qudt:numericValue ?droplet_diameter .
	BIND ( STR(?droplet_diameter) AS ?Droplet_Diameter) .
}
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_velocity_attr . 
	?droplet_velocity_attr a :Droplet_Velocity .
	?droplet_velocity_attr qudt:quantityValue ?droplet_velocity_QV . 
	?droplet_velocity_QV qudt:numericValue ?droplet_velocity .
	BIND ( STR(?droplet_velocity) AS ?Droplet_Velocity) .
}
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_distance_traveled_attr . 
	?droplet_distance_traveled_attr a :Droplet_DistanceTraveled .
	?droplet_distance_traveled_attr qudt:quantityValue ?droplet_distance_traveled_QV . 
	?droplet_distance_traveled_QV qudt:numericValue ?droplet_distance_traveled .
	BIND ( STR(?droplet_distance_traveled) AS ?Droplet_Distance_Traveled) .
}
?step ampo:hasParticipant ?ink .
?ink a ampo-ink:Ink .
?ink rdfs:label ?ink_label .
BIND ( STR(?ink_label) AS ?Ink) .
FILTER ( !?droplet_ejected ) .
}
ORDER BY ?ink_label ?waveform_type_value
```
### (8) Plot the droplet velocity (Dependent Variable - Z Axis), as a function of the 
    (a) voltage amplitude (Independent Variable - X Axis)
    (b) dwell time for symmetric bipolar waveform (Independent Variable - Y Axis)
    (c) Have a separate plot for each ink
    (d) Note values where a satellite droplet OR tail formed

```
prefix : <https://tw.rpi.edu/web/project/ampo-ink#> 
prefix owl: <http://www.w3.org/2002/07/owl#> 
prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
prefix sio: <http://semanticscience.org/resource/> 
prefix xml: <http://www.w3.org/XML/1998/namespace> 
prefix xsd: <http://www.w3.org/2001/XMLSchema#> 
prefix ampo: <https://tw.rpi.edu/web/project/ampo#> 
prefix ampo-ink: <https://tw.rpi.edu/web/project/ampo-ink#> 
prefix foaf: <http://xmlns.com/foaf/0.1/> 
prefix prov: <http://www.w3.org/ns/prov#> 
prefix qudt: <http://data.nasa.gov/qudt/owl/qudt#> 
prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
prefix dcterms: <http://purl.org/dc/terms/> 
prefix qudt-unit: <http://qudt.org/1.1/vocab/unit#> 

SELECT ?Trigger_Waveform ?Rise_Time ?Dwell_Time ?Fall_Time ?Echo_Time ?Final_Rise_Time 
?Max_Voltage_Amplitude ?Min_Voltage_Amplitude ?Period ?Idle_Voltage ?Amplitude ?Waveform_Type
?nozzle ?Nozzle_Temp 
?Droplet_Ejected ?Droplet_Visible ?Droplet_Tail ?Droplet_Satellites
?Droplet_T1 ?Droplet_T2 ?Droplet_Diameter ?Droplet_Velocity ?Droplet_Distance_Traveled ?Ink
WHERE { 
?step rdf:type :MaterialDeposition .
?step ampo:qualifiedEquipmentUsage ?nozzle_usage .
?nozzle_usage ampo:requiresInput ?subject .
?subject rdf:type :Actuator_DropletActuation .
?subject rdfs:label ?subject_label .
BIND( STR(?subject_label) AS ?Trigger_Waveform ) .
OPTIONAL {
    ?subject ampo:hasAttribute ?rise_time .
	?rise_time rdf:type :DropletActuation_RiseTime .
	?rise_time qudt:quantityValue ?rise_time_QV .
	?rise_time_QV qudt:numericValue ?rise_time_value .
	BIND(STR(?rise_time_value) AS ?Rise_Time) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?dwell_time .
	?dwell_time rdf:type :DropletActuation_DwellTime .
	?dwell_time qudt:quantityValue ?dwell_time_QV .
	?dwell_time_QV qudt:numericValue ?dwell_time_value .
	BIND(STR(?dwell_time_value) AS ?Dwell_Time) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?fall_time .
	?fall_time rdf:type :DropletActuation_FallTime .
	?fall_time qudt:quantityValue ?fall_time_QV .
	?fall_time_QV qudt:numericValue ?fall_time_value .
	BIND(STR(?fall_time_value) AS ?Fall_Time) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?echo_time .
	?echo_time rdf:type :DropletActuation_EchoTime .
	?echo_time qudt:quantityValue ?echo_time_QV .
	?echo_time_QV qudt:numericValue ?echo_time_value .
	BIND(STR(?echo_time_value) AS ?Echo_Time) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?final_rise_time .
	?final_rise_time rdf:type :DropletActuation_FinalRiseTime .
	?final_rise_time qudt:quantityValue ?final_rise_time_QV .
	?final_rise_time_QV qudt:numericValue ?final_rise_time_value .
	BIND(STR(?final_rise_time_value) AS ?Final_Rise_Time) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?max_voltage_amplitude .
	?max_voltage_amplitude rdf:type :DropletActuation_MaxVoltageAmplitude .
	?max_voltage_amplitude qudt:quantityValue ?max_voltage_amplitude_QV .
	?max_voltage_amplitude_QV qudt:numericValue ?max_voltage_amplitude_value .
	BIND(STR(?max_voltage_amplitude_value) AS ?Max_Voltage_Amplitude) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?min_voltage_amplitude .
	?min_voltage_amplitude rdf:type :DropletActuation_MinVoltageAmplitude .
	?min_voltage_amplitude qudt:quantityValue ?min_voltage_amplitude_QV .
	?min_voltage_amplitude_QV qudt:numericValue ?min_voltage_amplitude_value .
	BIND(STR(?min_voltage_amplitude_value) AS ?Min_Voltage_Amplitude) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?period .
	?period rdf:type :DropletActuation_Period .
	?period qudt:quantityValue ?period_QV .
	?period_QV qudt:numericValue ?period_value .
	BIND(STR(?period_value) AS ?Period) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?amplitude .
	?amplitude rdf:type :DropletActuation_Amplitude .
	?amplitude qudt:quantityValue ?amplitude_QV .
	?amplitude_QV qudt:numericValue ?amplitude_value .
	BIND(STR(?amplitude_value) AS ?Amplitude) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?idle_voltage .
	?idle_voltage rdf:type :DropletActuation_IdleVoltage .
	?idle_voltage qudt:quantityValue ?idle_voltage_QV .
	?idle_voltage_QV qudt:numericValue ?idle_voltage_value .
	BIND(STR(?idle_voltage_value) AS ?Idle_Voltage) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?line_type .
	?line_type rdf:type :DropletActuation_LineType .
	?line_type ampo:descriptiveValue ?line_type_value .
	BIND(STR(?line_type_value) AS ?Line_Type) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?waveform_type .
	?waveform_type rdf:type :DropletActuation_WaveformType .
	?waveform_type ampo:descriptiveValue ?waveform_type_value .
	BIND(STR(?waveform_type_value) AS ?Waveform_Type) .
}
?nozzle_usage ampo:equipment ?nozzle .
?nozzle_usage ampo:requiresInput ?nozzle_temp_input .
?nozzle_temp_input a :ActuatorNozzle_HeaterBlockTemperature .
?nozzle_temp_input qudt:quantityValue ?nozzle_temp_QV .
?nozzle_temp_QV qudt:numericValue ?nozzle_temp .
BIND ( STR(?nozzle_temp) AS ?Nozzle_Temp ) .
?step ampo:produces ?droplet .
?droplet a :Droplet .
OPTIONAL {?droplet rdfs:label ?droplet_label . }
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_ejected_attr . 
	?droplet_ejected_attr a :Droplet_Ejected .
	?droplet_ejected_attr rdf:value ?droplet_ejected .
	BIND ( STR(?droplet_ejected) AS ?Droplet_Ejected) .
}
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_visible_attr . 
	?droplet_visible_attr a :Droplet_Visible .
	?droplet_visible_attr rdf:value ?droplet_visible . 
	BIND ( STR(?droplet_visible) AS ?Droplet_Visible) .
}
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_tail_attr . 
	?droplet_tail_attr a :Droplet_Tail .
	?droplet_tail_attr rdf:value ?droplet_tail . 
	BIND ( STR(?droplet_tail) AS ?Droplet_Tail) .
}
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_satellites_attr . 
	?droplet_satellites_attr a :Droplet_Satellites .
	?droplet_satellites_attr rdf:value ?droplet_satellites . 
	BIND ( STR(?droplet_satellites) AS ?Droplet_Satellites) .
}
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_t1_attr . 
	?droplet_t1_attr a :Droplet_TimeFrame_1 .
	?droplet_t1_attr qudt:quantityValue ?droplet_t1_QV . 
	?droplet_t1_QV qudt:numericValue ?droplet_t1 .
	BIND ( STR(?droplet_t1) AS ?Droplet_T1) .

}
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_t2_attr . 
	?droplet_t2_attr a :Droplet_TimeFrame_2 .
	?droplet_t2_attr qudt:quantityValue ?droplet_t2_QV . 
	?droplet_t2_QV qudt:numericValue ?droplet_t2 .
	BIND ( STR(?droplet_t2) AS ?Droplet_T2) .
}
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_diameter_attr . 
	?droplet_diameter_attr a :Droplet_Diameter .
	?droplet_diameter_attr qudt:quantityValue ?droplet_diameter_QV . 
	?droplet_diameter_QV qudt:numericValue ?droplet_diameter .
	BIND ( STR(?droplet_diameter) AS ?Droplet_Diameter) .
}
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_velocity_attr . 
	?droplet_velocity_attr a :Droplet_Velocity .
	?droplet_velocity_attr qudt:quantityValue ?droplet_velocity_QV . 
	?droplet_velocity_QV qudt:numericValue ?droplet_velocity .
	BIND ( STR(?droplet_velocity) AS ?Droplet_Velocity) .
}
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_distance_traveled_attr . 
	?droplet_distance_traveled_attr a :Droplet_DistanceTraveled .
	?droplet_distance_traveled_attr qudt:quantityValue ?droplet_distance_traveled_QV . 
	?droplet_distance_traveled_QV qudt:numericValue ?droplet_distance_traveled .
	BIND ( STR(?droplet_distance_traveled) AS ?Droplet_Distance_Traveled) .
}
?step ampo:hasParticipant ?ink .
?ink a ampo-ink:Ink .
?ink rdfs:label ?ink_label .
BIND ( STR(?ink_label) AS ?Ink) .
FILTER (STR(?waveform_type_value) = "Symmetric Bipolar Waveform") .
FILTER ( ?droplet_ejected ) .
}
ORDER BY ?ink_label
```


-------------------------------






### Return all inks (one attribute per row)
```
prefix : <https://tw.rpi.edu/web/project/ampo-ink#> 
prefix owl: <http://www.w3.org/2002/07/owl#> 
prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
prefix sio: <http://semanticscience.org/resource/> 
prefix xml: <http://www.w3.org/XML/1998/namespace> 
prefix xsd: <http://www.w3.org/2001/XMLSchema#> 
prefix ampo: <https://tw.rpi.edu/web/project/ampo#> 
prefix foaf: <http://xmlns.com/foaf/0.1/> 
prefix prov: <http://www.w3.org/ns/prov#> 
prefix qudt: <http://data.nasa.gov/qudt/owl/qudt#> 
prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
prefix dcterms: <http://purl.org/dc/terms/> 
prefix qudt-unit: <http://qudt.org/1.1/vocab/unit#> 

SELECT ?subject ?subject_label ?attr ?attr_label ?attr_descriptiveValue ?attr_numericValue ?attr_unit ?attr_Quantity_Value
	WHERE { 
?subject rdf:type :Ink .
?subject rdfs:label ?subject_label .
?subject ampo:hasAttribute ?attr .
OPTIONAL {
	?attr rdf:type :Ink_Density .
	?attr rdfs:label ?attr_label .
	OPTIONAL {
		?attr ampo:descriptiveValue ?attr_descriptiveValue . 
	}
	OPTIONAL {
		?attr qudt:quantityValue ?attr_Quantity_Value .
		?attr_Quantity_Value qudt:numericValue ?attr_numericValue .
		?attr_Quantity_Value qudt:unit ?attr_unit .
	}
}
OPTIONAL {
	?attr rdf:type :Ink_DynamicViscosity .
	?attr rdfs:label ?attr_label .
	OPTIONAL {
		?attr ampo:descriptiveValue ?attr_descriptiveValue . 
	}
	OPTIONAL {
		?attr qudt:quantityValue ?attr_Quantity_Value .
		?attr_Quantity_Value qudt:numericValue ?attr_numericValue .
		?attr_Quantity_Value qudt:unit ?attr_unit .
	}
}
OPTIONAL {
	?attr rdf:type :Ink_SurfaceTension .
	?attr rdfs:label ?attr_label .
	OPTIONAL {
		?attr ampo:descriptiveValue ?attr_descriptiveValue . 
	}
	OPTIONAL {
		?attr qudt:quantityValue ?attr_Quantity_Value .
		?attr_Quantity_Value qudt:numericValue ?attr_numericValue .
		?attr_Quantity_Value qudt:unit ?attr_unit .
	}
}
OPTIONAL {
	?attr rdf:type :Ink_Color .
	?attr rdfs:label ?attr_label .
	OPTIONAL {
		?attr ampo:descriptiveValue ?attr_descriptiveValue . 
	}
	OPTIONAL {
		?attr qudt:quantityValue ?attr_Quantity_Value .
		?attr_Quantity_Value qudt:numericValue ?attr_numericValue .
		?attr_Quantity_Value qudt:unit ?attr_unit .
	}
}
#FILTER ( STR(?subject_label)="DI Water" )
}
```


### Return all inks (all attribute in the same row)
```
prefix : <https://tw.rpi.edu/web/project/ampo-ink#> 
prefix owl: <http://www.w3.org/2002/07/owl#> 
prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
prefix sio: <http://semanticscience.org/resource/> 
prefix xml: <http://www.w3.org/XML/1998/namespace> 
prefix xsd: <http://www.w3.org/2001/XMLSchema#> 
prefix ampo: <https://tw.rpi.edu/web/project/ampo#> 
prefix foaf: <http://xmlns.com/foaf/0.1/> 
prefix prov: <http://www.w3.org/ns/prov#> 
prefix qudt: <http://data.nasa.gov/qudt/owl/qudt#> 
prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
prefix dcterms: <http://purl.org/dc/terms/> 
prefix qudt-unit: <http://qudt.org/1.1/vocab/unit#> 

SELECT ?subject ?subject_label ?density_value ?density_unit ?dynamic_viscosity_value ?dynamic_viscosity_unit 
        ?surface_tension_value ?surface_tension_unit ?color_value
WHERE { 
?subject rdf:type :Ink .
?subject rdfs:label ?subject_label .
OPTIONAL {
    ?subject ampo:hasAttribute ?density .
	?density rdf:type :Ink_Density .
	?density rdfs:label ?density_label .
	OPTIONAL {
		?density qudt:quantityValue ?density_Quantity_Value .
		?density_Quantity_Value qudt:numericValue ?density_value .
		?density_Quantity_Value qudt:unit ?density_unit .
	}
}
OPTIONAL {
	?subject ampo:hasAttribute ?dynamic_viscosity .
	?dynamic_viscosity rdf:type :Ink_DynamicViscosity .
	?dynamic_viscosity rdfs:label ?dynamic_viscosity_label .
	OPTIONAL {
		?dynamic_viscosity qudt:quantityValue ?dynamic_viscosity_Quantity_Value .
		?dynamic_viscosity_Quantity_Value qudt:numericValue ?dynamic_viscosity_value .
		?dynamic_viscosity_Quantity_Value qudt:unit ?dynamic_viscosity_unit .
	}
}
OPTIONAL {
	?subject ampo:hasAttribute ?surface_tension .
	?surface_tension rdf:type :Ink_SurfaceTension .
	?surface_tension rdfs:label ?surface_tension_label .
	OPTIONAL {
		?surface_tension qudt:quantityValue ?surface_tension_Quantity_Value .
		?surface_tension_Quantity_Value qudt:numericValue ?surface_tension_value .
		?surface_tension_Quantity_Value qudt:unit ?surface_tension_unit .
	}
}
OPTIONAL {
	?subject ampo:hasAttribute ?color .
	?color rdf:type :Ink_Color .
	?color rdfs:label ?attr_label .
	OPTIONAL {
		?color ampo:descriptiveValue ?color_value . 
	}
}
#FILTER ( STR(?subject_label)="DI Water" )
}
```


### Return all trigger waveforms
```
prefix : <https://tw.rpi.edu/web/project/ampo-ink#> 
prefix owl: <http://www.w3.org/2002/07/owl#> 
prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
prefix sio: <http://semanticscience.org/resource/> 
prefix xml: <http://www.w3.org/XML/1998/namespace> 
prefix xsd: <http://www.w3.org/2001/XMLSchema#> 
prefix ampo: <https://tw.rpi.edu/web/project/ampo#> 
prefix ampo-ink: <https://tw.rpi.edu/web/project/ampo-ink#> 
prefix foaf: <http://xmlns.com/foaf/0.1/> 
prefix prov: <http://www.w3.org/ns/prov#> 
prefix qudt: <http://data.nasa.gov/qudt/owl/qudt#> 
prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
prefix dcterms: <http://purl.org/dc/terms/> 
prefix qudt-unit: <http://qudt.org/1.1/vocab/unit#> 

SELECT ?subject ?subject_label ?rise_time_value ?dwell_time_value ?fall_time_value ?echo_time_value ?final_rise_time_value 
        ?max_voltage_amplitude_value ?min_voltage_amplitude_value ?period_value ?idle_voltage_value ?amplitude_value ?line_type_value ?waveform_type_value
WHERE { 
?subject rdf:type :Actuator_DropletActuation .
?subject rdfs:label ?subject_label .
OPTIONAL {
    ?subject ampo:hasAttribute ?rise_time .
	?rise_time rdf:type :DropletActuation_RiseTime .
	?rise_time qudt:quantityValue ?rise_time_QV .
	?rise_time_QV qudt:numericValue ?rise_time_value .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?dwell_time .
	?dwell_time rdf:type :DropletActuation_DwellTime .
	?dwell_time qudt:quantityValue ?dwell_time_QV .
	?dwell_time_QV qudt:numericValue ?dwell_time_value .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?fall_time .
	?fall_time rdf:type :DropletActuation_FallTime .
	?fall_time qudt:quantityValue ?fall_time_QV .
	?fall_time_QV qudt:numericValue ?fall_time_value .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?echo_time .
	?echo_time rdf:type :DropletActuation_EchoTime .
	?echo_time qudt:quantityValue ?echo_time_QV .
	?echo_time_QV qudt:numericValue ?echo_time_value .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?final_rise_time .
	?final_rise_time rdf:type :DropletActuation_FinalRiseTime .
	?final_rise_time qudt:quantityValue ?final_rise_time_QV .
	?final_rise_time_QV qudt:numericValue ?final_rise_time_value .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?max_voltage_amplitude .
	?max_voltage_amplitude rdf:type :DropletActuation_MaxVoltageAmplitude .
	?max_voltage_amplitude qudt:quantityValue ?max_voltage_amplitude_QV .
	?max_voltage_amplitude_QV qudt:numericValue ?max_voltage_amplitude_value .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?min_voltage_amplitude .
	?min_voltage_amplitude rdf:type :DropletActuation_MinVoltageAmplitude .
	?min_voltage_amplitude qudt:quantityValue ?min_voltage_amplitude_QV .
	?min_voltage_amplitude_QV qudt:numericValue ?min_voltage_amplitude_value .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?period .
	?period rdf:type :DropletActuation_Period .
	?period qudt:quantityValue ?period_QV .
	?period_QV qudt:numericValue ?period_value .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?amplitude .
	?amplitude rdf:type :DropletActuation_Amplitude .
	?amplitude qudt:quantityValue ?amplitude_QV .
	?amplitude_QV qudt:numericValue ?amplitude_value .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?idle_voltage .
	?idle_voltage rdf:type :DropletActuation_IdleVoltage .
	?idle_voltage qudt:quantityValue ?idle_voltage_QV .
	?idle_voltage_QV qudt:numericValue ?idle_voltage_value .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?line_type .
	?line_type rdf:type :DropletActuation_LineType .
	?line_type ampo:descriptiveValue ?line_type_value .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?waveform_type .
	?waveform_type rdf:type :DropletActuation_WaveformType .
	?waveform_type ampo:descriptiveValue ?waveform_type_value .
}
#FILTER ( STR(?line_type)="Bipolar Lines" )
}
ORDER BY ?subject_label
```



### Return trigger waveforms that fits certain conditions of the droplet produced
```
prefix : <https://tw.rpi.edu/web/project/ampo-ink#> 
prefix owl: <http://www.w3.org/2002/07/owl#> 
prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
prefix sio: <http://semanticscience.org/resource/> 
prefix xml: <http://www.w3.org/XML/1998/namespace> 
prefix xsd: <http://www.w3.org/2001/XMLSchema#> 
prefix ampo: <https://tw.rpi.edu/web/project/ampo#> 
prefix ampo-ink: <https://tw.rpi.edu/web/project/ampo-ink#> 
prefix foaf: <http://xmlns.com/foaf/0.1/> 
prefix prov: <http://www.w3.org/ns/prov#> 
prefix qudt: <http://data.nasa.gov/qudt/owl/qudt#> 
prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
prefix dcterms: <http://purl.org/dc/terms/> 
prefix qudt-unit: <http://qudt.org/1.1/vocab/unit#> 


SELECT ?Trigger_Waveform ?Rise_Time ?Dwell_Time ?Fall_Time ?Echo_Time ?Final_Rise_Time 
?Max_Voltage_Amplitude ?Min_Voltage_Amplitude ?Period ?Idle_Voltage ?Amplitude 
?Line_Type ?Waveform_Type
?step ?nozzle_usage ?nozzle ?droplet ?Nozzle_Temp 
?Droplet_Ejected ?Droplet_Visible ?Droplet_Tail ?Droplet_Satellites
?Droplet_T1 ?Droplet_T2 ?Droplet_Diameter ?Droplet_Velocity ?Droplet_Distance_Traveled ?Ink
WHERE { 
?step rdf:type :MaterialDeposition .
?step ampo:qualifiedEquipmentUsage ?nozzle_usage .
?nozzle_usage ampo:requiresInput ?subject .
?subject rdf:type :Actuator_DropletActuation .
?subject rdfs:label ?subject_label .
BIND( STR(?subject_label) AS ?Trigger_Waveform ) .
OPTIONAL {
    ?subject ampo:hasAttribute ?rise_time .
	?rise_time rdf:type :DropletActuation_RiseTime .
	?rise_time qudt:quantityValue ?rise_time_QV .
	?rise_time_QV qudt:numericValue ?rise_time_value .
	BIND(STR(?rise_time_value) AS ?Rise_Time) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?dwell_time .
	?dwell_time rdf:type :DropletActuation_DwellTime .
	?dwell_time qudt:quantityValue ?dwell_time_QV .
	?dwell_time_QV qudt:numericValue ?dwell_time_value .
	BIND(STR(?dwell_time_value) AS ?Dwell_Time) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?fall_time .
	?fall_time rdf:type :DropletActuation_FallTime .
	?fall_time qudt:quantityValue ?fall_time_QV .
	?fall_time_QV qudt:numericValue ?fall_time_value .
	BIND(STR(?fall_time_value) AS ?Fall_Time) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?echo_time .
	?echo_time rdf:type :DropletActuation_EchoTime .
	?echo_time qudt:quantityValue ?echo_time_QV .
	?echo_time_QV qudt:numericValue ?echo_time_value .
	BIND(STR(?echo_time_value) AS ?Echo_Time) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?final_rise_time .
	?final_rise_time rdf:type :DropletActuation_FinalRiseTime .
	?final_rise_time qudt:quantityValue ?final_rise_time_QV .
	?final_rise_time_QV qudt:numericValue ?final_rise_time_value .
	BIND(STR(?final_rise_time_value) AS ?Final_Rise_Time) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?max_voltage_amplitude .
	?max_voltage_amplitude rdf:type :DropletActuation_MaxVoltageAmplitude .
	?max_voltage_amplitude qudt:quantityValue ?max_voltage_amplitude_QV .
	?max_voltage_amplitude_QV qudt:numericValue ?max_voltage_amplitude_value .
	BIND(STR(?max_voltage_amplitude_value) AS ?Max_Voltage_Amplitude) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?min_voltage_amplitude .
	?min_voltage_amplitude rdf:type :DropletActuation_MinVoltageAmplitude .
	?min_voltage_amplitude qudt:quantityValue ?min_voltage_amplitude_QV .
	?min_voltage_amplitude_QV qudt:numericValue ?min_voltage_amplitude_value .
	BIND(STR(?min_voltage_amplitude_value) AS ?Min_Voltage_Amplitude) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?period .
	?period rdf:type :DropletActuation_Period .
	?period qudt:quantityValue ?period_QV .
	?period_QV qudt:numericValue ?period_value .
	BIND(STR(?period_value) AS ?Period) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?amplitude .
	?amplitude rdf:type :DropletActuation_Amplitude .
	?amplitude qudt:quantityValue ?amplitude_QV .
	?amplitude_QV qudt:numericValue ?amplitude_value .
	BIND(STR(?amplitude_value) AS ?Amplitude) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?idle_voltage .
	?idle_voltage rdf:type :DropletActuation_IdleVoltage .
	?idle_voltage qudt:quantityValue ?idle_voltage_QV .
	?idle_voltage_QV qudt:numericValue ?idle_voltage_value .
	BIND(STR(?idle_voltage_value) AS ?Idle_Voltage) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?line_type .
	?line_type rdf:type :DropletActuation_LineType .
	?line_type ampo:descriptiveValue ?line_type_value .
	BIND(STR(?line_type_value) AS ?Line_Type) .
}
OPTIONAL {
    ?subject ampo:hasAttribute ?waveform_type .
	?waveform_type rdf:type :DropletActuation_WaveformType .
	?waveform_type ampo:descriptiveValue ?waveform_type_value .
	BIND(STR(?waveform_type_value) AS ?Waveform_Type) .
}
?nozzle_usage ampo:equipment ?nozzle .
?nozzle_usage ampo:requiresInput ?nozzle_temp_input .
?nozzle_temp_input a :ActuatorNozzle_HeaterBlockTemperature .
?nozzle_temp_input qudt:quantityValue ?nozzle_temp_QV .
?nozzle_temp_QV qudt:numericValue ?nozzle_temp .
BIND (STR(?nozzle_temp) AS ?Nozzle_Temp) .
?step ampo:produces ?droplet .
?droplet a :Droplet .
OPTIONAL {?droplet rdfs:label ?droplet_label . }
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_ejected_attr . 
	?droplet_ejected_attr a :Droplet_Ejected .
	?droplet_ejected_attr rdf:value ?droplet_ejected .
	BIND ( STR(?droplet_ejected) AS ?Droplet_Ejected) .
}
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_visible_attr . 
	?droplet_visible_attr a :Droplet_Visible .
	?droplet_visible_attr rdf:value ?droplet_visible . 
	BIND ( STR(?droplet_visible) AS ?Droplet_Visible) .
}
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_tail_attr . 
	?droplet_tail_attr a :Droplet_Tail .
	?droplet_tail_attr rdf:value ?droplet_tail . 
	BIND ( STR(?droplet_tail) AS ?Droplet_Tail) .
}
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_satellites_attr . 
	?droplet_satellites_attr a :Droplet_Satellites .
	?droplet_satellites_attr rdf:value ?droplet_satellites . 
	BIND ( STR(?droplet_satellites) AS ?Droplet_Satellites) .
}
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_t1_attr . 
	?droplet_t1_attr a :Droplet_TimeFrame_1 .
	?droplet_t1_attr qudt:quantityValue ?droplet_t1_QV . 
	?droplet_t1_QV qudt:numericValue ?droplet_t1 .
	BIND ( STR(?droplet_t1) AS ?Droplet_T1) .

}
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_t2_attr . 
	?droplet_t2_attr a :Droplet_TimeFrame_2 .
	?droplet_t2_attr qudt:quantityValue ?droplet_t2_QV . 
	?droplet_t2_QV qudt:numericValue ?droplet_t2 .
	BIND ( STR(?droplet_t2) AS ?Droplet_T2) .
}
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_diameter_attr . 
	?droplet_diameter_attr a :Droplet_Diameter .
	?droplet_diameter_attr qudt:quantityValue ?droplet_diameter_QV . 
	?droplet_diameter_QV qudt:numericValue ?droplet_diameter .
	BIND ( STR(?droplet_diameter) AS ?Droplet_Diameter) .
}
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_velocity_attr . 
	?droplet_velocity_attr a :Droplet_Velocity .
	?droplet_velocity_attr qudt:quantityValue ?droplet_velocity_QV . 
	?droplet_velocity_QV qudt:numericValue ?droplet_velocity .
	BIND ( STR(?droplet_velocity) AS ?Droplet_Velocity) .
}
OPTIONAL {
	?droplet ampo:hasAttribute ?droplet_distance_traveled_attr . 
	?droplet_distance_traveled_attr a :Droplet_DistanceTraveled .
	?droplet_distance_traveled_attr qudt:quantityValue ?droplet_distance_traveled_QV . 
	?droplet_distance_traveled_QV qudt:numericValue ?droplet_distance_traveled .
	BIND ( STR(?droplet_distance_traveled) AS ?Droplet_Distance_Traveled) .
}
?step ampo:hasParticipant ?ink .
?ink a ampo-ink:Ink .
?ink rdfs:label ?ink_label .
BIND ( STR(?ink_label) AS ?Ink) .
}
ORDER BY ?ink_label
```


### SPARQL Query Prefixes
```
prefix : <https://tw.rpi.edu/web/project/ampo-ink#> 
prefix owl: <http://www.w3.org/2002/07/owl#> 
prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
prefix sio: <http://semanticscience.org/resource/> 
prefix xml: <http://www.w3.org/XML/1998/namespace> 
prefix xsd: <http://www.w3.org/2001/XMLSchema#> 
prefix ampo: <https://tw.rpi.edu/web/project/ampo#> 
prefix foaf: <http://xmlns.com/foaf/0.1/> 
prefix prov: <http://www.w3.org/ns/prov#> 
prefix qudt: <http://data.nasa.gov/qudt/owl/qudt#> 
prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
prefix dcterms: <http://purl.org/dc/terms/> 
prefix qudt-unit: <http://qudt.org/1.1/vocab/unit#> 
```