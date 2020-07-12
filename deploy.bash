#!/bin/bash

tar --exclude='./sekolahbackend.tar' --exclude='./vscode' --exclude='.git' -zcvf sekolahbackend.tar . 
scp ./sekolahbackend.tar hmft@35.208.24.99:~/Downloads/sekolahbackend.tar