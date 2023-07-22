class UniprotEntryParser(object):
       # Class to parse a single entry in the Uniprot XML file. 
       # The entry is passed as an ElementTree object.
       # The class has methods to extract the accession number, protein name, gene name, organism name, ptm and sequence.
       # Author: Namuna Panday; UCLA, 2023

       def __init__(self, entry):
           self.entry = entry
           self.ns = {'uniprot': 'http://uniprot.org/uniprot'}
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
                     self.accessions =  [accession.text for accession in self.entry.findall('{http://uniprot.org/uniprot}accession')],
              except:
                     self.accessions =  None
              return self.accessions

       def get_name(self):

              # Get the protein name
              try:    
                     #self.name =  self.entry.find('{http://uniprot.org/uniprot}name').text
                     self.name =  self.entry.find('uniprot:protein/uniprot:recommendedName/uniprot:fullName', self.ns).text
              except:
                     self.name =  None
              return self.name


       def get_gene(self):
              try:
                     #self.gene = self.entry.find('{http://uniprot.org/uniprot}gene/name[@type="primary"]').text
                     self.gene = self.entry.find('uniprot:gene/uniprot:name[@type="primary"]', self.ns).text
              except:
                     self.gene = None
              return self.gene

       def get_organism(self):
              try:
                     #self.organism = self.entry.find('{http://uniprot.org/uniprot}organism/name[@type="scientific"]').text
                     self.organism = self.entry.find('uniprot:organism/uniprot:name[@type="scientific"]', self.ns).text
              except: 
                     self.organism = None
              return self.organism
       
       def get_sequence(self):
              try:
                     self.sequence = self.entry.find('uniprot:sequence', self.ns).text
              except:
                     self.sequence = None
              return self.sequence
       
       def get_uniprotId(self):
              try:
                     self.uniprotId = self.entry.find('uniprot:accession', self.ns).text
              except:
                     self.uniprotId = None
              return self.uniprotId


       def get_references(self):
              self.references = []
              for ref in self.entry.findall('uniprot:reference', self.ns):
                        reference = {}
                        key = ref.get('key')
                        reference['key'] = key
                        citation_type = ref.find('uniprot:citation', self.ns).get('type')
                        reference["citation_type"] = citation_type

                        #print(i, key, citation_type, ref)
                        if citation_type == 'journal article':
                                try:
                                        reference['journal'] = ref.find('uniprot:citation', self.ns).get('name')
                                except:
                                        reference['journal'] = None
                                try:
                                        reference['date'] = ref.find('uniprot:citation', self.ns).get('date')
                                except:
                                        reference['date'] = None
                                try:
                                        reference['title'] = ref.find('uniprot:citation/uniprot:title', self.ns).text
                                except:
                                        reference['title'] = None
                                try:
                                        reference['authors'] = [author.get('name') for author in ref.findall('uniprot:citation/uniprot:authorList/uniprot:person', self.ns)]
                                except:
                                        reference['authors'] = None
                                try:
                                        reference['pubmedId'] = ref.find('uniprot:citation/uniprot:dbReference[@type="PubMed"]', self.ns).get('id')
                                except:
                                        reference['pubmedId'] = None
                                try:
                                        reference['doi'] = ref.find('uniprot:citation/uniprot:dbReference[@type="DOI"]', self.ns).get('id')
                                except:
                                        reference['doi'] = None
                        if citation_type == 'submission':  
                                try: 
                                        reference['db'] = ref.find('uniprot:citation', self.ns).get('db')
                                except:
                                        reference['db'] = None
                                try:
                                        reference['date'] = ref.find('uniprot:citation', self.ns).get('name')
                                except:
                                        reference['date'] = None
                                try:
                                        reference['scope'] = [scope.text for scope in ref.findall('uniprot:scope', self.ns)]
                                except:
                                        reference['scope'] = None
                                try:
                                        reference['source'] = [source.text for source in ref.findall('uniprot:source', self.ns)]
                                except:
                                        reference['source'] = None
                        if citation_type == 'patent':
                                   try:
                                          reference['number'] = ref.find('uniprot:citation', self.ns).get('number')
                                   except:
                                          reference['number'] = None
                                   try:
                                          reference['country'] = ref.find('uniprot:citation', self.ns).get('country')
                                   except:
                                          reference['country'] = None
                                   try:
                                          reference['title'] = ref.find('uniprot:citation/uniprot:title', self.ns).text
                                   except:
                                          reference['title'] = None
                        if citation_type == 'thesis':
                                   try:
                                          reference['institution'] = ref.find('uniprot:citation', self.ns).get('institution')
                                   except:
                                          reference['institution'] = None
                                   try:
                                          reference['date'] = ref.find('uniprot:citation', self.ns).get('date')
                                   except:
                                          reference['date'] = None
                                   try:
                                          reference['title'] = ref.find('uniprot:citation/uniprot:title', self.ns).text
                                   except:
                                          reference['title'] = None
                                   try:
                                          reference['authors'] = [author.get('name') for author in ref.findall('uniprot:citation/uniprot:authorList/uniprot:person', self.ns)]
                                   except:
                                          reference['authors'] = None
                        if citation_type == 'unpublished observations':
                                   try:
                                          reference['date'] = ref.find('uniprot:citation', self.ns).get('date')
                                   except:
                                          reference['date'] = None
                                   try:
                                          reference['title'] = ref.find('uniprot:citation/uniprot:title', self.ns).text
                                   except:
                                          reference['title'] = None
                                   try:
                                          reference['authors'] = [author.get('name') for author in ref.findall('uniprot:citation/uniprot:authorList/uniprot:person', self.ns)]
                                   except:
                                          reference['authors'] = None
                        if citation_type == 'online journal article':
                                   try:
                                          reference['journal'] = ref.find('uniprot:citation', self.ns).get('name')
                                   except:
                                          reference['journal'] = None
                                   try:
                                          reference['date'] = ref.find('uniprot:citation', self.ns).get('date')
                                   except:
                                          reference['date'] = None
                                   try:
                                          reference['title'] = ref.find('uniprot:citation/uniprot:title', self.ns).text
                                   except:
                                          reference['title'] = None
                                   try:
                                          reference['authors'] = [author.get('name') for author in ref.findall('uniprot:citation/uniprot:authorList/uniprot:person', self.ns)]
                                   except:
                                          reference['authors'] = None
                                   try:
                                          reference['pubmedId'] = ref.find('uniprot:citation/uniprot:dbReference[@type="PubMed"]', self.ns).get('id')
                                   except:
                                          reference['pubmedId'] = None
                                   try:
                                          reference['doi'] = ref.find('uniprot:citation/uniprot:dbReference[@type="DOI"]', self.ns).get('id')
                                   except:
                                          reference['doi'] = None

                        if citation_type == 'book':
                                   try:
                                          reference['title'] = ref.find('uniprot:citation/uniprot:title', self.ns).text
                                   except:
                                          reference['title'] = None
                                   try:
                                          reference['authors'] = [author.get('name') for author in ref.findall('uniprot:citation/uniprot:authorList/uniprot:person', self.ns)]
                                   except:
                                          reference['authors'] = None
                                   try:
                                          reference['publisher'] = ref.find('uniprot:citation/uniprot:dbReference[@type="Publisher"]', self.ns).get('id')
                                   except:
                                          reference['publisher'] = None
                                   try:
                                          reference['isbn'] = ref.find('uniprot:citation/uniprot:dbReference[@type="ISBN"]', self.ns).get('id')
                                   except:
                                          reference['isbn'] = None
                                          
                        self.references.append(reference)
                     

              return self.references

       
       
       
       
       def get_ptm(self):
              try:
                     #self.ptm = self.entry.find('uniprot:feature[@type="modified residue"]', self.ns).text
                     for feature in self.entry.findall('uniprot:feature[@type="modified residue"]', self.ns):
                            # Get the position and description of the modification
                            position = feature.find('uniprot:location/uniprot:position', self.ns).get('position')
                            description = feature.get('description')
                            evidence = feature.get('evidence')   
                            self.ptm.append({'Position': position, 'Description': description, 'Evidence': evidence})
              except:
                     self.ptm = None
              return self.ptm
       

       
      