from flask_pg_extras import db_execute_results


def query(db):
    q = """
    SELECT relname AS name,
      seq_scan as count
    FROM
      pg_stat_user_tables
    ORDER BY seq_scan DESC;
    """

    return db_execute_results(db, q)
