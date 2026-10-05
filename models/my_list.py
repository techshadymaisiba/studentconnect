class MyList:
    """Manage a list of saved items."""

    def __init__(self):
        """Initialize an empty list of items."""
        self.items = []

    def add_item(self, item):
        """Add an item if it is not already in the list."""
        if item in self.items:
            return False

        self.items.append(item)
        return True

    def remove_item(self, item):
        """Remove an item from the list if it exists."""
        if item in self.items:
            self.items.remove(item)
            return True

        return False

    def get_items(self):
        """Return all items in the list."""
        return self.items

    def contains(self, item):
        """Check whether an item is already in the list."""
        return item in self.items