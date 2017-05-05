#!/bin/bash

javac $1
jar cvmf manifest.txt *.class

