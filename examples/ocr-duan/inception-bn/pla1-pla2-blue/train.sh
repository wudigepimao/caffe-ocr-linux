#!/usr/bin/env sh
set -e
LOG=examples/ocr-duan/inception-bn/pla1-pla2-blue/log/log-`date +%Y-%m-%d-%H-%M-%S`.log
./build/tools/caffe train --solver=examples/ocr-duan/inception-bn/pla1-pla2-blue/solver.prototxt 2>&1   | tee $LOG $@
