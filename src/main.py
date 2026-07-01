from config import DATASETS
from data_loader import download_data, smiles_to_fingerprints
from model import train_and_test

def main():
    print("Welcome to the ADMET ML Pipeline!")
    choice = input("Type the name of the dataset you want to run: ").strip().lower()

    if choice not in DATASETS:
        print("Error: Dataset not found. Please check your spelling!")
        return
    else:
        info=DATASETS[choice]
        df=download_data(info['link'])
        X = smiles_to_fingerprints(df['smiles']) 
        train_and_test(X, df, info)   
if __name__ == "__main__":
    main()