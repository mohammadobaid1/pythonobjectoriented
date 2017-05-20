class BankAccount:
	def __init__(self,minimumam):
		self.prebalance=minimumam
	def returnthreshold(self):
		return self.prebalance

	def printminimumbalance(self):
		print("Minimum balance to withdraw amount is ",self.prebalance)

class WithdrawAmount(BankAccount):
	def __init__(self,minimumam):
		BankAccount.__init__(self,minimumam)
	def amountwithdraw(self,amount):
		if int(amount) < int(self.returnthreshold()):
			print("Sorry minimum amount to be transferred should be= ",self.returnthreshold())
		else :
			self.amountdeducted=int(amount) - int(self.returnthreshold())		
			print("Amount deducted. Now you have= ",self.amountdeducted)


minimumamount=input("Enter minimum amount")
amountwithdrawdn=input("How much money you want to withdraw")
bankobj2=WithdrawAmount(minimumamount)
bankobj2.amountwithdraw(amountwithdrawdn)

