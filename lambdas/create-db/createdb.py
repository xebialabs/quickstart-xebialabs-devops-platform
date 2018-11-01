#!/usr/bin/python
import psycopg2
import cfn_resource
import logging

handler = cfn_resource.Resource()

@handler.create
def create_database(event, context):
    props = event['ResourceProperties']

    if not props['DBName']:
        return {
            'Status': 'FAILED',
            'Reason': 'Parameter DBName not found.'
        }
    elif not props['DBUser']:
        return {
            'Status': 'FAILED',
            'Reason': 'Parameter DBUser not found.'
        }
    elif not props['DBPassword']:
        return {
            'Status': 'FAILED',
            'Reason': 'Parameter DBPassword not found.'
        }
    elif not props['DBHost']:
        return {
            'Status': 'FAILED',
            'Reason': 'Parameter DBHost not found.'
        }

    db_name = props['DBName']
    db_user = props['DBUser']
    db_password = props['DBPassword']
    db_host = props['DBHost']

    conn = None
    cursor = None
    try:
        conn = psycopg2.connect(dbname='postgres', user=db_user, host=db_host, password=db_password)
    except:
        return {
            'Status': 'FAILED',
            'Reason': 'Could not connect to the Postgres DB'
        }
    else:
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE %s WITH OWNER %s" % (db_name, db_user))
        conn.commit()
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

    return {
        'Status': 'SUCCESS',
        'Reason': 'Successfully created database %s' % db_name
    }