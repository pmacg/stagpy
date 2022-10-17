# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _stag_internal
else:
    import _stag_internal

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


import weakref

class SwigPyIterator(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _stag_internal.delete_SwigPyIterator

    def value(self):
        return _stag_internal.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _stag_internal.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _stag_internal.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _stag_internal.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _stag_internal.SwigPyIterator_equal(self, x)

    def copy(self):
        return _stag_internal.SwigPyIterator_copy(self)

    def next(self):
        return _stag_internal.SwigPyIterator_next(self)

    def __next__(self):
        return _stag_internal.SwigPyIterator___next__(self)

    def previous(self):
        return _stag_internal.SwigPyIterator_previous(self)

    def advance(self, n):
        return _stag_internal.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _stag_internal.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _stag_internal.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _stag_internal.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _stag_internal.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _stag_internal.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _stag_internal.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self

# Register SwigPyIterator in _stag_internal:
_stag_internal.SwigPyIterator_swigregister(SwigPyIterator)

class vectori(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _stag_internal.vectori_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _stag_internal.vectori___nonzero__(self)

    def __bool__(self):
        return _stag_internal.vectori___bool__(self)

    def __len__(self):
        return _stag_internal.vectori___len__(self)

    def __getslice__(self, i, j):
        return _stag_internal.vectori___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _stag_internal.vectori___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _stag_internal.vectori___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _stag_internal.vectori___delitem__(self, *args)

    def __getitem__(self, *args):
        return _stag_internal.vectori___getitem__(self, *args)

    def __setitem__(self, *args):
        return _stag_internal.vectori___setitem__(self, *args)

    def pop(self):
        return _stag_internal.vectori_pop(self)

    def append(self, x):
        return _stag_internal.vectori_append(self, x)

    def empty(self):
        return _stag_internal.vectori_empty(self)

    def size(self):
        return _stag_internal.vectori_size(self)

    def swap(self, v):
        return _stag_internal.vectori_swap(self, v)

    def begin(self):
        return _stag_internal.vectori_begin(self)

    def end(self):
        return _stag_internal.vectori_end(self)

    def rbegin(self):
        return _stag_internal.vectori_rbegin(self)

    def rend(self):
        return _stag_internal.vectori_rend(self)

    def clear(self):
        return _stag_internal.vectori_clear(self)

    def get_allocator(self):
        return _stag_internal.vectori_get_allocator(self)

    def pop_back(self):
        return _stag_internal.vectori_pop_back(self)

    def erase(self, *args):
        return _stag_internal.vectori_erase(self, *args)

    def __init__(self, *args):
        _stag_internal.vectori_swiginit(self, _stag_internal.new_vectori(*args))

    def push_back(self, x):
        return _stag_internal.vectori_push_back(self, x)

    def front(self):
        return _stag_internal.vectori_front(self)

    def back(self):
        return _stag_internal.vectori_back(self)

    def assign(self, n, x):
        return _stag_internal.vectori_assign(self, n, x)

    def resize(self, *args):
        return _stag_internal.vectori_resize(self, *args)

    def insert(self, *args):
        return _stag_internal.vectori_insert(self, *args)

    def reserve(self, n):
        return _stag_internal.vectori_reserve(self, n)

    def capacity(self):
        return _stag_internal.vectori_capacity(self)
    __swig_destroy__ = _stag_internal.delete_vectori

# Register vectori in _stag_internal:
_stag_internal.vectori_swigregister(vectori)

class vectord(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _stag_internal.vectord_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _stag_internal.vectord___nonzero__(self)

    def __bool__(self):
        return _stag_internal.vectord___bool__(self)

    def __len__(self):
        return _stag_internal.vectord___len__(self)

    def __getslice__(self, i, j):
        return _stag_internal.vectord___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _stag_internal.vectord___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _stag_internal.vectord___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _stag_internal.vectord___delitem__(self, *args)

    def __getitem__(self, *args):
        return _stag_internal.vectord___getitem__(self, *args)

    def __setitem__(self, *args):
        return _stag_internal.vectord___setitem__(self, *args)

    def pop(self):
        return _stag_internal.vectord_pop(self)

    def append(self, x):
        return _stag_internal.vectord_append(self, x)

    def empty(self):
        return _stag_internal.vectord_empty(self)

    def size(self):
        return _stag_internal.vectord_size(self)

    def swap(self, v):
        return _stag_internal.vectord_swap(self, v)

    def begin(self):
        return _stag_internal.vectord_begin(self)

    def end(self):
        return _stag_internal.vectord_end(self)

    def rbegin(self):
        return _stag_internal.vectord_rbegin(self)

    def rend(self):
        return _stag_internal.vectord_rend(self)

    def clear(self):
        return _stag_internal.vectord_clear(self)

    def get_allocator(self):
        return _stag_internal.vectord_get_allocator(self)

    def pop_back(self):
        return _stag_internal.vectord_pop_back(self)

    def erase(self, *args):
        return _stag_internal.vectord_erase(self, *args)

    def __init__(self, *args):
        _stag_internal.vectord_swiginit(self, _stag_internal.new_vectord(*args))

    def push_back(self, x):
        return _stag_internal.vectord_push_back(self, x)

    def front(self):
        return _stag_internal.vectord_front(self)

    def back(self):
        return _stag_internal.vectord_back(self)

    def assign(self, n, x):
        return _stag_internal.vectord_assign(self, n, x)

    def resize(self, *args):
        return _stag_internal.vectord_resize(self, *args)

    def insert(self, *args):
        return _stag_internal.vectord_insert(self, *args)

    def reserve(self, n):
        return _stag_internal.vectord_reserve(self, n)

    def capacity(self):
        return _stag_internal.vectord_capacity(self)
    __swig_destroy__ = _stag_internal.delete_vectord

# Register vectord in _stag_internal:
_stag_internal.vectord_swigregister(vectord)

class edge(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    v1 = property(_stag_internal.edge_v1_get, _stag_internal.edge_v1_set)
    v2 = property(_stag_internal.edge_v2_get, _stag_internal.edge_v2_set)
    weight = property(_stag_internal.edge_weight_get, _stag_internal.edge_weight_set)

    def __init__(self):
        _stag_internal.edge_swiginit(self, _stag_internal.new_edge())
    __swig_destroy__ = _stag_internal.delete_edge

# Register edge in _stag_internal:
_stag_internal.edge_swigregister(edge)
cvar = _stag_internal.cvar
VERSION_MAJOR = cvar.VERSION_MAJOR
VERSION_MINOR = cvar.VERSION_MINOR
VERSION_PATCH = cvar.VERSION_PATCH

class LocalGraph(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def degree(self, v):
        return _stag_internal.LocalGraph_degree(self, v)

    def degree_unweighted(self, v):
        return _stag_internal.LocalGraph_degree_unweighted(self, v)

    def neighbors(self, v):
        return _stag_internal.LocalGraph_neighbors(self, v)

    def neighbors_unweighted(self, v):
        return _stag_internal.LocalGraph_neighbors_unweighted(self, v)
    __swig_destroy__ = _stag_internal.delete_LocalGraph

# Register LocalGraph in _stag_internal:
_stag_internal.LocalGraph_swigregister(LocalGraph)

class Graph(LocalGraph):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _stag_internal.Graph_swiginit(self, _stag_internal.new_Graph(*args))

    def adjacency(self):
        return _stag_internal.Graph_adjacency(self)

    def laplacian(self):
        return _stag_internal.Graph_laplacian(self)

    def normalised_laplacian(self):
        return _stag_internal.Graph_normalised_laplacian(self)

    def degree_matrix(self):
        return _stag_internal.Graph_degree_matrix(self)

    def inverse_degree_matrix(self):
        return _stag_internal.Graph_inverse_degree_matrix(self)

    def lazy_random_walk_matrix(self):
        return _stag_internal.Graph_lazy_random_walk_matrix(self)

    def total_volume(self):
        return _stag_internal.Graph_total_volume(self)

    def number_of_vertices(self):
        return _stag_internal.Graph_number_of_vertices(self)

    def number_of_edges(self):
        return _stag_internal.Graph_number_of_edges(self)

    def degree(self, v):
        return _stag_internal.Graph_degree(self, v)

    def degree_unweighted(self, v):
        return _stag_internal.Graph_degree_unweighted(self, v)

    def neighbors(self, v):
        return _stag_internal.Graph_neighbors(self, v)

    def neighbors_unweighted(self, v):
        return _stag_internal.Graph_neighbors_unweighted(self, v)
    __swig_destroy__ = _stag_internal.delete_Graph

# Register Graph in _stag_internal:
_stag_internal.Graph_swigregister(Graph)


def __eq__(*args):
    return _stag_internal.__eq__(*args)

def __ne__(*args):
    return _stag_internal.__ne__(*args)

def cycle_graph(n):
    return _stag_internal.cycle_graph(n)

def complete_graph(n):
    return _stag_internal.complete_graph(n)

def barbell_graph(n):
    return _stag_internal.barbell_graph(n)

def sprsMatValues(matrix):
    return _stag_internal.sprsMatValues(matrix)

def sprsMatInnerIndices(matrix):
    return _stag_internal.sprsMatInnerIndices(matrix)

def sprsMatOuterStarts(matrix):
    return _stag_internal.sprsMatOuterStarts(matrix)

def sprsMatToVec(*args):
    return _stag_internal.sprsMatToVec(*args)

def isSymmetric(matrix):
    return _stag_internal.isSymmetric(matrix)

def local_cluster(graph, seed_vertex, target_volume):
    return _stag_internal.local_cluster(graph, seed_vertex, target_volume)

def local_cluster_acl(*args):
    return _stag_internal.local_cluster_acl(*args)

def approximate_pagerank(graph, seed_vector, alpha, epsilon):
    return _stag_internal.approximate_pagerank(graph, seed_vector, alpha, epsilon)

def sweep_set_conductance(graph, vec):
    return _stag_internal.sweep_set_conductance(graph, vec)

def load_edgelist(filename):
    return _stag_internal.load_edgelist(filename)

def save_edgelist(graph, filename):
    return _stag_internal.save_edgelist(graph, filename)

def sbm(*args):
    return _stag_internal.sbm(*args)

def erdos_renyi(*args):
    return _stag_internal.erdos_renyi(*args)
VERSION = _stag_internal.VERSION


