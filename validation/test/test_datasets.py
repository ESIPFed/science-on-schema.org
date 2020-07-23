"""
pytest for running SHACL rules against test data graphs

Run with::

  $ pytest

or

  $ pytest -s

for verbose output.
"""
import warnings
import pytest
import rdflib
import os

# Note this test suite requires a modified version of pySHACL that injects
# additional metrics gathered during the validation process.
# https://github.com/datadavev/pySHACL
import pyshacl
import pyshacl.consts

# Expects directory structure like:
# validation
#   +- shapegraphs
#   +- test
#      +- test_datasets.py
#      +- resources
#         +- *.jsonld   test data graphs
ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Validation report
SH_ValidationReport = pyshacl.consts.SH_ValidationReport
SH_result = pyshacl.consts.SH_result
SH_value = pyshacl.consts.SH_value
SH_focusNode = pyshacl.consts.SH_focusNode
SH_resultPath = pyshacl.consts.SH_resultPath
SH_sourceShape = pyshacl.consts.SH_sourceShape
# failureCount property
SH_failureCount = pyshacl.consts.SH.term("failureCount")
# If zero, then no SHACL targets were found in the data graph
SH_shapesApplied = pyshacl.consts.SH.term("shapesApplied")

SO = rdflib.namespace.Namespace("http://schema.org/")
SOSOT = rdflib.namespace.Namespace("https://science-on-schema.org/test/resources/")

# The structure of the shape graph is such that it describes the class hierarchy
# needed for some of the tests
ONTOLOGY = "shapegraphs/soso_common_v1.2.0.ttl"

# Each test case is a tuple of SHACL graph, Data graph, and expected results
# Expected results is a dict of
#   focusNode : the node of the data graph where the expected failure occurred
#   resultPV : either the resultPath or the resultValue that caused the expected failure
TESTCASES = [
    (
        "shapegraphs/soso_common_v1.2.0.ttl",
        "test/resources/dataset_min.jsonld",
        {"failures": []},
    ),
    (
        "shapegraphs/soso_common_v1.2.0.ttl",
        "test/resources/dataset_ns.jsonld",
        {
            "failures": [
                {
                    "focusNode": SOSOT.term("dataset_ns.jsonld#ds-ns-01"),
                    "resultPV": SOSOT.term("dataset_ns.jsonld#ds-ns-01"),
                },
                {
                    "focusNode": SOSOT.term("dataset_ns.jsonld#ds-ns-02"),
                    "resultPV": SOSOT.term("dataset_ns.jsonld#ds-ns-02"),
                },
                {
                    "focusNode": SOSOT.term("dataset_ns.jsonld#ds-ns-03"),
                    "resultPV": SOSOT.term("dataset_ns.jsonld#ds-ns-03"),
                },
            ]
        },
    ),
    (
        "shapegraphs/soso_common_v1.2.0.ttl",
        "test/resources/dataset_core.jsonld",
        {
            "failures": [
                {"focusNode": SOSOT.term("dataset_core.jsonld#ds-core-01"), "resultPV": SO.term("version")},
                {"focusNode": SOSOT.term("dataset_core.jsonld#ds-core-02"), "resultPV": SO.term("name")},
                {
                    "focusNode": SOSOT.term("dataset_core.jsonld#ds-core-03"),
                    "resultPV": SO.term("description"),
                },
                {"focusNode": SOSOT.term("dataset_core.jsonld#ds-core-04"), "resultPV": SO.term("keywords")},
                {
                    "focusNode": SOSOT.term("dataset_core.jsonld#ds-core-05"),
                    "resultPV": SO.term("isAccessibleForFree"),
                },
                {"focusNode": SOSOT.term("dataset_core.jsonld#ds-core-06"), "resultPV": SO.term("url")},
                {"focusNode": SOSOT.term("dataset_core.jsonld#ds-core-07"), "resultPV": SO.term("sameAs")},
                {"focusNode": SOSOT.term("dataset_core.jsonld#ds-core-08"), "resultPV": SO.term("identifier")},
                {"focusNode": SOSOT.term("dataset_core.jsonld#ds-core-09"), "resultPV": SO.term("identifier")},
            ]
        },
    ),
]

# ===========
# Utility

# Mapping file name extension to rdflib parser
FORMAT_MAP = {
    ".ttl": "turtle",
    ".json": "json-ld",
    ".jsonld": "json-ld",
    ".json-ld": "json-ld",
    ".js": "json-ld",
    ".html": "rdfa",
    ".n3": "n3",
    ".nq": "nquads",
}


def _guessGraphFormat(filename):
    root, ext = os.path.splitext(filename)
    ext = ext.lower()
    return FORMAT_MAP.get(ext, None)


def _abspath(path):
    return os.path.join(ROOT_PATH, path)


def _loadGraph(fname):
    # Turn off deprecation warning from HTML5 lib, this is only an issue on Python3.7 and earlier
    # https://github.com/html5lib/html5lib-python/issues/402
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    g = rdflib.ConjunctiveGraph()
    format = _guessGraphFormat(fname)
    fname = _abspath((fname))
    g.load(fname, format=format)
    # Turn warnings back on
    warnings.filterwarnings("default")
    return g


# ===========
# Tests


# pytest will run this test with each of the tuples in TESTCASES
@pytest.mark.parametrize("shacl_source, data_source, expected", TESTCASES)
def test_shacl(shacl_source, data_source, expected):
    sg = _loadGraph(shacl_source)
    dg = _loadGraph(data_source)
    og = _loadGraph(ONTOLOGY)
    conforms, result_graph, result_text = pyshacl.validate(
        dg,
        shacl_graph=sg,
        ont_graph=og,
        meta_shacl=False,
        advanced=True,
        inference="rdfs",
    )
    print(result_graph.serialize(format="turtle").decode())
    shapes_applied = next(result_graph.objects(None, SH_shapesApplied))
    # A SHACL test should be applied in all cases
    assert shapes_applied.value > 0
    failure_count = next(result_graph.objects(None, SH_failureCount))
    expected_failures = expected.get("failures", [])
    assert failure_count.value == len(expected_failures)
    for result in result_graph.objects(None, SH_result):
        is_expected = False
        # get the sourceShape
        ss = next(result_graph.objects(result, SH_sourceShape))
        # get the focusNode
        fn = next(result_graph.objects(result, SH_focusNode))
        # get the resultPath or on failure, the resultValue
        try:
            tr = next(result_graph.objects(result, SH_resultPath))
        except StopIteration:
            tr = next(result_graph.objects(result, SH_value))
        for failure in expected_failures:
            if failure["resultPV"] == tr and failure["focusNode"] == fn:
                is_expected = True
                break
        if not is_expected:
            raise (
                Exception(
                    f"Unexpected failure for path: {tr}\n  source shape: {ss}\n  focusNode {fn}"
                )
            )


if __name__ == "__main__":
    print('Run with "pytest" or "pytest -s" for verbose output.')
