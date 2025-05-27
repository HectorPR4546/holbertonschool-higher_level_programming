#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Defines a subclass MyList that extends the built-in list class."""


class MyList(list):
    """A custom list class that prints the list sorted."""

    def print_sorted(self):
        """Prints the list in ascending sorted order.

        The original list is not modified.
        """
        print(sorted(self))
