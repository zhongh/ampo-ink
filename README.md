# ampo-ink


### Ontology IRI

`https://tw.rpi.edu/web/project/ampo-ink`


### Ontology Prefixes

```
@prefix : <https://tw.rpi.edu/web/project/ampo-ink#> .
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
```


### Ontology Import

This use case uses the updated ampo ontology `ampo-1.0.5.ttl` which is published at and imported from <http://homepages.rpi.edu/~zhongh3/ontologies/ampo-1.0.5.ttl>

### Updates (To be added)

### Last updates

- Added types and attributes for waveforms i.e. `ampo:Actuator_DropletActuation`
- Add according attributes for `ampo:Droplet`
- Explored and found using Python `string.Template` library to create and write triples neatly from predefined templates
- Verifed the example instances by running the queries
- Certain triples were to be added in addition to the individual definitions. For example, a `Actuator_DropletActuation` is input of some nozzle and is required input by some `ampo:EquipmentUsage`
- Found that we were unable to import individuals from external files and query correctly. Currently we concatenate files manually and it works fine.
- Qualified usages be defined as anonymous individuals while droplets (`ampo:Product`) be defined explicitly as named individuals. 


