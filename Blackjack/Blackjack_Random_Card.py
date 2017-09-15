## Random Card Generator 

import random
rank = random.choice( (('A','2','3','4','5','6','7','8','9','T','J','Q','K')*4) )
suit = random.choice( ('c','d','h','s') )
card = rank + suit

print(card)
