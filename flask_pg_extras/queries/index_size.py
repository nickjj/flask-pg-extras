from flask_pg_extras import db_execute_results


def query(db):
    q = """
    SELECT c.relname AS name,
      pg_size_pretty(sum(c.relpages::bigint*8192)::bigint) AS size
    FROM pg_class c
    LEFT JOIN pg_namespace n ON (n.oid = c.relnamespace)
    WHERE n.nspname NOT IN ('pg_catalog', 'information_schema')
    AND n.nspname !~ '^pg_toast'
    AND c.relkind='i'
    GROUP BY c.relname
    ORDER BY sum(c.relpages) DESC;
    """

    return db_execute_results(db, q)
