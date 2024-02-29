"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)
    

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """


    """Initialize the SerialGenerator with a starting value."""
    def __init__ (self, start = 100):
        self.start = start
        self.current = start

    """Generate the next serial number."""
    def generate(self):
        serial_number = self.current
        self.current += 1
        return serial_number
    
    """Reset the serial number generator to its initial state."""
    def reset(self):
        self.current = self.start
        serial_number = self.current
        return serial_number




# serial = SerialGenerator()

# print(serial.generate())