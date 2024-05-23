from flask import jsonify
from pymongo import MongoClient
import logging

logging.basicConfig(
    filename='src/log/logs.log',
    level=logging.DEBUG,
    format='| %(asctime)s | %(levelname)s | %(message)s |'
)

def conectar():
    try:
        client = MongoClient('mongodb://localhost:27017/')
        db = client['nombre_de_tu_base_de_datos']
        return db
    except Exception as e:
        logging.error(str(e))
        return jsonify({'error': str(e)}), 500

def insertar(tabla):
    try:
        db = conectar()
        collection = db[tabla]

        document = {
            "nombre": "Juan",
            "edad": 30,
            "ciudad": "Madrid"
        }

        result = collection.insert_one(document)

        logging.info(f"Documento insertado con ID: {result.inserted_id}")
        return result
    except Exception as e:
        logging.error(str(e))
        return jsonify({'error': str(e)}), 500

def selecionarUno(tabla, data):
    try:
        db = conectar()
        collection = db[tabla]

        result = collection.find_one(data)

        logging.info(result)
        return result
        # Consultar todos los documentos
        #for doc in collection.find():
            #print(doc)
    except Exception as e:
        logging.error(str(e))
        return jsonify({'error': str(e)}), 500

def selecionar(tabla, data):
    try:
        db = conectar()
        collection = db[tabla]

        result = collection.find(data)

        logging.info(result)
        return result
    except Exception as e:
        logging.error(str(e))
        return jsonify({'error': str(e)}), 500

def actualizarUno(tabla, filtro, data):
    try:
        db = conectar()
        collection = db[tabla]

        update_result = collection.update_one(
            filtro,
            {"$set": data}
        )

        logging.info(f"Documentos actualizados: {update_result.modified_count}")
        return update_result.modified_count
    except Exception as e:
        logging.error(str(e))
        return jsonify({'error': str(e)}), 500

def actualizar(tabla, filtro, data):
    try:
        db = conectar()
        collection = db[tabla]

        update_result = collection.update_many(
            filtro,
            {"$set": data}
        )

        logging.info(f"Documentos actualizados: {update_result.modified_count}")
        return update_result.modified_count
    except Exception as e:
        logging.error(str(e))
        return jsonify({'error': str(e)}), 500

def eliminarUno(tabla, data):
    try:
        db = conectar()
        collection = db[tabla]

        delete_result = collection.delete_one(data)

        logging.info(f"Documentos borrados: {delete_result.deleted_count}")
        return delete_result.deleted_count
    except Exception as e:
        logging.error(str(e))
        return jsonify({'error': str(e)}), 500

def eliminar(tabla, data):
    try:
        db = conectar()
        collection = db[tabla]

        delete_result = collection.delete_many(data)

        logging.info(f"Documentos borrados: {delete_result.deleted_count}")
        return delete_result.deleted_count
    except Exception as e:
        logging.error(str(e))
        return jsonify({'error': str(e)}), 500