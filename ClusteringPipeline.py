import pandas as pd
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

class ClusteringPipeline:
    def __init__(self, raw_data_path, new_data_path):
        # Alustaa ClusteringPipeline-luokan
        self.raw_data_path = raw_data_path
        self.new_data_path = new_data_path
        self.raw_data = None
        self.new_data = None
        self.scaler = StandardScaler()  # Määrittele skaalainstanssina

    def load_data(self):
        # Lataa raakadatan ja uuden datan tiedostot
        self.raw_data = pd.read_csv(self.raw_data_path, delimiter=';')
        self.new_data = pd.read_csv(self.new_data_path, delimiter=';')

    def preprocess_data(self):
        # Esikäsittele dataa
        # Poistaa 'target_column'-sarakkeen ja skaalaa ominaisuudet
        raw_features = self.raw_data.drop(columns=['target_column']).values  # Poista sarakkeet DataFramesta
        scaled_features = self.scaler.fit_transform(raw_features)
        
        # Lisää skaalatut ominaisuudet takaisin DataFrameen
        self.raw_data['scaled_feature1'] = scaled_features[:, 0]
        self.raw_data['scaled_feature2'] = scaled_features[:, 1]
        self.raw_data['scaled_feature3'] = scaled_features[:, 2]

        # Kouluttaa klusterointimallin alkuperäiselle datalle
        kmeans = KMeans(n_clusters=3, random_state=50)
        self.raw_data['cluster'] = kmeans.fit_predict(scaled_features)

    def cluster_new_data(self):
        # Klusteroi uusi data
        # Poista 'target_column'-sarakkeet ja skaalaa ominaisuudet
        new_raw_features = self.new_data.drop(columns=['target_column']).values
        scaled_new_features = self.scaler.transform(new_raw_features)
        
        # Lisää skaalatut ominaisuudet takaisin DataFrameen
        self.new_data['scaled_feature1'] = scaled_new_features[:, 0]
        self.new_data['scaled_feature2'] = scaled_new_features[:, 1]
        self.new_data['scaled_feature3'] = scaled_new_features[:, 2]

        # Kouluttaa klusterointimallin uudelle datalle
        kmeans = KMeans(n_clusters=3, random_state=50)
        self.new_data['cluster'] = kmeans.fit_predict(scaled_new_features)

    def evaluate_clusters(self):
        # Arvioi klusteroinnin onnistuminen
        # Laske silhouette-pisteet alkuperäiselle ja uudelle datalle
        silhouette_raw = silhouette_score(self.raw_data[['scaled_feature1', 'scaled_feature2', 'scaled_feature3']], self.raw_data['cluster'])
        silhouette_new = silhouette_score(self.new_data[['scaled_feature1', 'scaled_feature2', 'scaled_feature3']], self.new_data['cluster'])

        # Tulosta silhouette-pisteet
        print("Silhouette-pisteet raakadatalle:", silhouette_raw)
        print("Silhouette-pisteet uudelle datalle:", silhouette_new)
    
    def visualize_clusters(self):
        plt.figure(figsize=(10, 5))
        plt.subplot(1, 2, 1)
        plt.scatter(self.raw_data['scaled_feature1'], self.raw_data['scaled_feature2'], c=self.raw_data['cluster'], cmap='viridis')
        plt.title('Clustering Results - Raw Data')
        plt.xlabel('Scaled Feature 1')
        plt.ylabel('Scaled Feature 2')

        plt.subplot(1, 2, 2)
        plt.scatter(self.new_data['scaled_feature1'], self.new_data['scaled_feature2'], c=self.new_data['cluster'], cmap='viridis')
        plt.title('Clustering Results - New Data')
        plt.xlabel('Scaled Feature 1')
        plt.ylabel('Scaled Feature 2')

        plt.tight_layout()
        plt.show()

    def run_pipeline(self):
        # Suorittaa putken
        self.load_data()
        self.preprocess_data()
        self.cluster_new_data()
        self.evaluate_clusters()
        self.visualize_clusters()

if __name__ == "__main__":
    # Määritä raakadatan ja uuden datan tiedostopolut
    raw_data_path = "raw_data.csv"
    new_data_path = "new_data.csv"

    # Luo ja suorita putki
    pipeline = ClusteringPipeline(raw_data_path, new_data_path)
    pipeline.run_pipeline()
