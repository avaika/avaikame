#!/bin/bash

error() {
    echo "$@"
    exit 1
}

download() {
  ssh avaika 'set -x ; mysqldump avaika > avaika.sql && gzip avaika.sql' || error "Failed to ssh"
  rsync -e ssh  --progress -Pa --inplace --no-whole-file avaika:avaika.sql.gz .  || error "Failed to copy"
  ssh avaika 'rm avaika.sql*' || error "Failed to ssh"
  gunzip avaika.sql.gz || error "Failed to unarchive"
}

import() {
  mysql blog < avaika.sql || error "Failed to import"
}

[ "$1" == "-l" ] || download
import
[ "$1" == "-l" ] || rm -i avaika.sql
echo -n
