import random
class SkillIssueError(Exception):
	def __init__(self,SkillIssue):
		self.SkillIssue = SkillIssue
		super().__init__(self.SkillIssue)

def testskills():
	name = input("Enter your name: ")
	if "rohit" in name.lower():
		SkillIssue = "Rohit you can't pass this test. You have skill issues. Stfu and never use this module again"
		raise SkillIssueError(SkillIssue)
	else:
		num1 = str(random.randint(0,200))
		num2 = str(random.randint(0,200))
		l = ['+','-','*','/']
		exp = num1+random.sample(l,1)[0]+num2
		ans = eval(exp)
		uans = float(input(f"What is {exp}: "))
		if uans == ans:
			print(f"Congratulations!. You proved that you are {name} and not Rohit")
		else:
			SkillIssue = "HeHe you failed the test so bad idiot. You are either Rohit or you have skill issues like Rohit. Go join Rohit and never use this module again"
			raise SkillIssueError(SkillIssue)
