#this software is the property of William Chadwick
import random as rnd
class weapons:
	def __init__(self,level,dmg,dmgtype,element,manufacturer,weapontype,tier):
		self.level=0
		self.dmg=1
		self.dmgtype='melee'
		self.element='none'
		self.manufacturer='stock'
		self.weapontype='sword'
		self.tier='junk'
def weaponrnd():
	def levelrnd():
		level=rnd.randint(0,30)
	def dmgrnd():
	    if level>=0 and level<10:
		    dmg=rnd.randint(1,100)
	    elif level>=10 and level<20:
		    dmg=rnd.randint(101,200)
	    else:
		    dmg=rnd.randint(201,1000)
	def dmgtypernd():
		dmgtype=rnd.choice('melee','ranged')
	def elementrnd():
		element=rnd.choice('none','fire','electric','explosive','corrosive','slag','ice')
	def manufacturerrnd():
		manufacturer=rnd.choice('Vlads','Superion','Tryge','Goblin','Fahl','Dalisan')
	def weapontypernd():
		if dmgtype=='melee':
			weapontype=rnd.choice('sword','axe','spear','mace','hammer')
		elif dmgtype=='ranged':
			weapontype=rnd.choice('sniper','rifle','rocket launcher','pistol','smg','shotgun')
	def tierrnd():
		tier=rnd.choice('common','uncommon','rare','ultra rare','legendary','OP')
	levelrnd()
	dmgrnd()
	dmgtypernd()
	elementrnd()
	manufacturerrnd()
	weapontypernd()
	tierrnd()
weapon=weapons()
weaponrnd()
print(weapon.self)