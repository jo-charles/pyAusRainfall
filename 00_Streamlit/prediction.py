import joblib

def predict(data):
    clf_rf = joblib.load("../04_Model_Interpretability/rf_model.sav")
#    y_pred_test = clf_rf.predict(data)
    y_probas_test = clf_rf.predict_proba(data)
    y_pred_test = (y_probas_test[:,1] >= 0.5).astype(bool)
    if y_pred_test == True:
        confidence = y_probas_test[:,1]
    else :
        confidence = y_probas_test[:,0]
    return y_pred_test, confidence
