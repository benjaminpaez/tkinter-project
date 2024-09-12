import re
from datetime import datetime


def validation_data(legajo, dni, nombre_apellido, email, domicilio, fecha_nac, carrera, ingreso):
    if not (0 <= legajo <= 99999):
        raise ValueError("Legajo incorrecto. Debe ser un numero de 5 digitos")

    if not email or not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        raise ValueError("El correo electronico no es valido")

    if not (0 <= dni <= 99999999):
        raise ValueError("El dni debe ser un numero de 8 digitos")

    if not (2005 <= ingreso <= 2024):
        raise ValueError("El ano de ingreso debe ser entre 2005 y 2024")

    if len(nombre_apellido) > 30:
        raise ValueError("El nombre y apellido no debe ser mayor a 30 caracteres")

    if len(domicilio) > 20:
        raise ValueError("El domicilio no debe superar los 20 caracteres")

    try:
        fecha_nac_date = datetime.strptime(fecha_nac, "%Y-%m-%d")
        limite = datetime(1970, 1, 1)
        if fecha_nac_date <= limite:
            raise ValueError(f"La fecha de nacimiento debe ser posterior a {limite}")

    except ValueError:
        raise ValueError("La fecha debe estar en formato yyyy/mm/dd")

    carreras_disponibles = ['Medicina', 'Ingenieria', 'Veterinaria', 'Economia']

    if carrera not in carreras_disponibles:
        raise ValueError("La carrera seleccionada no existe o no esta disponible.")

    return True, ""
