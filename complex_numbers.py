import numpy as np

class ComplexNumber(np.dtype):
    """A custom data type to represent complex numbers."""

    name = 'complex128'
    char = 'c'
    itemsize = 16
    fields = [('real', np.float64), ('imag', np.float64)]

def complex_array(data):
    """Create a NumPy array of complex numbers from the given data."""
    return np.array(data, dtype=ComplexNumber)

# Example usage:

complex_array([(1, 2), (3, 4)])
