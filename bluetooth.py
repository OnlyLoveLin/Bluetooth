# 蓝牙手环对象
class Bracelet:
	'''
		bracelet_mac:手环mac地址
		avg_rssi:平均RSSI
		rssi_list:用来存放rssi列表
		rssi_distance:rssi计算出来的距离
	'''
	def __init__(self, bracelet_mac, rssi_list=None):
		self.bracelet_mac = bracelet_mac
		self.avg_rssi = 0
		if rssi_list == None:
			rssi_list =[]
		self.rssi_list = rssi_list
		self.rssi_distance = 0

	def get_distance(self):
		rssi_sum = 0
		print(self.rssi_list)
		for i in range(len(self.rssi_list)):
			rssi_sum += self.rssi_list[i]
		self.avg_rssi = int(rssi_sum/len(self.rssi_list))
		# print("this is avg_rssi:", self.avg_rssi)
		
		self.rssi_distance = self.calculation_distance(-50)
		# print("rssi_distance is :", self.rssi_distance)

	def calculation_distance(self, measuredPower):
		if self.avg_rssi >= 0:
			return -1.0
		elif measuredPower == 0:
			return -1.0
		rssi_ratio = self.avg_rssi * 1.0 / measuredPower
		if rssi_ratio < 1.0:
			return pow(rssi_ratio, 10)
		else:
			self.rssi_distance = (0.42093) * pow(rssi_ratio, 6.9476) + 0.54992
			return self.rssi_distance

	