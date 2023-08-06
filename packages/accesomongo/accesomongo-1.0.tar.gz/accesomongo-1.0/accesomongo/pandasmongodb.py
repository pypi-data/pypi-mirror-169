#!/usr/bin/env python
# coding: utf-8

# In[4]:


def write_df_to_mongoDB(  my_df,                          database_name = 'mydatabasename' ,                          collection_name = 'mycollectionname',
                          server = 'localhost',\
                          mongodb_port = 27017,\
                          chunk_size = 100):
    #"""
    #Esta función toma una lista y crea una colección en MongoDB (debe
    #pproporcionar el nombre de la base de datos, la colección, el puerto para conectarse a la base de datos remota,
    #servidor de la base de datos remota, puerto local para hacer un túnel a la otra máquina)
    #
    #---------------------------------------------------------------------------
    #Parametros / Entrada
    #    my_list: lista enviada a MongoDB
    #    database_name:  nombre de la base de datos
    #
    #    collection_name: nombre de la coleccion (a crear)
    #    server: el servidor donde se aloja la base de datos MongoDB
    #        Ejemplo: server = 'XXX.XXX.XX.XX'
    #    this_machine_port: puerto de la maquina local.
    #        Por example: this_machine_port = '27017'
    #    remote_port: the port where the database is operating
    #        For ejemplo: remote_port = '27017'
    #    chunk_size: El número de elementos de la lista que se enviará en
    #        algun momento al database. Default es 100.
    #
    #Output
    #    Cuando termine imprimira "Done"
    #----------------------------------------------------------------------------
    #26/09/2022: Jorge Guerra. Documentacion
    #"""



    #Para conectar
    # import os
    # import pandas as pd
    # import pymongo
    # from pymongo import MongoClient

    client = MongoClient('localhost',int(mongodb_port))
    db = client[database_name]
    collection = db[collection_name]
    # To write
    collection.delete_many({})  # Destruye la colleccion
    #aux_df=aux_df.drop_duplicates(subset=None, keep='last') # Para evitar repeticiones
    my_list = my_df.to_dict('records')
    l =  len(my_list)
    ran = range(l)
    steps=ran[chunk_size::chunk_size]
    steps.extend([l])

    # Insertar trozos del dataframe
    i = 0
    for j in steps:
        print (j)
        collection.insert_many(my_list[i:j]) # llenar la coleccion
        i = j

    print('Done')
    return


# In[5]:


def createDocsFromDF(df, collection = None, insertToDB=False):
    docs = [] 
    fields = [col for col in df.columns]
    for i in range(len(df)):
        doc = {col:df[col][i] for col in df.columns if col != 'index'}
        for key, val in doc.items():
            # tenemos que hacer esto, porque mongo no reconoce estos tipos np.
            if type(val) == np.int64:
                doc[key] = int(val)
            if type(val) == np.float64:
                doc[key] = float(val)
            if type(val) == np.bool_:
                doc[key] = bool(val)
        docs.append(doc) 
    if insertToDB and collection:
        db.collection.insert_many(docs)
    return docs 


# In[ ]:




