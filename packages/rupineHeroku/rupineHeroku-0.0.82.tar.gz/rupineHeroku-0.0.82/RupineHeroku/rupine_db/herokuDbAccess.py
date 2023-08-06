from pgcopy import CopyManager
import psycopg2

def connect(user,pw,host,Port,database):
    heroku_db_url = "postgres://{}:{}@{}:{}/{}".format(user,pw,host,Port,database)
    connection =  psycopg2.connect(heroku_db_url, sslmode='require')
    return connection

def fetchDataInDatabase(sql:str, params:list, connection):
    cursor = connection.cursor()
    cursor.execute(sql,params)
    result = cursor.fetchall()
    return result

def insertDataIntoDatabase(sql:str, params:list, connection):    
    
    cursor = connection.cursor()
    try:
        cursor.execute(sql,params)
        result = cursor.fetchall()
        connection.commit()
        cursor.close()
        if len(result) > 0:
            return result
        return None
    except Exception as e:
        connection.commit()
        cursor.close()
        return e

def insertBulkDataIntoDatabase(tableAndSchema:str, columns:tuple, params:tuple, connection):    
    
    cursor = connection.cursor()
    try:
        mgr = CopyManager(connection, tableAndSchema, columns)
        mgr.copy(params)
        
        connection.commit()
        cursor.close()
        return None
    except Exception as e:
        connection.commit()
        cursor.close()
        return e