import pandas as pd
import urllib.request
import urllib.error
import requests
import numpy as np
import sys
import re
import json
from typing import Iterable, Union
from urllib.parse import quote

'''
pfam2go

A package to match Pfam accession numbers to corresponding GO terms. 
pfam2go method provides the Go term accession number, the name along with a short description and the function type.
'''

__version__ = "1.1.0"
__author__ = 'Konstantin Volzhenin'
__credits__ = 'Sorbonne University, LCQB'

def pfam2go(pfam_seqs: Union[Iterable[str], str]) -> pd.DataFrame:
    """
    :param pfam_seqs: string or an Iterable object containing strings (e.g, list).
    :return pd.Dataframe containing GO terms for all corresponding Pfam numbers. Dataframe contains 5 string fields:
        - Pfam accession number
        - GO accession number,
        - GO name,
        - GO definition
        - GO functional aspect

    One Pfam number can correspond to several GO terms.
    In case the information about a specific GO term has not been found in QuickGO the last 3 columns will be assigned to NaN.
    """

    data = _data_init()[['Pfam accession', 'GO accession']]

    if type(pfam_seqs) is str:
        pfam_list = [pfam_seqs]
    else:
        try:
            pfam_list = list(pfam_seqs)
        except TypeError:
            raise Exception(
                'The input data format of Pfam sequences has to be iterable (list, Series, etc.) or string.')

    data_match = data[data['Pfam accession'].isin(pfam_list)].reset_index(drop=True)

    data_match[['name', 'definition', 'aspect']] = data_match['GO accession'].apply(_quickgo_search)

    return data_match


'''
_data_init

The _data_init is a private function that uploads the Pfam-GO mapping from 
http://current.geneontology.org/ontology/external2go/pfam2go

If this link does not function properly the backup version will be used.
'''


def _data_init() -> pd.DataFrame:
    url = 'http://current.geneontology.org/ontology/external2go/pfam2go'

    try:
        uf = urllib.request.urlopen(url)
        raw_data = uf.read().decode("utf-8")
        data = _raw_data_to_frame(raw_data)
    except urllib.error.HTTPError:
        sys.stderr.write(
            "WARNING: The mapping from the original website "
            "http://current.geneontology.org/ontology/external2go/pfam2go can not be processed. \n "
            "Probably, it was deleted or changed. The backup version will be used.")
        with open('pfam2go_backup', 'r') as f:
            raw_data = f.read()
            data = _raw_data_to_frame(raw_data)

    return data


'''
_raw_data_to_frame

The _raw_data_to_frame is a private function that converts the original Pfam-GO catalogue to pd.Dataframe
'''


def _raw_data_to_frame(raw_data: str) -> pd.DataFrame:
    data = raw_data.splitlines()
    data = [i for i in data if '!' not in i]

    data_listed = []

    pattern = re.compile('Pfam:(PF\d*)\s*(.*)\s*>\s*GO:(.*)\s*;\s*(.*)')
    for line in data:
        line_re = pattern.match(line)
        line = [line_re.group(i + 1) for i in range(4)]
        data_listed.append(line)

    return pd.DataFrame.from_records(data_listed, columns=('Pfam accession', 'Pfam name', 'GO name', 'GO accession'))


'''
_quickgo_search

The _quickgo_search is a private function that performs an id search across the QuickGO database 
to find the following information for every GO term:

-name
-description
-aspect (function type): can be either a molecular function, a biological process or a cellular component.
'''


def _quickgo_search(query: str) -> pd.Series:
    request_url = "https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/{}".format(quote(query))

    r = requests.get(request_url, headers={"Accept": "application/json"})

    response = r.text
    response_dict = json.loads(response)

    if 'results' in response_dict.keys():

        response = response_dict['results']
        response_non_obsolete = list(filter(lambda item: item['isObsolete'] == False, response))

        if len(response_non_obsolete) < 1:
            return pd.Series([np.nan, np.nan, np.nan])

        return pd.Series([response_non_obsolete[0]['name'],
                          response_non_obsolete[0]['definition']['text'],
                          response_non_obsolete[0]['aspect']])
    else:
        return pd.Series([np.nan, np.nan, np.nan])
