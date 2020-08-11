from flask_pg_extras import db_execute_results


def query(db):
    q = """
    SELECT relname,
      CASE idx_scan
        WHEN 0 THEN 'Insufficient data'
        ELSE (100 * idx_scan / (seq_scan + idx_scan))::text
      END percent_of_times_index_used,
      n_live_tup rows_in_table
     FROM
       pg_stat_user_tables
     ORDER BY
       n_live_tup DESC;
    """

    return db_execute_results(db, q)
