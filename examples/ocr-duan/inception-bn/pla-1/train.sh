#!/usr/bin/env sh
set -e

./build/tools/caffe train --solver=examples/ocr-duan/inception-bn/pla-1/solver.prototxt $@
