def crear_diccionario(claves, valores):
    # Verificar que ambas listas tengan la misma longitud
    if len(claves) != len(valores):
        return "Error: Las listas deben tener la misma longitud."
    
    # Crear el diccionario manualmente
    diccionario = {}
    for i in range(len(claves)):
        diccionario[claves[i]] = valores[i]
    return diccionario

# Ejemplo de uso
claves = ["nombre", "edad", "ciudad"]
valores = ["Juan", 25, "Madrid"]

resultado = crear_diccionario(claves, valores)
print(resultado)
