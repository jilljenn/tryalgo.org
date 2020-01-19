#!/usr/bin/env bash
for f in en/images/*.pdf; do pdf2svg $f en/images/`basename $f .pdf`.svg; done
