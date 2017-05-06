#!/bin/bash

# file name gets passed without extension
javac $1.java
echo Main-Class: $1 > manifest.txt
jar cvmf manifest.txt $1.jar *.class

