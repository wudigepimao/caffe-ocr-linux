#!/usr/bin/env sh

LOG=examples/ocr-duan/inception-bn/pla2/test-log/test-log-`date +%Y-%m-%d-%H-%M-%S`.log
./build/tools/ocr_test /home/duan/data/plate/pla2/test/images/ /home/duan/caffe/caffe_ocr_for_linux-v2/examples/ocr-duan/inception-bn/pla2/modules chi 2>&1   | tee $LOG
