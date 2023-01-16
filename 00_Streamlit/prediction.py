import joblib

def predict(data):
    clf_rf = joblib.load("../04_Model_Interpretability/rf_model.sav")
#    y_pred_test = clf_rf.predict(data)
    y_probas_test = clf_rf.predict_proba(data)
    y_pred_test = (y_probas_test[:,1] >= 0.485).astype(bool)
    return y_pred_test
