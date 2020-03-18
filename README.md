# Ayuda Covid 19

Instalación de postgtres:

1. Instalar posgresql:
    sudo apt-get install postgresql
2. Instalar postgis:
    sudo apt-get install postgis
3. Crear Base de datos:
    sudo -u postgres createdb DATABASE_NAME
4. Crear Usuario:
    sudo -u postgres createuser -s DATABASE_USER -P
5.  Entrar en la BBDD:
    sudo -u postgres psql DATABASE_NAME
6.  Otorgar permisos e instalar postgis extension

    GRANT ALL PRIVILEGES ON DATABASE "DATABASE_NAME" TO DATABASE_USER;
    CREATE EXTENSION postgis;
    \q




