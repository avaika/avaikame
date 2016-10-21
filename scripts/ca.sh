#!/bin/bash

error() {
    echo "$@"
    exit 1
}

[ "$1" == "-l" ] && work_local="true" && shift
database="${1:-blog}"
db_file="avaika.sql"

download() {
  ssh avaika "set -x ; mysqldump avaika > $db_file && gzip $db_file" || error "Failed to ssh"
  rsync -e ssh  --progress -Pa --inplace --no-whole-file avaika:${db_file}.gz .  || error "Failed to copy"
  ssh avaika "rm ${db_file}*" || error "Failed to ssh"
  gunzip "${db_file}.gz" || error "Failed to unarchive"
}

import() {
  mysql "$database" -N -e 'show tables;' | while read table; do 
      mysql "$database" -e "SET FOREIGN_KEY_CHECKS = 0; drop table $table;"; 
  done 
  mysql "$database" < "$db_file" || error "Failed to import"
}

[ -n "$work_local" ] || download
[ -f "$db_file" ] || error "No dump found // $db_file"
import
[ -n "$work_local" ] || rm -i "$db_file"
echo -n
