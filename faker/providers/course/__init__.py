from .. import BaseProvider

class Provider(BaseProvider):
	subjects=["Art","Computer Science","English","Music"]
	
	grades=["A","A-","B+","B","B-","C+","C","C-","D+","D","D-","F"]
	
	titles=["Advanced Loitering",
			"Class 101",
			"Dirty Pictures",
			"Flipping Burgers for Fun and Profit", 
			"Getting Dressed",
			"History of Something",
			"How to Watch Television",
			"Introduction to Basics",
			"Joy of Garbage",
			"Learning!",
			"Philosophy and Star Trek",
			"Philosophy of the Simposons",
			"Rocket Surgery",
			"The Art of Walking",
			"The Beatles",
			"The Science of Superheroes",
			"The Strategy of Starcraft",
			"Theoretical Phys Ed",
			"Tree Climbing",
			"Underwater Basketweaving"]

	@classmethod
	def subject(cls):
		return cls.random_element(cls.subjects)
	
	@classmethod
	def grade(cls):
		return cls.random_element(cls.grades)
		
	@classmethod
	def title(cls):
		return cls.random_element(cls.titles)