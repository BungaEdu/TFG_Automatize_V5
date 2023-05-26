import mysql

from Program.data.BaseDatosConector import mydb


def insertarRegistro(idNumEjecucion, ejecution_moment, doc_path, xpath, urlDoc, urlActual, urlPost, controlErrores):
    try:
        mycursor = mydb.cursor()

        sql = '''
        INSERT INTO log (
            idNumEjecucion,
            ejecution_moment,
            doc_path,
            xpath,
            enlace_from_doc,
            enlace_from_browser_init,
            enlace_from_browser_post,
            enlace_from_browser_result
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        '''

        values = (
            idNumEjecucion,
            ejecution_moment,
            doc_path,
            xpath,
            urlDoc,
            urlActual,
            urlPost,
            controlErrores
        )

        mycursor.execute(sql, values)
        mydb.commit()

        mycursor.close()

    except mysql.connector.Error as error:
        print(f"Se produjo un error al conectar a la base de datos: {error}")