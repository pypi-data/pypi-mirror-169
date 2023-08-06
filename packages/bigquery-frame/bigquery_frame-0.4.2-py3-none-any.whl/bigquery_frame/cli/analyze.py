import sys
from argparse import ArgumentParser
from typing import List

from bigquery_frame import BigQueryBuilder
from bigquery_frame.transformations import analyze


def main(argv: List[str] = None):
    if argv is None:
        argv = sys.argv[1:]

    parser = ArgumentParser(description="", prog="bq-analyze")
    parser.add_argument("table", nargs="*")
    args = parser.parse_args(argv)
    bq = BigQueryBuilder()
    df = bq.sql(args.table)
    analyze(df).show()
