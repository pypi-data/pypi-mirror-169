# -*- coding: utf-8 -*-

import re
import gzip

import pandas as pd
import numpy as np

from eust.core import _download_file, conf


_DIMENSION_NAME_RE = re.compile(r"^[a-z_0-9]+$")
_YEAR_RE = re.compile(r"^(1|2)[0-9]{3}$")


def _is_valid_dimension_name(s: str) -> bool:
    return bool(_DIMENSION_NAME_RE.match(s))


def _read_tsv(path_or_buffer) -> pd.DataFrame:
    d = pd.read_csv(path_or_buffer, sep="\t", header=0, dtype=str)
    parsed_chunks = list(map(_parse_chunk, _gen_chunks(d)))
    del d # saving some memory here
    return pd.concat(parsed_chunks).sort_index()


CHUNK_SIZE = int(1e6)


def _gen_chunks(data):
    i = 0
    while True:
        chunk = data.iloc[i * CHUNK_SIZE : (i + 1) * CHUNK_SIZE]
        if not len(chunk):
            return
        yield chunk
        i += 1

def _parse_chunk(chunk):
    index_header_str = chunk.columns[0]
    row_dims, col_dims = (s.split(",") for s in index_header_str.split("\\"))

    assert len(row_dims) >= 1, row_dims

    # cannot handle multidimensional column labels
    assert len(col_dims) == 1, col_dims
    (col_dim,) = col_dims

    index_data = chunk[index_header_str]
    chunk.index = pd.MultiIndex.from_tuples(
        (v.split(",") for v in index_data), names=row_dims
    )
    del chunk[index_header_str]

    chunk.columns.name = col_dim

    chunk = chunk.stack()

    assert set(chunk.apply(type)) == {str}
    assert isinstance(chunk, pd.Series), chunk.columns

    assert all(map(_is_valid_dimension_name, chunk.index.names)), chunk.index.names

    chunk = (
        chunk.str.split(" ", expand=True)
        .rename(columns={0: "value", 1: "flag"})
        .replace({":": float("nan"), "": float("nan")})
        .astype({"value": float})
    )

    assert list(chunk.columns) == ["value", "flag"], chunk.columns

    assert isinstance(chunk.index, pd.MultiIndex), chunk.index

    def adapt_index_level_values(name, level_values):
        level_values = [s.strip() for s in level_values]

        if name == "time":
            matches_year = (_YEAR_RE.match(s) for s in level_values)
            if all(matches_year):
                level_values = list(map(int, level_values))

        return level_values

    chunk.index = chunk.index.set_levels(
        [
            adapt_index_level_values(level_name, level_values)
            for level_name, level_values in zip(chunk.index.names, chunk.index.levels)
        ]
    )

    chunk = chunk.sort_index()
    assert chunk.index.is_unique

    return chunk

_TSV_GZ_FILENAME = "data.tsv.gz"
_HDF_FILENAME = "data.h5"
_HDF_TABLE_PATH = "eurostat_table"


def _read_tsv_gz(path_or_buffer) -> pd.DataFrame:
    with gzip.open(path_or_buffer, "rb") as f:
        return _read_tsv(f)


def _download_tsv_gz(url, dst_dir):
    path = dst_dir / _TSV_GZ_FILENAME
    _download_file(url, path)


def _read(the_dir):
    hdf_path = the_dir / _HDF_FILENAME
    tsv_gz_path = the_dir / _TSV_GZ_FILENAME
    try:
        data = pd.read_hdf(hdf_path, _HDF_TABLE_PATH)
    except FileNotFoundError:
        data = _read_tsv_gz(tsv_gz_path)

        data.to_hdf(
            hdf_path,
            _HDF_TABLE_PATH,
            complevel=conf["hdf_complevel"],
            complib=conf["hdf_complib"],
        )

    # Replace empty flags by None (issue #3)
    #
    # Doing it at this point so that the null flag is saved in the HDF
    # file as a string, for performance reasons.
    # This is a pandas PerformanceWarning:
    # "your performance may suffer as PyTables will pickle object types
    # that it cannot map directly to c-types
    # [inferred_type->mixed,key->block0_values] [items->['flag']]"
    data["flag"] = data["flag"].replace({"": None})

    return data
