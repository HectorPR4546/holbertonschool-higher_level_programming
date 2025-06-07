#!/usr/bin/env python3
"""Module for converting CSV data to JSON format."""

import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert CSV data to JSON and write to data.json.
    
    Args:
        csv_filename (str): The filename of the input CSV file
        
    Returns:
        bool: True if conversion was successful, False otherwise
    """
    try:
        # Read CSV data and convert to list of dictionaries
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]
        
        # Serialize to JSON and write to file
        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)
        
        return True
    
    except FileNotFoundError:
        print(f"Error: The file {csv_filename} was not found.")
        return False
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False
