class AEKPS1:
	"""
	คลาส AEKPS1 คือ 
	ข้อมูลภาควิชา

	Example
	#-------------------
	name1 = AEKPS1()
	name1.show_name()
	name1.show_youtube()
	name1.about()
	#-------------------
	"""
	def __init__(self):
		self.name = 'AE'
		self.page = 'https://www.facebook.com/kaveenon.jantra'

	def show_name(self):
		print('สวัสดีภาควิชาของฉันคือ {}'.format(self.name))
	def show_youtube(self):
		print('https://www.youtube.com/channel/UCWR3MwezKwOXzPSaFVtS5Iw')

	def about(self):
		text= """
		นี่คือภาควิชาที่เปิดสอนนิสิตทางด้าน
		วิศวกรรมเกษตร
		เพื่อให้ผู้เรียนได้ทราบถึง
		การประยุกต์ใช้หลักวิศวกรรมเพื่อการเกษตร
		"""
		print(text)


if __name__ == '__main__':
	name1 = AEKPS1()
	name1.show_name()
	name1.show_youtube()
	name1.about()

		
