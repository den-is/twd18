#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
    CREATE USER rango;
    CREATE DATABASE rango;
    GRANT ALL PRIVILEGES ON DATABASE rango TO rango;
EOSQL
