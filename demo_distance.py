import time
import math
import paho.mqtt.client	as mqtt
import msgpack
import numpy as np
from bluetooth import *
from bracelet_local import *

# 两个手环位置对象
l1 = Local(9)
l2 = Local(64)
# 三个rssi队列

def	on_subscribe(mosq, obj,	mid, granted_qos):
	print("Subscribed: " + str(mid))

def	on_message(mosq, obj, msg):
	# print(msgpack.unpackb(msg.payload))
	# print(msgpack.unpackb(msg.payload)[b'mac'])
	# 将此MAC地址改为自己网关的MAC地址
	if (msgpack.unpackb(msg.payload)[b'mac'] == b"B4E62DC0414D"):
		b1 = Bracelet(9)
		b2 = Bracelet(64)

		print("===============================================")
		print("id:", msgpack.unpackb(msg.payload)[b'mid'])
		print("网关IP地址:", msgpack.unpackb(msg.payload)[b'ip'])
		msgpack_list = msgpack.unpackb(msg.payload)[b'devices']
		

		# 过滤数据报信息
		for d in range(len(msgpack_list)):
			msgpack_bytes = msgpack_list[d]
			if (int(msgpack_bytes[6])) == b1.bracelet_mac:
				rssi = int(msgpack_bytes[7])-256
				print("蓝牙设备mac:%x:%x:%x:%x:%x:%x" %(msgpack_bytes[1], msgpack_bytes[2], msgpack_bytes[3], msgpack_bytes[4], msgpack_bytes[5], msgpack_bytes[6]))
				print("网关一手环9RSSI:", rssi)
				b1.rssi_list.append(rssi)
				b1.get_distance()
				print(b1.bracelet_mac, "distance is ", b1.rssi_distance)

			if (int(msgpack_bytes[6])) == b2.bracelet_mac:
				rssi = int(msgpack_bytes[7])-256
				print("蓝牙设备mac:%x:%x:%x:%x:%x:%x" %(msgpack_bytes[1], msgpack_bytes[2], msgpack_bytes[3], msgpack_bytes[4], msgpack_bytes[5], msgpack_bytes[6]))
				print("网关一手环64的RSSI:", rssi)
				b2.rssi_list.append(rssi)
				b2.get_distance()
				print(b2.bracelet_mac, "distance is ", b2.rssi_distance)
		print("--------------------")
		l1.x = b1.rssi_distance
		l2.x = b2.rssi_distance

	elif (msgpack.unpackb(msg.payload)[b'mac'] == b"30AEA48F46F0"):
		b1 = Bracelet(9)
		b2 = Bracelet(64)

		print("===============================================")
		print("id:", msgpack.unpackb(msg.payload)[b'mid'])
		print("网关IP地址:", msgpack.unpackb(msg.payload)[b'ip'])
		msgpack_list = msgpack.unpackb(msg.payload)[b'devices']

		# 过滤数据报信息
		for d in range(len(msgpack_list)):
			msgpack_bytes = msgpack_list[d]
			if (int(msgpack_bytes[6])) == b1.bracelet_mac:
				rssi = int(msgpack_bytes[7])-256
				print("蓝牙设备mac:%x:%x:%x:%x:%x:%x" %(msgpack_bytes[1], msgpack_bytes[2], msgpack_bytes[3], msgpack_bytes[4], msgpack_bytes[5], msgpack_bytes[6]))
				print("网关二手环9RSSI:", rssi)
				b1.rssi_list.append(rssi)
				b1.get_distance()
				print(b1.bracelet_mac, "distance is ", b1.rssi_distance)

			if (int(msgpack_bytes[6])) == b2.bracelet_mac:
				rssi = int(msgpack_bytes[7])-256
				print("蓝牙设备mac:%x:%x:%x:%x:%x:%x" %(msgpack_bytes[1], msgpack_bytes[2], msgpack_bytes[3], msgpack_bytes[4], msgpack_bytes[5], msgpack_bytes[6]))
				print("网关二手环64的RSSI:", rssi)
				b2.rssi_list.append(rssi)
				b2.get_distance()
				print(b2.bracelet_mac, "distance is ", b2.rssi_distance)
		print("--------------------")
		l1.y = b1.rssi_distance
		l2.y = b2.rssi_distance
		
	
	elif (msgpack.unpackb(msg.payload)[b'mac'] == b"B4E62DBE98FD"):
		b1 = Bracelet(9)
		b2 = Bracelet(64)

		print("===============================================")
		print("id:", msgpack.unpackb(msg.payload)[b'mid'])
		print("网关IP地址:", msgpack.unpackb(msg.payload)[b'ip'])
		msgpack_list = msgpack.unpackb(msg.payload)[b'devices']

		# 过滤数据报信息
		for d in range(len(msgpack_list)):
			msgpack_bytes = msgpack_list[d]
			if (int(msgpack_bytes[6])) == b1.bracelet_mac:
				rssi = int(msgpack_bytes[7])-256
				print("蓝牙设备mac:%x:%x:%x:%x:%x:%x" %(msgpack_bytes[1], msgpack_bytes[2], msgpack_bytes[3], msgpack_bytes[4], msgpack_bytes[5], msgpack_bytes[6]))
				print("网关三手环9RSSI:", rssi)
				b1.rssi_list.append(rssi)
				b1.get_distance()
				print(b1.bracelet_mac, "distance is ", b1.rssi_distance)

			if (int(msgpack_bytes[6])) == b2.bracelet_mac:
				rssi = int(msgpack_bytes[7])-256
				print("蓝牙设备mac:%x:%x:%x:%x:%x:%x" %(msgpack_bytes[1], msgpack_bytes[2], msgpack_bytes[3], msgpack_bytes[4], msgpack_bytes[5], msgpack_bytes[6]))
				print("网关三手环64的RSSI:", rssi)
				b2.rssi_list.append(rssi)
				b2.get_distance()
				print(b2.bracelet_mac, "distance is ", b2.rssi_distance)
		print("--------------------")
		l1.z = b1.rssi_distance
		l2.z = b2.rssi_distance
	print("*************************")
	l1.get_local()
	l2.get_local()

def	on_connect(mosq, obj,flags,	rc):
	print("Connected with result code "+str(rc))
	mqttc.subscribe("your-topic", 0)
	print("Connected")


mqttc =	mqtt.Client()
mqttc.username_pw_set("hello", "12345678")
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe
mqttc.on_message = on_message
mqttc.connect("mqtt.bconimg.com", 1883,	60)
mqttc.loop_forever()