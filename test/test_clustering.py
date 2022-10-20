"""Tests for the clustering algorithms."""
import scipy.sparse
import pytest
import numpy as np
from context import stag
import stag.graph
import stag.cluster

# Define the adjacency matrices of some useful graphs.
C4_ADJ_MAT = scipy.sparse.csr_matrix([[0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0]])
K6_ADJ_MAT = scipy.sparse.csr_matrix([[0, 1, 1, 1, 1, 1], [1, 0, 1, 1, 1, 1], [1, 1, 0, 1, 1, 1],
                                      [1, 1, 1, 0, 1, 1], [1, 1, 1, 1, 0, 1], [1, 1, 1, 1, 1, 0]])
BARBELL5_ADJ_MAT = scipy.sparse.csr_matrix([[0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
                                            [1, 0, 1, 1, 1, 0, 0, 0, 0, 0],
                                            [1, 1, 0, 1, 1, 0, 0, 0, 0, 0],
                                            [1, 1, 1, 0, 1, 0, 0, 0, 0, 0],
                                            [1, 1, 1, 1, 0, 1, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 1, 0, 1, 1, 1, 1],
                                            [0, 0, 0, 0, 0, 1, 0, 1, 1, 1],
                                            [0, 0, 0, 0, 0, 1, 1, 0, 1, 1],
                                            [0, 0, 0, 0, 0, 1, 1, 1, 0, 1],
                                            [0, 0, 0, 0, 0, 1, 1, 1, 1, 0],
                                            ])


def test_default_local_clustering():
    # Construct a graph object with the barbell adjacency matrix
    graph = stag.graph.Graph(BARBELL5_ADJ_MAT)

    # Find a local cluster near the first vertex
    cluster = stag.cluster.local_cluster(graph, 1, 21)

    # Assert that the correct clusters have been found.
    assert (set(cluster) == {0, 1, 2, 3, 4})


def test_acl_local_clustering():
    # Construct a graph object with a well-defined cluster structure
    graph = stag.random.sbm(1000, 2, 0.01, 0.001)

    # Find a local cluster near the first vertex
    cluster = stag.cluster.local_cluster(graph, 1, int(500 * 500 * 0.011))
    pass


def test_approximate_pagerank():
    # For easier manual verification, we use a cycle graph with 0.5 weights on the edges
    adj = 0.5 * stag.graph.cycle_graph(4).adjacency()
    graph = stag.graph.Graph(adj)

    # Construct seed matrix.
    s = scipy.sparse.csc_matrix((4, 1))
    s[0, 0] = 1

    # Run the personalised pagerank and check that we get the right result
    p, r = stag.cluster.approximate_pagerank(graph, s, 1./3, 1./8)
    expected_p = [41./81, 2./27, 0, 2./27]
    expected_r = [5./81, 2./27 + 5./162, 2./27, 2./27 + 5./162]
    np.testing.assert_almost_equal(p.todense().transpose().tolist()[0], expected_p)
    np.testing.assert_almost_equal(r.todense().transpose().tolist()[0], expected_r)
