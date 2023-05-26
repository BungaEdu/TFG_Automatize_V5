from Program.data.BaseDatosConector import mydb


def controlId():
    mycursor = mydb.cursor()

    mycursor.execute("SELECT COUNT(*) FROM log")
    countRegistros = mycursor.fetchone()[0]
    mycursor.close()

    if countRegistros != 0:
        mycursor = mydb.cursor()
        mycursor.execute(f"SELECT idNumEjecucion FROM log LIMIT {countRegistros - 1}, 1")
        resultadoId = mycursor.fetchone()
        mycursor.close()
        id = resultadoId[0] + 1
    else:
        id = 1
    return id
