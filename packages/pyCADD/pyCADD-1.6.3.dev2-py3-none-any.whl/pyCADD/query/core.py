import json
import logging
import requests
# from urllib import parse, request

import pandas as pd
import requests
from pyCADD.query.config import BaseQueryCfg

logger = logging.getLogger(__name__)

# API 接口
UNIPROT_URL = 'https://rest.uniprot.org/uniprotkb/'
PDB_URL = 'https://data.rcsb.org/graphql?query='

def query_uniprot(uniprot_id:str, save_path:str=None):

    # params = {
    # 'from': 'ACC+ID',
    # 'to': 'PDB_ID',
    # 'format': 'tab',
    # 'query': uniprot_id
    # }

    # data = parse.urlencode(params).encode('utf-8')
    # req = request.Request(UNIPROT_URL, data)
    
    # with request.urlopen(req) as f:
    #     result = f.read().decode('utf-8')
    
    req = requests.get(UNIPROT_URL + uniprot_id + '?format=json&fields=xref_pdb').text
    if save_path is not None:
        with open(save_path, 'w') as f:
            # f.write(result)
            f.write(req)

def parse_uniport(uniprot_file_path):
    # df = pd.read_csv(uniprot_file_path, sep='\t', header=None, names=['ACC', 'PDB'])
    # pdb_list = list(df.loc[1:, 'PDB'].to_numpy())
    with open(uniprot_file_path) as f:
        data = json.load(f)
    
    data = pd.DataFrame(data['uniProtKBCrossReferences'])
    pdb_list = data['id'].to_list()
    return pdb_list

def query_pdb(pdb_list, save_path=None, quert_cfg=None):

    query_cfg = BaseQueryCfg(pdb_list) if quert_cfg is None else quert_cfg(pdb_list)
    query = query_cfg.get_query()
    query = parse.quote(query)
    req = requests.get(PDB_URL + query)
    data_json = req.json()

    if save_path is not None:
        with open(save_path, 'w') as f:
            f.write(json.dumps(data_json))

    return data_json
