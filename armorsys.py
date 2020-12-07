#this software is property of William Chadwick
import random as rnd
class armor:
	def _init_(self,resisttype,resist,lvl,tier):
		self.resisttype='none'
		self.resist=0
		self.lvl=0
		self.tier='junk'
def armorrnd():
	def resisttypernd():
		resisttype=rnd.choice('fire','ice','electric','slag','corrosive','all')
	def resistrnd():
		resist=rnd.randint(1,1000)
	def lvlrnd():
		lvl=rnd.randint(0,30)
	def tierrnd():
		tier=rnd.choice('common','uncommon','rare','ultra rare','legendary','OP')
	resisttypernd()
	resistrnd()
	lvlrnd()
	tierrnd()
armor1=armor()
armorrnd()
print(armor1.self)