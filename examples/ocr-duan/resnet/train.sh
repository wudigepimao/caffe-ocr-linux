#!/usr/bin/env sh
set -e

./build/tools/caffe train --solver=examples/ocr-duan/resnet/solver.prototxt $@
