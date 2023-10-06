#!/usr/bin/python

import rrdtool
import random , time
from rrdtool import update as rrd_update

#RRD database creation

ret = rrdtool.create("example.rrd", "--step", "1", "--start", 'N',

"DS:metric1:GAUGE:2:U:U",

"RRA:AVERAGE:0.5:1:2",

"RRA:AVERAGE:0.5:2:10",

"RRA:AVERAGE:0.5:10:100",

"RRA:MAX:0.5:1:10",

"RRA:MAX:0.5:10:100")

#Input For Database
for i in range(1,1000):
	lol = random.uniform(40.0,60.0)	
	print(lol)
	ret = rrd_update('example.rrd', 'N:%s' %(str(lol)));
	time.sleep(1)

#For information of last update
info = rrdtool.info('example.rrd')
print(info['last_update'])



