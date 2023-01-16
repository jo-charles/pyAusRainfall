from imblearn.under_sampling import RandomUnderSampler
from sklearn.preprocessing import StandardScaler
import pandas as pd

def select():
    df = pd.read_csv('../data/weatherAUS_preprocessed.csv', index_col=0)
    data = df.drop('RainTomorrow', axis=1)
    target = df['RainTomorrow']
    rUs = RandomUnderSampler()
    data, target = rUs.fit_resample(data, target)
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data)
    selected = df.sample()
    selected_features = selected.drop('RainTomorrow', axis=1)
    selected_target = selected['RainTomorrow']
    selected_scaled = scaler.transform(selected_features)
    
    
    return selected, selected_scaled, selected_target
