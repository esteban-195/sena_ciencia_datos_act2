import streamlit as st
import pandas as pd

st.title("Bases de Datos en la Nube: Firebase Firestore")

st.markdown("""
### Ejercicio
Firebase es otra opción excelente adoptada por múltiples startups para almacenar datos en tiempo real.

**Instrucciones:**
1. Asume que se te proporcionó un archivo de credenciales de servicio `llave_secreta.json`.
2. Escribe el **código teórico (usando st.code() o conectándote si tienes tu propia bd)** que emplearías con `firebase_admin` para arrancar la aplicación y obtener el cliente de la base de datos.
3. El objetivo sería conectarse a la colección `vehiculos` de tu Firestore y traer todos los documentos.
4. Indica cómo convertirías la respuesta iterando los documentos para extraer su `to_dict()`.
5. Convierte esa lista a un DataFrame `df_firebase` final.
""")

st.subheader("Tu resultado:")
st.markdown("Escribe en la parte de abajo el código que usarías para lograr el objetivo. Si usas código comentado/teórico, compártelo adentro de `st.code()`.")

# ESTUDIANTE: Escribe tu código a continuación

st.code("""
    import streamlit as st
    import pandas as pd
    import firebase_admin
    from firebase_admin import credentials, firestore
        
    #Cargar credenciales desde archivo JSON
    cred =  credentials.Certificate("llave_secreta.json")
    
    #Inicializar la aplicacion Firebase
    firebase_admin.initialize_app(cred)
    
    #Obtener cliente de Firestore
    db = firestore.client()
        
    #Conectarse a la coleccion "vehiculos"
    coleccion = db.collection("vehiculos")
        
    #Traer los documentos
    documentos = coleccion.stream()
        
    #Convertir cada documento a diccionario
    lista_vehiculos[]
        
    for doc in documentos:
        datos = doc.to_dict()
        lista_vehiculos.append(datos)
        
    df_firebase = pd.Dataframe(lista_vehiculos)
    st.dataframe(df_firebase)        
    
""", language= "python" )
