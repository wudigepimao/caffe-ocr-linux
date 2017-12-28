#!/usr/bin/env sh
set -e

./build/tools/caffe train --solver=examples/ocr-duan/inception-bn/solver.prototxt $@
