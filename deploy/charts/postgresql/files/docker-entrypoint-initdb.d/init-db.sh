#!/bin/bash

echo "$POSTGRES_USER"

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
    CREATE USER soft_arch_user
    WITH PASSWORD '123456';

    GRANT ALL PRIVILEGES
    ON ALL TABLES IN SCHEMA public
    TO soft_arch_user;

    CREATE DATABASE softarch;
EOSQL

echo "Hello world"