from .. import BaseProvider

class Provider(BaseProvider):
	subjects=["English","Art","Computer Science","Music"]
	
	grades=["A","A-","B+","B","B-","C+","C","C-","D+","D","D-","F"]

	@classmethod
	def subject(cls):
		return cls.random_element(cls.subjects)
	
	@classmethod
	def grade(cls):
		return cls.random_element(cls.grades)