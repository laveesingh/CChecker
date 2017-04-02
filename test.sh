#!/bin/bash
for filename in tests/complex/*.c do
	$python cchecker.py -f tests/complex/$filename.c
done