#!/usr/bin/env python3
"""Module for XML serialization and deserialization."""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a Python dictionary to an XML file.
    
    Args:
        dictionary (dict): The dictionary to serialize
        filename (str): The filename to save the XML data
    """
    try:
        # Create the root element
        root = ET.Element("data")
        
        # Add each dictionary item as a child element
        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)
        
        # Create the ElementTree and write to file
        tree = ET.ElementTree(root)
        tree.write(filename, encoding='utf-8', xml_declaration=True)
    
    except Exception as e:
        print(f"Error serializing to XML: {e}")
        raise


def deserialize_from_xml(filename):
    """Deserialize an XML file to a Python dictionary.
    
    Args:
        filename (str): The XML file to deserialize
        
    Returns:
        dict: The deserialized dictionary
    """
    try:
        # Parse the XML file
        tree = ET.parse(filename)
        root = tree.getroot()
        
        # Reconstruct the dictionary
        result = {}
        for child in root:
            result[child.tag] = child.text
        
        return result
    
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
        return None
    except ET.ParseError:
        print(f"Error: Invalid XML in {filename}.")
        return None
    except Exception as e:
        print(f"Error deserializing from XML: {e}")
        return None
