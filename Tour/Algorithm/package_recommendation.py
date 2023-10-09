# Import the libraries
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

# Load the data
df = pd.read_csv('tour_package.csv', encoding='unicode_escape')

# Create a list of columns to keep
columns_to_keep = ['Package_name', 'Country', 'Price', 'Description']

# Create a function to combine the selected columns into a single string
def combine_features(row):
    return ' '.join(row[columns_to_keep])

# Apply the function to create a new column 'combined_features'
df['combined_features'] = df.apply(combine_features, axis=1)

count_vectorizer = CountVectorizer()
count_matrix = count_vectorizer.fit_transform(df['combined_features'])
cosine_sim = cosine_similarity(count_matrix)

# Define a function to get package recommendations
def get_recommendations(package_name, cosine_sim_matrix):
    # Get the index of the package that matches the package name
    idx = df[df['Package_name'] == package_name].index[0]

    # Get the pairwise similarity scores with other packages
    sim_scores = list(enumerate(cosine_sim_matrix[idx]))

    # Sort the packages based on similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the top 5 similar packages (excluding the input package itself)
    top_packages = sim_scores[1:6]

    # Get the package indices
    package_indices = [i[0] for i in top_packages]

    # Return the top 5 recommended package names
    return df['Package_name'].iloc[package_indices]

package_name = "Paragliding in Pokhara"
recommendations = get_recommendations(package_name, cosine_sim)
print(recommendations)
