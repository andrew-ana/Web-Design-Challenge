## Data Visualization
# Andrew Anastasiades | @andrew-ana   
# Welcome! 

# Dependencies
import pandas as pd

# File Paths
data_csv_path = "Resources/cities.csv"
data_html_path = "Resources/cities.html"

# CSV Conversion
df = pd.read_csv(data_csv_path)
df.to_html(data_html_path)