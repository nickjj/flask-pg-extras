from flask_pg_extras import db_execute_results


def query(db):
    q = """
    SELECT
      pid,
      now() - pg_stat_activity.query_start AS duration,
      query AS query
    FROM
      pg_stat_activity
    WHERE
      pg_stat_activity.query <> ''::text
      AND state <> 'idle'
      AND now() - pg_stat_activity.query_start > interval '5 minutes'
    ORDER BY
      now() - pg_stat_activity.query_start DESC;
    """

    return db_execute_results(db, q)
