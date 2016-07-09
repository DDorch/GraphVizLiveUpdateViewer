# GraphVizLiveUpdateViewer

A PyQT script for automatically generating and displaying a graph produced with GraphViz dot tool.

This script displays the result of a GraphViz graph with live update capability: each time you save your GraphViz file, this one will be automatically update. So you can see in real time, the effect of your modification on your GraphViz file.

![Window capture](https://github.com/DDorch/GraphVizLiveUpdateViewer/blob/master/WindowCapture.png)

# User documentation

## Requirement

An OS with Python3, PyQT5, and GraphViz installed.

## Installation

Copy dot.py and dot.ini to your disk.

## Configuration

Before using the tool, one needs to configure `dotd.ini` in order to define:
* The Path to the GraphViz DOT program (Section `[DOT]`, parameter `EXE`)
* The format of the image that will be produced by DOT defined by image file extension format (`png` by default, other formats were not tested) (Section `[DOT]`, parameter `FORMAT`)
* The refresh time for updating the view in milliseconds (Section `[DAEMON]`, parameter `SLEEP`)

## How to run the script

Type this command line: `dotd.py [Name of the GraphViz file]`

You can test the script with the example provided in this repository `dotd.py test_cluster.gv` and you will get the example window above.

On some Windows configuration, the python file association doesn't pass the command line arguments to the python interpreter. If you meet this issue, refer to http://stackoverflow.com/questions/2640971/windows-is-not-passing-command-line-arguments-to-python-programs-executed-from-t 
