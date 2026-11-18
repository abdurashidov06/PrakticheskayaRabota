# ATTS 03-24 R ABDURASHIDOV ABDULAZIZ

print("I am learning python")


import sys
print(sys.version)
a=12
b=8
print(a+b)

print("Local start is working")



import matplotlib.pyplot as plt
students=["Anna","Bek","Dana","Ezoz","Lola"]
scores=[56,96,45,62,77]
plt.bar(students,scores,color='green')
plt.axhline(60,color='orange',linestyle='--') #porog
plt.title('Balli studentov')
plt.ylabel('Bal')
plt.savefig('scores.png', dpi=150, bbox_inches='tight')