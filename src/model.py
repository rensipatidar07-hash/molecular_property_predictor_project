import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import roc_auc_score

def train_and_test(X, df, dataset_info):
    task = dataset_info['type']
    target = dataset_info['target']
    y = df[target].values
    # add these two lines right after y = df[target].values
    good_rows = ~np.isnan(y)
    X = X[good_rows]
    y = y[good_rows]
    # clean missing values
    # split data (remember stratify for classification)
    # train correct model based on task type
    # print score (RMSE for regression, AUC for classification)
    task = dataset_info['type']
    if task == 'regression':
        X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
        )
        rf = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
        rf.fit(X_train, y_train)

        rf_preds = rf.predict(X_test)

        rf_rmse = np.sqrt(np.mean((y_test - rf_preds) ** 2))
        return rf, rf_rmse
    else:
        X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y)

        #print("Training samples:", X_train.shape[0])
        #print("Testing samples:", X_test.shape[0])

        # Verify balance is maintained
        unique, counts = np.unique(y_test, return_counts=True)
        #print("Test set class distribution:", dict(zip(unique, counts)))
        rf = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
        rf.fit(X_train, y_train)

        # Use predict_proba not predict
        probs = rf.predict_proba(X_test)[:, 1]
        auc = roc_auc_score(y_test, probs)

        return rf, auc