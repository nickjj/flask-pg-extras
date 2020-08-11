from flask_pg_extras import db_execute_results


def query(db):
    q = """
    SELECT * FROM pg_available_extensions ORDER BY installed_version;
    """

    return db_execute_results(db, q)
