
from utils.constants import MESES, SEX_TYPE

def convert_to_uppercase(string):
    """
    Converts the input string to uppercase.

    Args:
        string (str): The string to be converted.

    Returns:
        str: The uppercase version of the input string.
    """
    return string.upper()


def mapear_meses(value):
    return MESES.get(value, "Mes no válido")


def mapear_gender(value):
    return SEX_TYPE.get(value, "Género no válido")