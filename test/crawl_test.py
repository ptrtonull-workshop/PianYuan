from pianyuan.mysql import *
from pianyuan.spider import *

account={'host':'localhost','username':'root','password':'root'}
acc = modify(account['host'],account['username'],account['password'])
db = create(acc)
run(1, 1, db)