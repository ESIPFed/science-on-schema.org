# Shape Graphs

## About

Some details on the shape graphs in this directory

Filename | Description
------------ | -------------
googleRequired.ttl | Checks for the Google required items described in https://developers.google.com/search/docs/data-types/dataset
googleRecommended.ttl | Checks for the Google recommended items described in https://developers.google.com/search/docs/data-types/dataset
googleRecommendedCoverageCheck.ttl | Same as the test for Google recommended but sets all items to min 1 to check for coverage.  Use the one above if you don't care about coverage of recommended items
P418Required.ttl | Same as googleRequired but adds in a check for an @id for Dataset type. Otherwise, checks for the Google recommended items described in https://developers.google.com/search/docs/data-types/dataset
importTest.ttl | TESTING: A testing file for checking if shape imports works to allow people to stack together a set of shape graphs to check with
temporalRange.ttl | TESTING: A file to explore validate temporal items in a data graph 
testingDataGraphs | A directory with various data graphs (some with errors) to use as part of testing shape graphs and perhaps a CI path in the future