import logging
import datetime

now = datetime.datetime.now()
dateFileName = now.strftime("%Y-%m-%d") + ".log"

def createLoggerObj():
  fileName = dateFileName
  formatStr = '%(asctime)s %(message)s'
  logging.basicConfig(format=formatStr, filename=fileName, level=logging.INFO)
  myLogObj = logging.getLogger('sqa2023-logger') 
  return myLogObj
