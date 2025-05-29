#!/usr/bin/python3
"""
This module defines the VerboseList class that extends Python's built-in list.
It overrides common list methods to provide additional console output,
demonstrating polymorphism and enhancing visibility into list operations.
"""


class VerboseList(list):
    """
    A subclass of list that provides verbose output for key operations.

    Methods:
        append(item): Adds an item and prints a message.
        extend(iterable): Extends the list and prints the number of items added.
        remove(item): Removes an item and prints a message.
        pop(index=-1): Pops an item and prints what was removed.
    """

    def append(self, item):
        """
        Add an item to the end of the list and print a message.

        Args:
            item: The item to append.
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """
        Extend the list with elements from the iterable and print how many were added.

        Args:
            iterable: An iterable of items to extend the list with.
        """
        length_before = len(self)
        super().extend(iterable)
        num_added = len(self) - length_before
        print(f"Extended the list with [{num_added}] items.")

    def remove(self, item):
        """
        Remove the first occurrence of an item from the list and print a message.

        Args:
            item: The item to remove.
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """
        Remove and return an item at a given position, and print what was removed.

        Args:
            index (int, optional): The index of the item to remove. Defaults to -1 (last item).

        Returns:
            The item that was removed.
        """
        item = self[index] if len(self) > 0 else None
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
