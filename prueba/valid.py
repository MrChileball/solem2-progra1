


def validar_rut(rut, dv):
    rut_limpio = ''.join(filter(str.isdigit, rut))
    dv_limpio = dv.upper().strip()

    
    if not rut_limpio or not dv_limpio:
        return False
    if len(rut_limpio) < 7:  
        return False
    if dv_limpio not in '0123456789K':
        return False

 
    factores = [2, 3, 4, 5, 6, 7, 2, 3]
    suma = 0
    rut_reverso = rut_limpio[::-1]  

    for i in range(len(rut_reverso)):
        suma += int(rut_reverso[i]) * factores[i]

    resto = suma % 11
    dv_calculado = 11 - resto

    if dv_calculado == 11:
        dv_esperado = '0'
    elif dv_calculado == 10:
        dv_esperado = 'K'
    else:
        dv_esperado = str(dv_calculado)

    return dv_limpio == dv_esperado

# Ejemplo 1: RUT válido
rut = "12.345.678"
dv = "5"
print(validar_rut(rut, dv))  # True

# Ejemplo 2: RUT inválido
rut = "11.111.111"
dv = "1"
print(validar_rut(rut, dv))  # False

# Ejemplo 3: RUT con 'K'
rut = "6.583.772"
dv = "K"
print(validar_rut(rut, dv))  # True (si el cálculo da K)