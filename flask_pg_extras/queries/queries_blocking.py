from flask_pg_extras import db_execute_results


def query(db):
    q = """
    SELECT bl.pid AS blocked_pid,
      ka.query AS blocking_statement,
      now() - ka.query_start AS blocking_duration,
      kl.pid AS blocking_pid,
      a.query AS blocked_statement,
      now() - a.query_start AS blocked_duration
    FROM pg_catalog.pg_locks bl
    JOIN pg_catalog.pg_stat_activity a
      ON bl.pid = a.pid
    JOIN pg_catalog.pg_locks kl
      JOIN pg_catalog.pg_stat_activity ka
        ON kl.pid = ka.pid
    ON bl.transactionid = kl.transactionid AND bl.pid != kl.pid
    WHERE NOT bl.granted;
    """

    return db_execute_results(db, q)
