# pfam2go
A Python package designed for a quick search for GO terms given a list of corresponding Pfam accession numbers.

The pfam2go method is designed to take an interable object (list, pd.Series, etc.) that cobtains several Pfam accession numbers, and outputs a pandas Dataframe with all corresponding GO terms along with their characteristics (name, function, short description).

The list of GO terms corresponding to specific Pfam numbers is taken from:
http://current.geneontology.org/ontology/external2go/pfam2go

(Mitchell et al. (2015) Nucl. Acids Res. 43 :D213-D221)

The functional information is taken from https://www.ebi.ac.uk/QuickGO/
