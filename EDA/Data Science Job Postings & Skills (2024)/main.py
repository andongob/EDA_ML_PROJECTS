"""
Author: Ana Ndongo
Date: 27 December 2024
Description:

LinkedIn is a popular professional networking platform with millions of job postings across various industries.

This dataset provides a raw dump of data science-related job postings collected from LinkedIn. It includes information about job titles, companies, locations, search parameters, and other relevant details.

The main objective of this dataset is not only to provide insights into the data science job market and the skills required by professionals in this field but also to offer users an opportunity to practice their data cleaning skills.

By working with this dataset, users can gain hands-on experience in cleaning and preprocessing raw data, a critical skill for aspiring data scientists.
"""
import os
import sys
from utils.processing import DataLoader
from utils.analyzer import DataAnalyzer


#---------------- CARGAR DATASET -------------------#

# Detectar dinámicamente el directorio raíz del proyecto
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_root)
print("Directorio raíz detectado dinámicamente:", project_root)


# Ruta simplificada al dataset
df_path = os.path.join(project_root, "dataSet")
print(f"Ruta del dataset: {df_path}")
df = "currencies_data.csv"

#---------------- CARGAR Y PROCESAR LOS DATOS -------------------#
try:
    loader = DataLoader(df_path=df_path, df=df)
    df = loader.load_data()
    print("\n--- Dataset cargado correctamente ---")
except FileNotFoundError as e:
    print(f"Error al cargar el dataset: {e}")
    df = None
except ValueError as e:
    print(f"Error de valor en el dataset: {e}")
    df = None

# Si los datos se cargaron, proceder al análisis
if df is not None:
    # Instanciar el analizador
    analyzer = DataAnalyzer(df)

    # Llamadas a los métodos del analizador para verificar si se están cargando o no
    #print(dir(analyzer))  # Verifica que 'nan_summary' esté listado

    analyzer.overview()
    analyzer.duplicates_analysis()
    analyzer.missing_values_analysis()
    analyzer.data_types_analysis()
    print("Columnas categóricas detectadas:", analyzer.columns_cat)
    print("Columnas numéricas detectadas:", analyzer.columns_num)
    #analyzer.nan_summary()
else:
    print("\n--- No se pudo cargar el dataset. Análisis abortado ---")


    #---------------- VISUALIZAR LOS DATOS -------------------#

from utils.visualization import DataVisualizationCoordinator

print("\n--- Visualización Combinada ---")

# Columnas seleccionadas para las visualizaciones
x_col = "Grocery"      # Columna para el eje X del scatterplot
y_col = "Milk"         # Columna para el eje Y del scatterplot
bar_box_col = "Grocery"  # Columna para el barplot y boxplot
cluster_col = "Channel"  # Columna de clusters

# Instanciar el coordinador de visualizaciones
viz_coordinator = DataVisualizationCoordinator(df)

# Generar todas las visualizaciones en una sola ventana
try:
    viz_coordinator.plot_all(x=x_col, y=y_col, column=bar_box_col, clusters=cluster_col)
except KeyError as e:
    print(f"Error en las visualizaciones: {e}")
    print("Columnas disponibles en el DataFrame:", df.columns.tolist())
    