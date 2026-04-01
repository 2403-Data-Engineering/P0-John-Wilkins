# Import the dataclass decorator from the dataclasses module
# This helps automatically generate common methods like __init__, __repr__, etc.
from dataclasses import dataclass


# The @dataclass decorator tells Python to treat this class as a data container
# It automatically creates an __init__ method and other useful methods for you
@dataclass
class Classes:
    # This defines an attribute called 'class_name'
    # The ': str' means this attribute should be a string
    class_name: str