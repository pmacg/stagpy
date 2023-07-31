"""
Some objects used for interoperability between C++ and Python.
"""
from . import stag_internal
import scipy.sparse
import inspect
import numpy as np
from typing import Union, List, Tuple

class SprsMat(object):
    """
    An object representing a sparse matrix for use by the STAG library.
    The data is stored natively on the 'C++' side of the library, allowing
    for fast computation.

    The object is designed for easy interoperability with scipy sparse matrix
    objects. The SprsMat object can be constructed directly from a scipy
    sparse matrix, and the to_scipy() method can be used to convert back
    to a scipy matrix.

    If they are only used as arguments to STAG library methods, they will be very
    efficient since the data will stay on the C++ side of the library.
    """

    def __init__(self, matrix: Union[scipy.sparse.spmatrix, List[List[float]]]):
        r"""
        Construct a STAG SprsMat.

        Pass either a scipy sparse matrix object or a List of Lists representing
        the dense matrix to be stored in sparse format.

        For example:

        \code{python}
        >>> import stag.utility
        >>> import stag.graph
        >>>
        >>> adj_mat = stag.utility.SprsMat([[0, 1, 1, 1],
        ...                                 [1, 0, 1, 1],
        ...                                 [1, 1, 0, 1],
        ...                                 [1, 1, 1, 0]])
        >>> g = stag.graph.Graph(adj_mat)
        \endcode
        """
        ##
        # \cond
        # Do not document the internal workings of the SprsMat object
        ##
        self.scipy_mat = None

        if issubclass(type(matrix), scipy.sparse.spmatrix):
            self.scipy_mat = matrix.tocsc()
        if isinstance(matrix, List):
            self.scipy_mat = scipy.sparse.csc_matrix(matrix)

        if isinstance(matrix, stag_internal.SprsMat):
            self.internal_sprsmat = matrix
        else:
            assert self.scipy_mat is not None
            col_starts = self.scipy_mat.indptr
            row_indices = self.scipy_mat.indices
            values = self.scipy_mat.data
            self.internal_sprsmat = stag_internal.sprsMatFromVectorsDims(
                self.scipy_mat.shape[0], self.scipy_mat.shape[1],
                col_starts, row_indices, values)
        ##
        # \endcond
        ##

    def to_scipy(self) -> scipy.sparse.csc_matrix:
        """
        Convert the STAG SprsMat object to a scipy sparse matrix.
        """
        if self.scipy_mat is None:
            outer_starts = stag_internal.sprsMatOuterStarts(self.internal_sprsmat)
            inner_indices = stag_internal.sprsMatInnerIndices(self.internal_sprsmat)
            values = stag_internal.sprsMatValues(self.internal_sprsmat)
            self.scipy_mat = scipy.sparse.csc_matrix(
                (values, inner_indices, outer_starts),
                shape=self.shape())
        return self.scipy_mat

    def to_dense(self) -> np.ndarray:
        """
        Convert the STAG SprsMat object to a dense numpy matrix.
        """
        return self.to_scipy().toarray()

    def transpose(self) -> 'stag.utility.SprsMat':
        """
        Return the transpose of the matrix.
        """
        return SprsMat(self.internal_sprsmat.__transpose__())

    def shape(self) -> Tuple[int, int]:
        """
        Return the shape of the matrix.
        """
        return self.internal_sprsmat.get_rows(), self.internal_sprsmat.get_cols()

    ##
    # \cond
    # Do not document the operator methods
    ##
    def __sub__(self, other):
        if isinstance(other, SprsMat):
            if self.shape() != other.shape():
                raise ValueError("Matrix dimensions must match.")
            return SprsMat(self.internal_sprsmat - other.internal_sprsmat)
        else:
            return NotImplemented

    def __rsub__(self, other):
        if isinstance(other, SprsMat):
            if self.shape() != other.shape():
                raise ValueError("Matrix dimensions must match.")
            return SprsMat(other.internal_sprsmat - self.internal_sprsmat)
        else:
            return NotImplemented

    def __neg__(self):
        return SprsMat(-self.internal_sprsmat)

    def __add__(self, other):
        if isinstance(other, SprsMat):
            if self.shape() != other.shape():
                raise ValueError("Matrix dimensions must match.")
            return SprsMat(self.internal_sprsmat + other.internal_sprsmat)
        else:
            return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        if isinstance(other, int):
            return SprsMat(self.internal_sprsmat.__mulint__(other))
        elif isinstance(other, float):
            return SprsMat(self.internal_sprsmat.__mulfloat__(other))
        elif isinstance(other, SprsMat):
            return SprsMat(self.internal_sprsmat * other.internal_sprsmat)
        else:
            return NotImplemented

    def __rmul__(self, other):
        if isinstance(other, SprsMat):
            return SprsMat(other.internal_sprsmat * self.internal_sprsmat)
        else:
            return self.__mul__(other)

    def __matmul__(self, other):
        return self.__mul__(other)

    def __rmatmul__(self, other):
        return self.__rmul__(other)

    def __truediv__(self, other):
        if isinstance(other, int):
            return SprsMat(self.internal_sprsmat.__truedivint__(other))
        elif isinstance(other, float):
            return SprsMat(self.internal_sprsmat.__truedivfloat__(other))
        else:
            return NotImplemented

    ##
    # \endcond
    ##
