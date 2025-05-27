#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Defines a class BaseGeometry with an unimplemented area method."""


class BaseGeometry:
    """Base class for geometry objects."""

    def area(self):
        """Raises an exception since area is not implemented.

        Raises:
            Exception: Always raised with the message that area is
            not implemented.
        """
        raise Exception("area() is not implemented")
