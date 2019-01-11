from pprint import pprint

class Human:
	def __init__(self):
		print("I am a Human.")

class Female(Human):
	def __init__(self):
		print("I am a Female.")
		super().__init__()

class Doctor(Human):
	def __init__(self):
		print("I am a Doctor.")
		super().__init__()

class Asian(Human):
	def __init__(self):
		print("I am an Asian.")
		super().__init__()

class Korean(Asian):
	def __init__(self):
		print("I am from Korea.")
		super().__init__()

class KoreanDoctor(Korean, Doctor):
	def __init__(self):
		super().__init__()

class FemaleKoreanDoctor(Female, KoreanDoctor):
	def __init__(self):
		super().__init__()

pprint(FemaleKoreanDoctor.mro())
fkd = FemaleKoreanDoctor()