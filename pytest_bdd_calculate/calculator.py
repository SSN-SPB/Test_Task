class Calculator:
    def __init__(self):
        self.values = []
        self.result = None

    def enter(self, value):
        """Add a value to the calculator."""
        self.values.append(value)

    def multiply(self):
        """Multiply all entered values."""
        if len(self.values) < 2:
            raise ValueError("Need at least 2 values to multiply")
        
        self.result = 1
        for value in self.values:
            self.result *= value
        
        return self.result

    def get_result(self):
        """Get the current result."""
        return self.result
