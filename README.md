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


### Ontology Headings

```
<https://tw.rpi.edu/web/project/ampo-ink> rdf:type owl:Ontology ;
                                          
                                          owl:imports <http://homepages.rpi.edu/~zhongh3/ontologies/ampo-1.0.5.ttl> .
```


### Updates

- added types and attributes for waveforms
- (DONE) very ontology ampo-ink vs ampo-ink-droplet, the classes part should be the same
- (DONE) add according attributes for droplets
- (DONE) find a good way to use python to create and write triples neatly (using `string.Template` library)
- (NOW) verify the example instances by running the queries
- (NOW) and get a start to output triples
- Reminder, certain triples are to be added seperately than in the individual definitijons. For example, a trigger waveform is input of some nozzle and is required input by some equipmentusage
- (!) Unable to import individuals from external files and query correctly. has to concatenate files.
- qualified usage be anonymous ok; let's explitely define droplets. should be good to go for sunday.

