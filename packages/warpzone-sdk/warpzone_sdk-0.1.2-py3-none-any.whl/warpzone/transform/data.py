import base64 as b64

import pyarrow as pa
import pyarrow.parquet as pq


def parquet_to_arrow(parquet: bytes) -> pa.Table:
    """Convert parquet as bytes to pyarrow table"""
    return pq.read_table(pa.py_buffer(parquet))


def b64_parquet_to_arrow(content: bytes) -> pa.Table:
    return parquet_to_arrow(b64.b64decode(content))


def arrow_to_parquet(table: pa.Table) -> bytes:
    """Convert pyarrow table to parquet as bytes"""
    buf = pa.BufferOutputStream()
    pq.write_table(table, buf)
    return buf.getvalue().to_pybytes()


def arrow_to_b64_parquet(table: pa.Table) -> bytes:
    return b64.b64encode(arrow_to_parquet(table))
