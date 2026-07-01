import pandas as pd
import numpy as np
from rdkit import Chem
from rdkit.Chem import rdFingerprintGenerator, DataStructs

def download_data(link):
    df = pd.read_csv(link)
    return df

def smiles_to_fingerprints(smiles_list):
    fp_gen = rdFingerprintGenerator.GetMorganGenerator(radius=2, fpSize=2048)
    features = []
    for smiles in smiles_list:
        mol = Chem.MolFromSmiles(smiles)
        if mol is not None:
            fp = fp_gen.GetFingerprint(mol)
            arr = np.zeros((2048,))
            DataStructs.ConvertToNumpyArray(fp, arr)
            features.append(arr)
        else:
            features.append(np.zeros(2048))
    return np.array(features)
