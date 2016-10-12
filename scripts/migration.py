#!/usr/bin/python
# -*- coding: utf-8 -*-

# import pdb
# pdb.set_trace()
import MySQLdb as mdb
import sys
# import re
import os
# from datetime import datetime, time
import datetime
import codecs
reload(sys)
sys.setdefaultencoding('utf-8')
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)

for tfile in 'db.sql' 'files.sh':
    if os.path.isfile(tfile):
        os.remove(tfile)

# Connect to database
try:
    con = mdb.connect('localhost', 'root', '', 'blog', charset="utf8", use_unicode=True)
    cur = con.cursor(mdb.cursors.DictCursor)
    tcur = con.cursor(mdb.cursors.DictCursor)
except mdb.Error, e:
    print "Connection failed"
    sys.exit(1)

cur.execute(u"select id, UNIX_TIMESTAMP(created) as created, post from me_post where category_id = 1;")
f = open('files.sh', 'w')
d = open('db.sql', 'w')

for x in xrange(0, cur.rowcount):
    row = cur.fetchone()
    post_id = row['id']
    post = row['post']
    res = post.split('</p>')
    for part in res:
        part = part.replace('<p>', '').replace('>>>', '').split('<<<')
        text = part[0].replace('\'', '\\\'')
        del part[0]
        if text:
            for i in xrange(0, len(part), 2):
                for photo in part[i:i+2]:
                    photo_id = photo.split(':')[0]
                    if 'photo1' in locals():
                        tcur.execute("select upload from adminfiles_fileupload where id=%s", photo_id)
                        photo2 = tcur.fetchone()['upload']
                        new_photo2 = datetime.datetime.utcfromtimestamp(row['created']).strftime('%Y/%m/%d') + '/' + photo2.split('/')[2]
                    else:
                        tcur.execute("select upload from adminfiles_fileupload where id=%s", photo_id)
                        photo1 = tcur.fetchone()['upload']
                        new_photo1 = datetime.datetime.utcfromtimestamp(row['created']).strftime('%Y/%m/%d') + '/' + photo1.split('/')[2]
                if 'photo2' not in locals():
                    photo2 = ""
                    new_photo2 = ""
                if 'text' in locals():
                    d.write(u"insert into me_postphoto (post_id, text, photo, photoRight) values ('%s', '%s', '%s', '%s');\n" % (post_id, unicode(text), new_photo1, new_photo2))
                    del text
                else:
                    d.write(u"insert into me_postphoto (post_id, photo, photoRight) values ('%s', '%s', '%s');\n" % (post_id, new_photo1, new_photo2))
                f.write('cp -v "%s" "%s"; rm -v "%s" ; \n' % (photo1, new_photo1, photo1))
                f.write('cp -v "%s" "%s"; rm -v "%s" ; \n' % (photo2, new_photo2, photo2))
                del photo1
                del photo2
con.commit()
cur.close
tcur.close
con.close
f.close()
d.close()
