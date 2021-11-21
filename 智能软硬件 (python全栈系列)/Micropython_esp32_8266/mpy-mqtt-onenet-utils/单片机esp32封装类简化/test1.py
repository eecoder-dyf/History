from T1 import *
#esp32端
###############################################
CLIENT_ID = "857129375"
username='234533'
password='2kJV69eUrcMgCxxxxxx'
###############################################
myMQTT = T1(CLIENT_ID,username,password)
#wifi
myMQTT.wifi("ywzywz","12345678")
myMQTT.mqttInit()
###############################################

data_name = ["temp","hum"]
data_value = [15.5,36.5]

def task_main():
    myMQTT.publish('$dp',data_name,data_value)
    myMQTT.c.check_msg() #检测接收并调用sub_cb

def run():
    while 1:
        task_main()
        time.sleep(5)
