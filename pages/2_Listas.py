import streamlit as st
import pandas as pd

st.title("Método 2: Desde una Lista de Listas")

st.markdown("""
### Ejercicio
En este ejercicio debes crear un DataFrame partiendo de una **lista de listas** que represente el inventario de una tienda de tecnología.

1. Crea una lista de listas donde cada sub-lista contenga información de un producto: 
   `[Nombre del producto, Categoría, Precio, Cantidad en stock]`
   Agrega al menos 4 productos diferentes.
2. Crea un DataFrame llamado `df_inventario` a partir de esta lista y pásale el parámetro `columns=[]` definiendo cómo se llamarán tus columnas.
3. Muestra el DataFrame en la aplicación usando `st.dataframe()`.
""")

st.subheader("Tu resultado:")
# ESTUDIANTE: Escribe tu código a continuación


lista_de_listas = [
   ["Laptop HP 15", "Tecnología", 2500000, 5],
   ["Mouse Logitech", "Accesorios", 80000, 20],
   ["Teclado Mecánico Redragon", "Accesorios", 220000, 15],
   ["Monitor Samsung 24\"", "Tecnología", 900000, 8],
   ["Disco Duro Externo 1TB", "Almacenamiento", 300000, 12],
   ["Memoria USB 64GB", "Almacenamiento", 45000, 30],
   ["Silla Gamer", "Muebles", 650000, 4],
   ["Impresora Epson", "Tecnología", 750000, 6],
   ["Audífonos Sony", "Audio", 180000, 18],
   ["Router TP-Link", "Redes", 120000, 10]
]

df_inventario = pd.DataFrame(lista_de_listas, columns=["Nombre del producto", "Categoría", "Precio", "Cantidad en stock"])
st.dataframe(df_inventario)
