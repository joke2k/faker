from . import BaseProvider
from .. import Generator
import itertools
class Provider(BaseProvider):


	def simple_profile(self):

		return {"username":self.generator.user_name(),
			"name":self.generator.name(),
			"sex": self.random_element(["M","F"]),
			"address":self.generator.address(),
			"mail":self.generator.free_email(),

			#"password":self.generator.password()
			"birthdate":self.generator.date(),

		}

	def profile(self):
		d={#"job":self.generator.job(),
		"ssn":self.numerify("###-##-####"),
		"residence":self.generator.address(),
		"current_location":(self.generator.latitude(),self.generator.longitude()),
		"blood_group":"".join(self.random_element(list(itertools.product(["A","B","AB","0"],["+","-"]))))
		}
		for i in range(1,self.random_int(1,5)):

			d["website-"+str(i)]=self.generator.url()

		return dict(d,**self.generator.simple_profile())


