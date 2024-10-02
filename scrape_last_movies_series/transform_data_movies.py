import re
import pandas as pd

# Function to transform the data
def transform_data(movies_data):
    transformed_data = []
    
    # Iterate through each row in the DataFrame using iterrows()
    for index, movie in movies_data.iterrows():
        # Clean and transform each field
        movie_name = movie['movie_name'].strip() if pd.notna(movie['movie_name']) else ""
        category = re.sub(r'\s+', ' ', movie['category'].strip()) if pd.notna(movie['category']) else ""
        categories = [cat.strip() for cat in category.split(",")]

        # Join the list of categories into a string
        categories_str = ', '.join(categories)

        # Convert movie rate to float
        try:
            movie_rate = float(movie['movie_rate'])
        except ValueError:
            movie_rate = None

        description = movie['description'].replace('"', '').strip() if pd.notna(movie['description']) else ""

        # Convert duration to an integer (assuming it's in minutes)
        try:
            duration = int(movie['duration'].replace('min', '').strip())
        except (ValueError, AttributeError):
            duration = None  # Handle missing or invalid duration

        # Normalize the country field
        country = movie['country'].strip() if pd.notna(movie['country']) else ""

        def country_bref(countr):
            if countr == "United States of America":
                return "USA"
            if countr == "United Kingdom":
                return "UK"
            return countr

        countries = [country_bref(con.strip()) for con in country.split(",")]

        # Join the list of countries into a string
        countries_str = ', '.join(countries)

        # Ensure the movie link starts with "https://"
        movie_link = movie['movie_link'].strip() if pd.notna(movie['movie_link']) else ""
        if not movie_link.startswith("https://"):
            movie_link = "https://" + movie_link

        # Append all transformed data
        transformed_data.append({
            'movie_name': movie_name,
            'categories': categories_str,
            'movie_rate': movie_rate,
            'description': description,
            'country': countries_str,
            'release_date': movie['date'],  # Keep date as is
            'duration': duration,
            'movie_link': movie_link
        })

    return transformed_data

# Read the CSV file
df = pd.read_csv("C:\\Users\\acer\\OneDrive\\Bureau\\ID1\\web scrapping\\last_movies.csv")

# Transform the data
transformed_data = transform_data(df)

# Convert the transformed data back to a DataFrame
transformed_df = pd.DataFrame(transformed_data)

# Drop rows with any missing (NaN) values
transformed_movies_df_clean = transformed_df.dropna()

# Print the transformed data
print(transformed_movies_df_clean)

# Optionally, save the transformed data back to a new CSV file
transformed_movies_df_clean.to_csv("C:\\Users\\acer\\OneDrive\\Bureau\\ID1\\web scrapping\\scrape_last_movies_series\\transformed_movies.csv", index=False)

print("Transformation complete and data saved to transformed_movies.csv")
