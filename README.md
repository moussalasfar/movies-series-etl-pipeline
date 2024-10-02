# ETL Pipeline for Movies and Series Data

## Overview

This project is an **ETL (Extract, Transform, Load) pipeline** designed to automate the process of scraping, transforming, and loading data about the latest movies and series into a MySQL database. The pipeline extracts data from websites, processes it, and loads the structured data into the database while avoiding duplicates.

## Features

- **Scraping**: Extracts movie and series data, including names, ratings, descriptions, categories, and more.
- **Transformation**: Cleans and normalizes the data (removes missing values, ensures consistency in formats).
- **Loading**: Loads data into a MySQL database using `INSERT IGNORE` to prevent duplicate entries.

## Project Structure

```bash
|-- scrape_last_movies_series/
    |-- app.py                # Main script to run the entire ETL process
    |-- scrape_last_movies_series.py  # Script for scraping movie and series data
    |-- transform_data_movies.py # Script for transforming movie data
    |-- transform_data_series.py # Script for transforming series data
    |-- load_data.py           # Script to load the data into MySQL
    |-- transformed_movies.csv # Output file after transforming movies
    |-- transformed_series.csv # Output file after transforming series
    |-- create_tables.sql
    |-- requirements.txt
   
