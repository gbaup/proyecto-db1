def validar_cedula(cedula):
    cedula = str(cedula)

    if len(cedula) < 8:
        cedula = cedula.zfill(8)

    numero_base = cedula[:-1]
    digito_verificador = int(cedula[-1])

    factores = [2, 9, 8, 7, 6, 3, 4]

    suma = sum(int(d) * f for d, f in zip(numero_base, factores))

    resto = suma % 10
    digito_calculado = (10 - resto) if resto != 0 else 0

    return digito_calculado == digito_verificador
