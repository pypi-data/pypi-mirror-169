# pfam2go 
The pfam2go package provides a short and simple interface to match the Pfam accesion numbres to Gene Ontology annotation data.    
The Pfam - Go term mapping was taken from:
>http://current.geneontology.org/ontology/external2go/pfam2go
> 
>Mitchell et al. (2015) Nucl. Acids Res. 43 :D213-D221

The Go term information is taken from QuickGO:
>https://www.ebi.ac.uk/QuickGO/

### Installation

pfam2go can be installed via pip:
```
pip install pfam2go
```

### Usage

```
pfam2go(pfam_seqs: Union[Iterable[str], str]) -> pd.DataFrame
```
Input:

<em>pfam_seqs</em>: string or an Iterable object containing strings (e.g., list or pd.Series).

Returns:

pd.Dataframe containing GO terms for all corresponding Pfam numbers. Dataframe contains 5 string fields: 
- Pfam accession number 
- GO accession number
- GO name 
- GO definition 
- GO functional aspect  

One Pfam number can correspond to several GO terms.  
In case the information about a specific GO term has not been found in QuickGO the last 3 columns will be assigned to NaN.

### Example

```
from pfam2go import pfam2go  
pfam_list = ['PF00032', 'PF00049', 'PF08463']  
data = pfam2go(pfam_list)  
```