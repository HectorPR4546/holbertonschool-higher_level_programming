#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Defines an abstract class Animal and two subclasses Dog and Cat."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class for animals."""

    @abstractmethod
    def sound(self):
        """Abstract method to return the sound made by the animal."""
        pass


class Dog(Animal):
    """Concrete class representing a dog."""

    def sound(self):
        """Returns the sound of a dog.

        Returns:
            str: The sound "Bark".
        """
        return "Bark"


class Cat(Animal):
    """Concrete class representing a cat."""

    def sound(self):
        """Returns the sound of a cat.

        Returns:
            str: The sound "Meow".
        """
        return "Meow"
