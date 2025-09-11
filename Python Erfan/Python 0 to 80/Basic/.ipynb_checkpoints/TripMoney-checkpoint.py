# -*- coding: utf-8 -*-
"""
Created on Mon Jun 23 14:02:11 2025

@author: ebfin
"""

pizza_price = 140
pizza_num = 12
doogh_price = 400
doogh_number = 6
ja_price = 4850
ja_number = 3
number_people = 3

kolle_kharj = (pizza_price * pizza_num) + (doogh_price * doogh_number ) + (ja_price * ja_number)
 
print("Kole Kharj = " +  str(kolle_kharj))
print("Each persone = " + str((kolle_kharj / number_people)))