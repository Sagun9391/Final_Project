# recommendation_model.py
from Tour.models.Package import Package
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

# Fetch all packages from the database
packages = Package.objects.all()

# Extract attributes for each package and store them in lists
package_names = [package.name for package in packages]
package_countries = [package.country.name for package in packages]
package_prices = [package.price for package in packages]
package_descriptions = [package.description for package in packages]

# Create a list of strings containing the combined attributes
combined_attributes = [f"{name} {country} {price} {description}" for name, country, price, description in
                       zip(package_names, package_countries, package_prices, package_descriptions)]

# Initialize the CountVectorizer and compute the count matrix
count_vectorizer = CountVectorizer()
count_matrix = count_vectorizer.fit_transform(combined_attributes)

# Calculate the cosine similarity matrix
cosine_sim = cosine_similarity(count_matrix)


def get_package_recommendations(package_name, country, price, description):
    # Create a string representing the input package's attributes
    input_package_attributes = f"{package_name} {country} {price} {description}"

    # Calculate the cosine similarity of the input package with all packages in the database
    input_package_vector = count_vectorizer.transform([input_package_attributes])
    cosine_similarities = cosine_similarity(input_package_vector, count_matrix)

    # Get the indices of packages sorted by similarity (in descending order)
    package_indices = cosine_similarities.argsort()[0][::-1]

    # Exclude the input package itself (if it exists in the recommendations)
    package_indices = [idx for idx in package_indices if package_names[idx] != package_name]

    # Get the top 5 similar packages
    top_package_indices = package_indices[:5]

    # Retrieve the names of the top similar packages
    recommended_package_names = [package_names[idx] for idx in top_package_indices]

    return recommended_package_names
