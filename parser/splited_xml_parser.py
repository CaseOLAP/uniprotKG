class SplitedEntryParser(object):
       # Class to parse a single entry in the Uniprot XML file. 
       # The entry is passed as an ElementTree object.
       # The class has methods to extract the accession number, protein name, gene name, organism name, ptm and sequence.
       # Author: Namuna Panday; UCLA 2023

       def __init__(self, entry):
           self.entry = entry
           #self.ns = {'uniprot': 'http://uniprot.org/uniprot'}
           self.ns = {'ns0': 'http://uniprot.org/uniprot'}
           self.name = None
           self.accessions = None
           self.uniprotId = None
           self.gene = None
           self.organism = None
           self.sequence = None
           self.references= None
           self.ptm = []


       def get_accession(self):
              # Get the accession number
              try:
                     self.accessions =  [accession.text for accession in self.entry.findall('ns0:accession', self.ns)]
              except AttributeError:
                     self.accessions =  None
              return self.accessions

       def get_name(self):

              # Get the protein name
              try:
                     #self.name =  self.entry.find('{http://uniprot.org/uniprot}name').text
                     self.name =  self.entry.find('ns0:protein/ns0:recommendedName/ns0:fullName', self.ns).text
              except:
                     self.name =  None
              return self.name


       def get_gene(self):
              try:
                     #self.gene = self.entry.find('{http://uniprot.org/uniprot}gene/name[@type="primary"]').text
                     self.gene = self.entry.find('ns0:gene/ns0:name[@type="primary"]', self.ns).text
              except:
                     self.gene = None
              return self.gene

       def get_organism(self):
              try:
                     #self.organism = self.entry.find('{http://uniprot.org/uniprot}organism/name[@type="scientific"]').text
                     self.organism = self.entry.find('ns0:organism/ns0:name[@type="scientific"]', self.ns).text
              except:
                     self.organism = None
              return self.organism

       def get_sequence(self):
              try:
                     self.sequence = self.entry.find('ns0:sequence', self.ns).text
              except:
                     self.sequence = None
              return self.sequence

       def get_uniprotId(self):
              try:
                     self.uniprotId = self.entry.find('ns0:accession', self.ns).text
              except:
                     self.uniprotId = None
              return self.uniprotId


       def get_references(self):
              self.references = []
              for ref in self.entry.findall('ns0:reference', self.ns):
                        reference = {}
                        key = ref.get('key')
                        reference['key'] = key
                        citation_type = ref.find('ns0:citation', self.ns).get('type')
                        reference["citation_type"] = citation_type

                        #print(i, key, citation_type, ref)
                        if citation_type == 'journal article':
                                try:
                                        reference['journal'] = ref.find('ns0:citation', self.ns).get('name')
                                except:
                                        reference['journal'] = None
                                try:
                                        reference['date'] = ref.find('ns0:citation', self.ns).get('date')
                                except:
                                        reference['date'] = None
                                try:
                                        reference['title'] = ref.find('ns0:citation/uniprot:title', self.ns).text
                                except:
                                        reference['title'] = None
                                try:
                                        reference['authors'] = [author.get('name') for author in ref.findall('ns0:citation/ns0:authorList/ns0:person', self.ns)]
                                except:
                                        reference['authors'] = None
                                try:
                                        reference['pubmedId'] = ref.find('ns0:citation/ns0:dbReference[@type="PubMed"]', self.ns).get('id')
                                except:
                                        reference['pubmedId'] = None
                                try:
                                        reference['doi'] = ref.find('ns0:citation/ns0:dbReference[@type="DOI"]', self.ns).get('id')
                                except:
                                        reference['doi'] = None
                        if citation_type == 'submission':
                                try:
                                        reference['db'] = ref.find('ns0:citation', self.ns).get('db')
                                except:
                                        reference['db'] = None
                                try:
                                        reference['date'] = ref.find('ns0:citation', self.ns).get('name')
                                except:
                                        reference['date'] = None
                                try:
                                        reference['scope'] = [scope.text for scope in ref.findall('ns0:scope', self.ns)]
                                except:
                                        reference['scope'] = None
                                try:
                                        reference['source'] = [source.text for source in ref.findall('ns0:source', self.ns)]
                                except:
                                        reference['source'] = None
                        if citation_type == 'patent':
                                   try:
                                          reference['number'] = ref.find('ns0:citation', self.ns).get('number')
                                   except:
                                          reference['number'] = None
                                   try:
                                          reference['country'] = ref.find('ns0:citation', self.ns).get('country')
                                   except:
                                          reference['country'] = None
                                   try:
                                          reference['title'] = ref.find('ns0:citation/uniprot:title', self.ns).text
                                   except:
                                          reference['title'] = None
                        if citation_type == 'thesis':
                                   try:
                                          reference['institution'] = ref.find('ns0:citation', self.ns).get('institution')
                                   except:
                                          reference['institution'] = None
                                   try:
                                          reference['date'] = ref.find('ns0:citation', self.ns).get('date')
                                   except:
                                          reference['date'] = None
                                   try:
                                          reference['title'] = ref.find('ns0:citation/uniprot:title', self.ns).text
                                   except:
                                          reference['title'] = None
                                   try:
                                          reference['authors'] = [author.get('name') for author in ref.findall('ns0:citation/ns0:authorList/ns0:person', self.ns)]
                                   except:
                                          reference['authors'] = None
                        if citation_type == 'unpublished observations':
                                   try:
                                          reference['date'] = ref.find('ns0:citation', self.ns).get('date')
                                   except:
                                          reference['date'] = None
                                   try:
                                          reference['title'] = ref.find('ns0:citation/ns0:title', self.ns).text
                                   except:
                                          reference['title'] = None
                                   try:
                                          reference['authors'] = [author.get('name') for author in ref.findall('ns0:citation/ns0:authorList/ns0:person', self.ns)]
                                   except:
                                          reference['authors'] = None
                        if citation_type == 'online journal article':
                                   try:
                                          reference['journal'] = ref.find('ns0:citation', self.ns).get('name')
                                   except:
                                          reference['journal'] = None
                                   try:
                                          reference['date'] = ref.find('ns0:citation', self.ns).get('date')
                                   except:
                                          reference['date'] = None
                                   try:
                                          reference['title'] = ref.find('ns0:citation/ns0:title', self.ns).text
                                   except:
                                          reference['title'] = None
                                   try:
                                          reference['authors'] = [author.get('name') for author in ref.findall('ns0:citation/ns0:authorList/ns0:person', self.ns)]
                                   except:
                                          reference['authors'] = None
                                   try:
                                          reference['pubmedId'] = ref.find('ns0:citation/ns0:dbReference[@type="PubMed"]', self.ns).get('id')
                                   except:
                                          reference['pubmedId'] = None
                                   try:
                                          reference['doi'] = ref.find('ns0:citation/ns0:dbReference[@type="DOI"]', self.ns).get('id')
                                   except:
                                          reference['doi'] = None

                        if citation_type == 'book':
                                   try:
                                          reference['title'] = ref.find('ns0:citation/ns0:title', self.ns).text
                                   except:
                                          reference['title'] = None
                                   try:
                                          reference['authors'] = [author.get('name') for author in ref.findall('ns0:citation/ns0:authorList/ns0:person', self.ns)]
                                   except:
                                          reference['authors'] = None
                                   try:
                                          reference['publisher'] = ref.find('ns0:citation/ns0:dbReference[@type="Publisher"]', self.ns).get('id')
                                   except:
                                          reference['publisher'] = None
                                   try:
                                          reference['isbn'] = ref.find('ns0:citation/ns0:dbReference[@type="ISBN"]', self.ns).get('id')
                                   except:
                                          reference['isbn'] = None

                        self.references.append(reference)


              return self.references





       def get_ptm(self):
              try:
                     #self.ptm = self.entry.find('uniprot:feature[@type="modified residue"]', self.ns).text
                     for feature in self.entry.findall('ns0:feature[@type="modified residue"]', self.ns):
                            # Get the position and description of the modification
                            position = feature.find('ns0:location/ns0:position', self.ns).get('position')
                            description = feature.get('description')
                            evidence = feature.get('evidence')
                            self.ptm.append({'Position': position, 'Description': description, 'Evidence': evidence})
              except:
                     self.ptm = None
              return self.ptm