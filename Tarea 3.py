from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['libro_recetas']
coleccion = db['recetas']

def agregar_receta():
    try:
        coleccion.insert_one({
            'nombre': input("Nombre de la receta: "),
            'ingredientes': input("Ingredientes (separados por comas): "),
            'pasos': input("Pasos para la receta: ")
        })
        print("Receta agregada con éxito.")
    except Exception as e:
        print(f"Error al agregar receta: {e}")

def actualizar_receta():
    try:
        coleccion.update_one(
            {'nombre': input("Nombre de la receta a actualizar: ")},
            {'$set': {
                'nombre': input("Nuevo nombre de la receta: "),
                'ingredientes': input("Nuevos ingredientes (separados por comas): "),
                'pasos': input("Nuevos pasos: ")
            }}
        )
        print("Receta actualizada con éxito.")
    except Exception as e:
        print(f"Error al actualizar receta: {e}")

def eliminar_receta():
    try:
        coleccion.delete_one({'nombre': input("Nombre de la receta a eliminar: ")})
        print("Receta eliminada con éxito.")
    except Exception as e:
        print(f"Error al eliminar receta: {e}")

def ver_recetas():
    try:
        recetas = list(coleccion.find({}, {'nombre': 1}))
        if recetas:
            print(f"Total de recetas: {len(recetas)}")
            for receta in recetas:
                print(receta['nombre'])
        else:
            print("No hay recetas disponibles.")
    except Exception as e:
        print(f"Error al ver las recetas: {e}")

def buscar_receta():
    try:
        receta = coleccion.find_one({'nombre': input("Nombre de la receta a buscar: ")}, {'ingredientes': 1, 'pasos': 1})
        if receta:
            print(f"Ingredientes: {receta['ingredientes']}\nPasos: {receta['pasos']}")
        else:
            print("Receta no encontrada.")
    except Exception as e:
        print(f"Error al buscar la receta: {e}")

if __name__ == "__main__":
    while True:
        try:
            print("\n--- Libro de Recetas ---")
            print("1. Agregar nueva receta")
            print("2. Actualizar receta existente")
            print("3. Eliminar receta")
            print("4. Ver listado de recetas")
            print("5. Buscar ingredientes y pasos de receta")
            print("6. Salir")

            opcion = input("Selecciona una opción: ")

            if opcion == '1':
                agregar_receta()
            elif opcion == '2':
                actualizar_receta()
            elif opcion == '3':
                eliminar_receta()
            elif opcion == '4':
                ver_recetas()
            elif opcion == '5':
                buscar_receta()
            elif opcion == '6':
                break
            else:
                print("Opción no válida, por favor elige otra.")
        except Exception as e:
            print(f"Error en la ejecución del programa: {e}")

if _name_ == '_main_':
    menu()

# Cerrar la conexión a la base de datos al terminar
conn.close()
