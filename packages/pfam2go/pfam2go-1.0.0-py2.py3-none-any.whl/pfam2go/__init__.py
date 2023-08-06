import pandas as pd
import urllib.request
import urllib.error
import requests
import sys
import re
import json
from urllib.parse import quote

"""
pfam2go

A package to match Pfam accession numbers to corresponding GO terms.
"""

__version__ = "1.0.0"
__author__ = 'Konstantin Volzhenin'
__credits__ = 'Sorbonne University, LCQB'


def init():
    url = 'http://current.geneontology.org/ontology/external2go/pfam2go'

    try:
        uf = urllib.request.urlopen(url)
        raw_data = uf.read().decode("utf-8")
        data = _raw_data_to_frame(raw_data)
    except urllib.error.HTTPError:
        # log.warning(
        #     "WARNING: The mapping from the original website "
        #     "http://current.geneontology.org/ontology/external2go/pfam2go could not be processed. \n "
        #     "Probably, it was deleted or changed. The backup version will be used. Please report this warning.")
        with open('pfam2go_backup', 'r') as f:
            raw_data = f.read()
            data = _raw_data_to_frame(raw_data)

    return data


def pfam2go(pfam_seqs):
    data = init()[['Pfam accession', 'GO accession']]

    if type(pfam_seqs) is str:
        pfam_list = [pfam_seqs]
    else:
        try:
            pfam_list = list(pfam_seqs)
        except TypeError:
            raise Exception(
                'The input data format of Pfam sequences has to be iterable (list, Series, etc.) or string.')

    data_match = data[data['Pfam accession'].isin(pfam_list)].reset_index(drop=True)

    data_match[['name', 'definition.text', 'aspect']] = data_match['GO accession'].apply(_quickgo_search)

    return data_match


def _raw_data_to_frame(raw_data):
    data = raw_data.splitlines()
    data = [i for i in data if '!' not in i]

    data_listed = []

    pattern = re.compile('Pfam:(PF\d*)\s*(.*)\s*>\s*GO:(.*)\s*;\s*(.*)')
    for line in data:
        line_re = pattern.match(line)
        line = [line_re.group(i + 1) for i in range(4)]
        data_listed.append(line)

    return pd.DataFrame.from_records(data_listed, columns=('Pfam accession', 'Pfam name', 'GO name', 'GO accession'))


def _quickgo_search(query):
    request_url = "https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/{}".format(quote(query))

    r = requests.get(request_url, headers={"Accept": "application/json"})

    if not r.ok:
        r.raise_for_status()
        sys.exit()

    response = r.text
    response = pd.json_normalize(json.loads(response)['results'])
    response = response[response['isObsolete'] == False][['id', 'name', 'definition.text', 'aspect']]
    response = response[response['id'] == query].loc[0, :]
    response.drop('id', inplace=True)

    return response
