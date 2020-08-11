from sqlalchemy.exc import ProgrammingError

from flask_pg_extras import db_execute_results


def query(db):
    q = """
    SELECT query AS qry,
      interval '1 millisecond' * total_time AS exec_time,
      to_char((total_time/sum(total_time) OVER()) * 100, 'FM90D0') || '%'  AS prop_exec_time,
      to_char(calls, 'FM999G999G990') AS ncalls,
      interval '1 millisecond' * (blk_read_time + blk_write_time) AS sync_io_time
    FROM pg_stat_statements WHERE userid = (SELECT usesysid FROM pg_user WHERE usename = current_user LIMIT 1)
    ORDER BY calls DESC LIMIT 10;
    """
    result = None

    try:
        result = db_execute_results(db, q)

    except ProgrammingError:
        result = ('pg_stat_statements is required but it is not enabled:\n'
                  '  https://www.postgresql.org/docs/current/pgstatstatements.html')
        print(result)

    return result
