from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

# URL de conexión
SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:@localhost:3306/coworking_db'

try:
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    connection = engine.connect()
    print("Conexión exitosa a la base de datos")

    # Realiza una consulta simple para verificar la conexión
    result = connection.execute(text("SELECT 1"))
    print("Resultado de la consulta: ", result.fetchone())

except SQLAlchemyError as e:
    print("Error al conectar a la base de datos: ", e)

finally:
    connection.close()
    print("Conexión cerrada")
