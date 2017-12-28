#!/usr/bin/env sh

LOG=examples/ocr-duan/inception-bn/pla1-pla2-blue/test-log/test-log-`date +%Y-%m-%d-%H-%M-%S`.log
./build/tools/ocr_test /home/duan/data/plate/pla1-pla2-blue/test/images/ /home/duan/caffe/caffe_ocr_for_linux-v2/examples/ocr-duan/inception-bn/pla1-pla2-blue/modules chi 2>&1   | tee $LOG
