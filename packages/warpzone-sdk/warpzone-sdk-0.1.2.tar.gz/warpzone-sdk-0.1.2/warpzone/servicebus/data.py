""" Module w.r.t. data transformation."""
import pandas as pd
import pyarrow as pa

from ..transform.data import arrow_to_b64_parquet, b64_parquet_to_arrow


def msg_to_pandas_dataframe(message_body: bytes) -> pd.DataFrame:
    """This function takes a Azure servicebus message transform it into a
    pandas dataframe.

    Args:
        message (bytes): The body of a Azure Service Bus message in bytes.
    Returns:
        pd.DataFrame: A pandas dataframe with the decoded data.
    """
    return b64_parquet_to_arrow(message_body).to_pandas()


def pandas_dataframe_to_msg(df: pd.DataFrame) -> bytes:
    """This function takes a pandas dataframe transform it into a
    Azure servicebus message.

    Args:
        df (pd.DataFrame): A pandas dataframe
    Returns:
        bytes: The body of a Azure Service Bus message in bytes.
    """
    return arrow_to_b64_parquet(pa.Table.from_pandas(df))
