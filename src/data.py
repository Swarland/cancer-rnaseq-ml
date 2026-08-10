import pandas as pd

def remove_zero_variance(x_df):
    """
    Takes in an expression dataset and filters out genes with zero variance

    inputs (pandas.DataFrame): x_df

    outputs (pandas.DataFrame): filtered expression df
    """

    zero_var_cols = x_df.columns[x_df.nunique() == 1].tolist()

    print(
        f"Removing {len(zero_var_cols)} zero-variance genes."
    )

    return x_df.drop(columns=zero_var_cols)



def load_data(expression_path="../data/raw/TCGA-PANCAN-HiSeq-801x20531/data.csv",
    labels_path="../data/raw/TCGA-PANCAN-HiSeq-801x20531/labels.csv"):
    """
    Load the TCGA gene expression dataset, verify sample alignment,
    remove zero-variance genes, and return feature and label DataFrames.

    Returns

    X_df : pandas.DataFrame
        Gene expression matrix (samples × genes).

    y_df : pandas.DataFrame
        Sample labels indexed by sample ID.
    
    """

    ## loads files
    X_df = pd.read_csv(expression_path)
    y_df = pd.read_csv(labels_path)

    if not (X_df["Unnamed: 0"] == y_df["Unnamed: 0"]).all():
        raise ValueError("Sample IDs do not match.")

    ## sets index and converts y to 1D array
    X_df = X_df.set_index("Unnamed: 0")
    y_df = y_df.set_index("Unnamed: 0")["Class"]
    
    ## removes zero variance
    X_df = remove_zero_variance(X_df)

    return X_df, y_df