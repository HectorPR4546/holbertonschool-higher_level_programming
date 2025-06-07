#!/usr/bin/env python3
"""Module for serializing and deserializing custom objects using pickle."""

import pickle


class CustomObject:
    """A custom Python class that can be serialized with pickle."""
    
    def __init__(self, name, age, is_student):
        """Initialize the CustomObject.
        
        Args:
            name (str): The name of the person
            age (int): The age of the person
            is_student (bool): Whether the person is a student
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the object's attributes in a formatted way."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the current instance and save to a file using pickle.
        
        Args:
            filename (str): The file to save the serialized object to
            
        Returns:
            bool: True if successful, False if an error occurred
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
            return True
        except (pickle.PicklingError, IOError, Exception):
            return False

    @classmethod
    def deserialize(cls, filename):
        """Deserialize an instance from a file using pickle.
        
        Args:
            filename (str): The file to load the serialized object from
            
        Returns:
            CustomObject or None: The deserialized object or None if error
        """
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except (pickle.UnpicklingError, FileNotFoundError, EOFError, Exception):
            return None
