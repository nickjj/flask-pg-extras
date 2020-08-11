import click

from flask import current_app
from flask.cli import with_appcontext

from flask_pg_extras.queries.extensions import query as query_extensions
from flask_pg_extras.queries.index_size import query as query_index_size
from flask_pg_extras.queries.index_unused import query as query_index_unused
from flask_pg_extras.queries.queries_active_locks import query as query_queries_active_locks
from flask_pg_extras.queries.queries_blocking import query as query_queries_blocking
from flask_pg_extras.queries.queries_long_running import query as query_queries_long_running
from flask_pg_extras.queries.queries_outliers import query as query_queries_outliers
from flask_pg_extras.queries.queries_popular import query as query_queries_popular
from flask_pg_extras.queries.table_bloat import query as query_table_bloat
from flask_pg_extras.queries.table_cache_hit import query as query_table_cache_hit
from flask_pg_extras.queries.table_est_row_count import query as query_est_row_count
from flask_pg_extras.queries.table_index_size import query as query_table_index_size
from flask_pg_extras.queries.table_index_usage import query as query_table_index_usage
from flask_pg_extras.queries.table_seq_scans import query as query_table_seq_scans
from flask_pg_extras.queries.table_size import query as query_table_size
from flask_pg_extras.queries.total_cache_hit import query as query_total_cache_hit
from flask_pg_extras.queries.total_index_size import query as query_total_index_size
from flask_pg_extras.queries.total_table_size import query as query_total_table_size
from flask_pg_extras.queries.vacuum_stats import query as query_vacuum_stats


@click.group()
def pg_extras():
    """Obtain useful information from your PostgreSQL database."""
    pass


@pg_extras.command()
@with_appcontext
def extensions():
    """Installed and available extensions."""
    query_extensions(current_app.extensions['sqlalchemy'].db)


@pg_extras.command()
@with_appcontext
def index_size():
    """Size of individual indexes."""
    query_index_size(current_app.extensions['sqlalchemy'].db)


@pg_extras.command()
@with_appcontext
def index_unused():
    """Unused and almost unused indexes."""
    query_index_unused(current_app.extensions['sqlalchemy'].db)


@pg_extras.command()
@with_appcontext
def queries_active_locks():
    """Queries with active locks."""
    query_queries_active_locks(current_app.extensions['sqlalchemy'].db)


@pg_extras.command()
@with_appcontext
def queries_blocking():
    """Queries holding locks that are waiting."""
    query_queries_blocking(current_app.extensions['sqlalchemy'].db)


@pg_extras.command()
@with_appcontext
def queries_long_running():
    """Queries actively running for longer than 5 minutes."""
    query_queries_long_running(current_app.extensions['sqlalchemy'].db)


@pg_extras.command()
@with_appcontext
def queries_outliers():
    """10 longest executing queries."""
    query_queries_outliers(current_app.extensions['sqlalchemy'].db)


@pg_extras.command()
@with_appcontext
def queries_popular():
    """10 most called queries."""
    query_queries_popular(current_app.extensions['sqlalchemy'].db)


@pg_extras.command()
@with_appcontext
def table_bloat():
    """Table bloat (beware of 10+ bloat ratios)."""
    query_table_bloat(current_app.extensions['sqlalchemy'].db)


@pg_extras.command()
@with_appcontext
def table_cache_hit():
    """Table cache hit rate (aim for 99%+)."""
    query_table_cache_hit(current_app.extensions['sqlalchemy'].db)


@pg_extras.command()
@with_appcontext
def table_est_row_count():
    """Estimated count of rows for each table (n_live_tup)."""
    query_est_row_count(current_app.extensions['sqlalchemy'].db)


@pg_extras.command()
@with_appcontext
def table_index_size():
    """Total size of all the indexes for each table."""
    query_table_index_size(current_app.extensions['sqlalchemy'].db)


@pg_extras.command()
@with_appcontext
def table_index_usage():
    """Index hit rate for each table."""
    query_table_index_usage(current_app.extensions['sqlalchemy'].db)


@pg_extras.command()
@with_appcontext
def table_seq_scans():
    """Total sequential scans for each table."""
    query_table_seq_scans(current_app.extensions['sqlalchemy'].db)


@pg_extras.command()
@with_appcontext
def table_size():
    """Total size of the tables (excluding indexes)."""
    query_table_size(current_app.extensions['sqlalchemy'].db)


@pg_extras.command()
@with_appcontext
def total_cache_hit():
    """Total index and table hit rate."""
    query_total_cache_hit(current_app.extensions['sqlalchemy'].db)


@pg_extras.command()
@with_appcontext
def total_index_size():
    """Total size of all indexes for every table."""
    query_total_index_size(current_app.extensions['sqlalchemy'].db)


@pg_extras.command()
@with_appcontext
def total_table_size():
    """Total size of the tables (including indexes)."""
    query_total_table_size(current_app.extensions['sqlalchemy'].db)


@pg_extras.command()
@with_appcontext
def vacuum_stats():
    """Show dead rows and expected vacuum triggers."""
    query_vacuum_stats(current_app.extensions['sqlalchemy'].db)
