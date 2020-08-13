import os
import sys
import time
import base64
from azure.storage.queue import QueueClient

try:
  ##connection_string = os.environ['AzureWebJobsStorage']
  connection_string = "DefaultEndpointsProtocol=https;EndpointSuffix=core.windows.net;AccountName=kedastorage1;AccountKey=Dg+ydacn2doHY+JsKLFmlD1tfTYqgfwA3y15RBi9kxhbr/yIZDJHGmAEr38GVjiNQdLLV0P3/KfgIQEwIBlS9w=="
  ##queue_name = os.environ['QUEUE_NAME']
  queue_name = "js-queue-items"
except KeyError:
  print('Error: missing environment variable AzureWebJobsStorage or QUEUE_NAME')
  exit(1)

queue = QueueClient.from_connection_string(conn_str=connection_string, queue_name=queue_name)

for message in range(0, int(sys.argv[1])):
  queue.send_message(content=base64.b64encode('hello_'+str(message)))