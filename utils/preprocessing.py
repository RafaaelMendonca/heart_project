from sklearn.preprocessing import MinMaxScaler

class MinMaxScalerClass:
    def __init__(self):
        self.scaler = MinMaxScaler()

    def fit(self, data):
        self.scaler.fit(data)

    def transform(self, data):
        return self.scaler.transform(data)
    
    def fit_transform(self, data):
        return self.scaler.fit_transform(data)