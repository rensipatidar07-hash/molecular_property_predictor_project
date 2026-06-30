# data_loader.py

def load_data(url):
    """Downloads dataset from URL, handling compression automatically."""
    print(f"Loading data from: {url}")
    # pandas read_csv automatically detects '.gz' extension and decompresses it!
    return pd.read_csv(url)