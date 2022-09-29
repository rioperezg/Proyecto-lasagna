from pyclbr import Function
#Informacion sobre el tiempo que la lasagna debe cocinarse y tiempo de preparacion de la lasagna
EXPECTED_BAKE_TIME = 40 
PREPARATION_TIME = 2
#funcion que defina cuanto tiempo le queda a la lasagna en el horno
def bake_time_remaining(elapsed_bake_time):
    return (EXPECTED_BAKE_TIME - elapsed_bake_time)
#funcion que calcule el tiempo de coccion de la lasagna en funcion del numero de capas
def preparation_time_in_minutes(number_of_layers):
    return number_of_layers * PREPARATION_TIME
#funcion que defina cuanto tiempo se lleva cocinando la lasagna teniendo en cuenta el tiempo de la preparacion y el tiempo que ya lleva cocinandose
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time

