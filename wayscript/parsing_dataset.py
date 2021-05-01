import json
import random

# Reading in Variables from Previous WayScript Modules
name = variables['name']
postcode = variables['postcode']
addr = variables['addr']
pricerange = variables['pricerange']
phone = variables['phone']
food = variables['food']
area = variables['area']

# Creating Dict objects to store values to
data = {}

# Beginning index 
i = 0

chosen_int = random.randint(0, len(name)-1)
chosen_str = ""
#Iterate over potentially many products on a single PO
for i in range (0, len(name)):
  order = {}
  order['name'] = name[i]
  order['postcode'] = postcode[i]
  order['addr'] = addr[i]
  order['pricerange'] = pricerange[i]
  order['food'] = food[i]
  order['area'] = area[i]
  order['phone'] = phone[i]
  data['order_'+str(i)] = order
  if i == chosen_int:
        chosen_str = 'order_'+str(i)
  i += 1
  

# write data to our dict



# create json format to pass to API
return_data = json.dumps(data[chosen_str])
  
variables['return_data'] = return_data
