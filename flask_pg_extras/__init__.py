from sqlalchemy import text
from tabulate import tabulate


class FlaskPGExtras(object):
    def __init__(self, app=None):
        self.app = app

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """
        Mutate the application passed in as explained here:
          https://flask.palletsprojects.com/en/1.1.x/extensiondev/

        :param app: Flask application
        :return: None
        """
        pass


def db_execute_results(db, q):
    """
    Output the database query results in tabular format.

    :param db: SQLAlchemy db object
    :param q: SQL query as string
    :return: SQLAlchemy execute result
    """
    result = db.engine.execute(text(q))

    result_fetchall = result.fetchall()

    print(tabulate([list(r) for r in result_fetchall],
                   headers=result.keys(), tablefmt="psql"))

    return result
