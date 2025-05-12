from tkinter import*
from tkinter import ttk
from tkinter import messagebox

import pymongo

MONGO_HOST= "localhost"
MONGO_PUERTO="27017"
MONGO_TIEMPO_FUERA= 1000

MONGO_URI = f"mongodb://{MONGO_HOST}:{MONGO_PUERTO}/"
MONGO_BASE_DATOS="botilleria"
MONGO_COLLECTION="bebidas"

def mostrar_datos(tabla):
    try:    
        cliente = pymongo.MongoClient(MONGO_URI, serverSelectionTimeoutMS=MONGO_TIEMPO_FUERA)
        base_datos = cliente[MONGO_BASE_DATOS]
        coleccion = base_datos[MONGO_COLLECTION]
        for documento in coleccion.find():
           tabla.insert("",0,text=documento["_id"], values= documento["nombre"])
        
        cliente.close()
    except pymongo.errors.ServerSelectionTimeoutError as errortiempo:
        print("Tiempo exedido "+ errortiempo)
    except pymongo.errors.ConnectionFailure as errorConexion:
        print("Error de conexion "+ errorConexion)

ventana = Tk()
tabla=ttk.Treeview(ventana, columns=2)
tabla.grid(row=1,column=0,columnspan=2)
tabla.heading("#0", text="ID")
tabla.heading("#1", text="NOMBRE")
mostrar_datos(tabla)
ventana.mainloop()