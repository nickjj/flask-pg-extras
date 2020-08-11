from flask_pg_extras import db_execute_results


def query(db):
    q = """
    SELECT
      relname AS name,
      n_live_tup AS estimated_count
    FROM
      pg_stat_user_tables
    ORDER BY
      n_live_tup DESC;
    """

    return db_execute_results(db, q)
