def slice_simple():
    texto = "Awesome"
    texto = texto.lower()
    print(texto[0:3])
    a = int((len(texto)/2)-1)
    b = int((len(texto)/2)+2)
    print(texto[a:b])
    print(texto[0:7])
   

    # Código a implementar, se debe utilizar la variable 'texto' para resolver el ejercicio.
    # No se debe modificar la definición de la función, ni ingresar otro valor mediante input.


# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_slice_simple_test.py` o `python tp3_slice_simple_test.py`
