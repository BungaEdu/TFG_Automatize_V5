from Program.data.BaseDatosConector import mydb


def ejecutar_consulta(query):
    cursor = mydb.cursor()
    cursor.execute(query)
    resultados = cursor.fetchall()
    cursor.close()
    return resultados


print("##################### REGISTROS POR HORA #####################")
queryRegistroPorHora = "SELECT DATE_FORMAT(ejecution_moment, '%Y-%m-%d %H:00:00') AS hora, COUNT(*) AS " \
                       "total_registros FROM log GROUP BY hora "
resultadosRegistroPorHora = ejecutar_consulta(queryRegistroPorHora)
# Imprimir los resultados
for fila in resultadosRegistroPorHora:
    hora, total_registros = fila
    print("Hora:", hora, "Total de registros:", total_registros)


print("##################### EJECUCIONES POR DÍA #####################")
queryEjecucionesPorDia = "SELECT DATE(ejecution_moment) AS dia, COUNT(*) AS num_ejecuciones, MAX(idNumEjecucion) - " \
                         "MIN(idNumEjecucion) AS posiciones_avanzadas FROM log WHERE ejecution_moment >= CURDATE() - " \
                         "INTERVAL 1 WEEK GROUP BY dia "
resultadosEjecucionesPorDia = ejecutar_consulta(queryEjecucionesPorDia)
# Imprimir los resultados por día
for fila in resultadosEjecucionesPorDia:
    dia, num_ejecuciones, posiciones_avanzadas = fila
    print("Día:", dia, "Ejecuciones del programa:", posiciones_avanzadas+1)


print("##################### LINK MÁS REPETIDO #####################")
queryLinkMasRepetido = "SELECT enlace_from_doc, COUNT(*) AS total_repeticiones FROM log GROUP BY enlace_from_doc " \
                       "ORDER BY total_repeticiones DESC LIMIT 1 "
resultadoLinkMasRepetido = ejecutar_consulta(queryLinkMasRepetido)

urlDoc_mas_repetido, total_repeticiones = resultadoLinkMasRepetido[0]
print("El url más repetido es:", urlDoc_mas_repetido, "con un total de repeticiones:", total_repeticiones)


mydb.close()
