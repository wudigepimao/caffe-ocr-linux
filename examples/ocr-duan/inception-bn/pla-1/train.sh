#!/usr/bin/env sh
set -e
LOG=examples/ocr-duan/inception-bn/pla-1/log/log-`date +%Y-%m-%d-%H-%M-%S`.log
./build/tools/caffe train --solver=examples/ocr-duan/inception-bn/pla-1/solver.prototxt 2>&1   | tee $LOG $@
