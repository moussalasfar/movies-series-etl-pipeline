import re
import pandas as pd

# Function to transform the series data
def transform_series_data(series_data):
    transformed_data = []
    
    # Iterate through each row in the DataFrame using iterrows()
    for index, serie in series_data.iterrows():
        # Clean and transform each field
        serie_name = serie['serie_name'].strip() if pd.notna(serie['serie_name']) else ""
        season_episode = serie['season_episode'].strip() if pd.notna(serie['season_episode']) else ""
        
        # Clean and split categories
        category = re.sub(r'\s+', ' ', serie['category'].strip()) if pd.notna(serie['category']) else ""
        categories = [cat.strip() for cat in category.split(",")]
        categories_str = ', '.join(categories)  # Convert back to a string

        # Convert series rate to float
        try:
            serie_rate = float(serie['serie_rate'])
        except ValueError:
            serie_rate = None

        # Clean description field
        description = serie['description'].replace('"', '').strip() if pd.notna(serie['description']) else ""

        # Convert duration to an integer (assuming it's in minutes, removing "m")
        try:
            duration = int(serie['duration'].replace('m', '').strip())
        except (ValueError, AttributeError):
            duration = None  # Handle missing or invalid duration

        # Normalize the country field
        country = serie['country'].strip() if pd.notna(serie['country']) else ""

        def country_bref(countr):
            if countr == "United States of America":
                return "USA"
            if countr == "United Kingdom":
                return "UK"
            return countr

        countries = [country_bref(con.strip()) for con in country.split(",")]
        countries_str = ', '.join(countries)  # Convert back to a string

        # Ensure the series link starts with "https://"
        serie_link = serie['movie_link'].strip() if pd.notna(serie['movie_link']) else ""
        if not serie_link.startswith("https://"):
            serie_link = "https://" + serie_link

        # Append all transformed data
        transformed_data.append({
            'serie_name': serie_name,
            'season_episode': season_episode,
            'categories': categories_str,  # Use the string of categories
            'serie_rate': serie_rate,
            'description': description,
            'country': countries_str,  # Use the string of countries
            'duration': duration,
            'serie_link': serie_link
        })

    return transformed_data

# Read the CSV file
df_series = pd.read_csv("C:\\Users\\acer\\OneDrive\\Bureau\\ID1\\web scrapping\\last_series.csv")

# Transform the data
transformed_series_data = transform_series_data(df_series)

# Convert the transformed data back to a DataFrame
transformed_series_df = pd.DataFrame(transformed_series_data)

# Drop rows with any missing (NaN) values
transformed_series_df_clean = transformed_series_df.dropna()

# Print the transformed data
print(transformed_series_df_clean)

# Optionally, save the transformed data back to a new CSV file
transformed_series_df_clean.to_csv("C:\\Users\\acer\\OneDrive\\Bureau\\ID1\\web scrapping\\scrape_last_movies_series\\transformed_series.csv", index=False)

print("Transformation complete and data saved to transformed_series.csv")
