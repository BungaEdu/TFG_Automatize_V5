import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MySQL",
    database="log_automatize_1"
)

# El código inicial para crear la tabla es el siguiente:
# CREATE TABLE nombre_de_la_tabla (
# 	idNumEjecucion INT,
# 	ejecution_moment DATETIME,
# 	doc_path VARCHAR(255),
# 	xpath VARCHAR(255),
# 	urlDoc VARCHAR(255),
# 	urlActual VARCHAR(255),
# 	urlPost VARCHAR(255),
# 	controlErrores VARCHAR(255)
# );
