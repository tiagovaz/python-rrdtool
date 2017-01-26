import rrdtool
import time

# Timeperiod for which we want the graph in sec
period = "300"

# For updation of graph after 10sec 
for i in range(1,100):
	ret = rrdtool.graph( "lol.png", "--start", "-%s" %(period), 
	"--vertical-label=Avg of 10s",
         '--watermark=playground.in.supportex.net',
         "-w 800",
	 "-h 500",
         "DEF:metric1=example.rrd:metric1:AVERAGE",
         "LINE1:metric1#0000FF:metric1\r",)
	time.sleep(10)

# Time is in UTC
