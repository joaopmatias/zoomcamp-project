#!/bin/bash

source /root/.sdkman/bin/sdkman-init.sh 

/root/.sdkman/candidates/spark/3.3.2/sbin/start-master.sh  --host 0.0.0.0

/root/.sdkman/candidates/spark/3.3.2/sbin/start-worker.sh spark://0.0.0.0:7077

exec tail -f /dev/null