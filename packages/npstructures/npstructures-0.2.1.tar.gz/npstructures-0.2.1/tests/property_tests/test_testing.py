from hypothesis import given
import hypothesis.strategies as st
from npstructures import RaggedArray
import hypothesis.extra.numpy as hnp
import numpy as np


shape = hnp.array_shapes(min_dims=2, max_dims=2, max_side=1000)
shape_1 = st.shared(shape, key="test")
shape_2 = st.shared(shape, key="test")


@given(hnp.arrays(float, shape_1),
       hnp.arrays(float, shape_2))
def test_add(a, b):
    ra = RaggedArray.from_numpy_array(a)
    rb = RaggedArray.from_numpy_array(b)
    np.testing.assert_equal(
        a+b, (ra+rb).to_numpy_array())
