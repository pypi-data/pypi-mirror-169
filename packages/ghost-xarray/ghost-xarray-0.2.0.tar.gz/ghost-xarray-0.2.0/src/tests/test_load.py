import ghost_xarray
import numpy as np

DTYPE = np.float32
SHAPE = (8, 8)


def test_load_scalar(tmp_path):
    file = tmp_path / "data.out"
    x = np.random.random(SHAPE).astype(DTYPE)
    x.tofile(file)

    y = ghost_xarray.load_scalar(file, coords=SHAPE, dtype=DTYPE)
    assert y.sum() == x.sum()

    y = ghost_xarray.load_scalar(file, coords=SHAPE, dtype=DTYPE, chunks={})
    assert y.sum().compute() == x.sum()
