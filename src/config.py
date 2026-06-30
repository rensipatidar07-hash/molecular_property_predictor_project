DATASETS = {
   
    'tox21': {
        'link': 'https://deepchemdata.s3-us-west-1.amazonaws.com/datasets/tox21.csv.gz',
        'target': 'NR-AR', 
        'type': 'classification'
    },
    'lipophilicity' : {
        'link' : 'https://deepchemdata.s3-us-west-1.amazonaws.com/datasets/Lipophilicity.csv',
        'target' : 'exp',
        'type' : 'regression'
    },
    'bbbp':{
        'link':'https://deepchemdata.s3-us-west-1.amazonaws.com/datasets/BBBP.csv',
        'target' : 'p_np',
        'type': 'classification'
    },
    
    'esol': {
        'link': 'https://raw.githubusercontent.com/deepchem/deepchem/master/datasets/delaney-processed.csv',
        'target': 'measured log solubility in mols per litre',
        'type': 'regression'
    },
}