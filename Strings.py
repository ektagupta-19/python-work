#!/usr/bin/env python
# coding: utf-8

# In[1]:


var="Welcome to the practice exercise"
print (var)


# In[2]:


cc=input("whats is your name?")

# Print the string:
print(cc)


# In[3]:


print("#"*15)


# In[6]:


c= str(1.8)
print (c)


# In[7]:


one= input("num1")
sec=input("num2")
print(int(one)* int(sec))


# In[8]:


print(6%4)


# In[10]:


print('I can\'t study any longer')


# In[11]:



line= '     I hope you enjoyed this practice session.'
print(line.rstrip(5))


# In[20]:


string = "OQYWFClFhFGAvIWYwGKpmZhnJiyzTslSIhSwvOsqJMEphzmifTkyqOMNpnOtXZxmCfgDYqbaBHAUvIWhMnvwZnEMVDvmEfLrDoQnAZgQEgXQVnmSYkfedpAdhrtpOgORpYLRZYGWdhWYuqQssCUXtTzKRDAhpjUheOzUroZNzWFtZOVwIapzUYtbSbjYNErzQ"
print(string.find(46))


# In[21]:


word = ['1','2','3','4']
word[ : ] = [ ] 
print(word)


# In[25]:


import random
print(random.randint(100,135))


# In[26]:


list=[2,4,6,8,10,12,14,16,18,20]
print(list)


# In[29]:



list3=[1,2,'r',7,'k',6,'o','h','d',5,9]
print(list3.count('k'))


# In[30]:



tuple1=(1,'hello','world','567')
print(tuple1[2])


# In[31]:



tuple2=(1,25,67,100,3,54)
print (sorted(tuple2))


# In[33]:



list4=[1,2,4,6,3,2,5,4,7,4,6,5,3,2,2,1]
print(set(list4))
print(len(set(list4)))


# In[36]:


a={1,2,3,5,6,7}
b={4,5,8,9,2,3}
print (a|b)
print (a&b)
print (a-b)
print(a.symmetric_difference(b))


# In[38]:


dict={'Sam':21,'cody':12, 'addy':13,'zach':45,'army':6 }
print(dict)


# In[39]:


dict={'Sam':21,'cody':12, 'addy':13,'zach':45,'army':6 }
dict["zach"]=47
print(dict)


# In[40]:


sorted(dict)
print(dict)


# In[41]:


processed_orders = [1152, 1154, 1155, 1156, 1157, 1160, 1161, 1162, 1166, 1169, 1170, 1172, 1176, 1050, 1178, 1051, 1052, 1054, 1058, 1060, 1061, 1062, 1065, 1066, 1067, 1068, 1069, 1076, 1077, 1080, 1081, 1083, 1091, 1085, 1088, 1089, 1131, 1092, 1094, 1095, 1099, 1102, 1103, 1104, 1106, 1107, 1108, 1109, 1111, 1117, 1119, 1121, 1150, 1128, 1129, 1136, 1137, 1139, 1140, 1141, 1144, 1148, 1124]

# List of order ID’s which are returned
returned_orders = [1153, 1158, 1159, 1163, 1164, 1165, 1167, 1168, 1171, 1173, 1174, 1175, 1177, 1053, 1055, 1056, 1057, 1059, 1063, 1064, 1070, 1071, 1072, 1073, 1074, 1075, 1078, 1079, 1082, 1084, 1086, 1087, 1090, 1093, 1096, 1097, 1098, 1100, 1101, 1105, 1110, 1112, 1113, 1114, 1115, 1116, 1118, 1120, 1122, 1123, 1125, 1126, 1127, 1130, 1132, 1133, 1134, 1135, 1138, 1142, 1143, 1145, 1146, 1147, 1149, 1151]

print(len(processed_orders)+ len(returned_orders))


# In[50]:


list= processed_orders+returned_orders
print((sorted(list))[49])


# In[51]:


list= processed_orders+returned_orders
print((sorted(list))[49])

print ((sorted(list))[49] in processed_orders)
print ((sorted(list))[49] in returned_orders)


# In[52]:


print((sorted(list))[-1])


# In[46]:


print(list[:3])


# In[54]:


print((sorted(list))[:3])


# In[56]:


Employee_data ={101: 43, 102: 25, 103: 43, 104: 31, 105: 26, 106: 28, 107: 29, 108: 43, 109: 25, 110: 22, 111: 22, 112: 25, 113: 30, 115: 45, 116: 23, 117: 29, 118: 28, 119: 30, 120: 28, 121: 42, 122: 39, 123: 29, 124: 42, 125: 43, 126: 42, 127: 40, 128: 27, 129: 23, 130: 30, 131: 37, 132: 20, 133: 36, 134: 27, 135: 27, 136: 22, 137: 28, 138: 23, 139: 45, 140: 39, 141: 29, 142: 33, 143: 39, 145: 34, 146: 26, 147: 30, 148: 38, 149: 29, 150: 24, 151: 28, 152: 34, 153: 42, 154: 29, 155: 23, 156: 31, 158: 25, 160: 45, 161: 42, 162: 27, 163: 24, 164: 20, 166: 24, 167: 28, 168: 20, 169: 33, 170: 34, 171: 37, 172: 45, 173: 35, 174: 23, 175: 44, 176: 27, 177: 30, 178: 26, 179: 27} 
print(max(Employee_data.values))


# In[ ]:







s='aabupGradaab'.strip('a').strip('b').strip('a')
print(s)
# %%
print(((500//7) % 5) ** 3)
# %%
D = {1:['Raj', 22], 2:['Simran', 21], 3:['Rahul', 40]}
for val in D:
     print(val)
# %%
single_word_list=[]
paragraph="abc def gf"
for sentence in paragraph:
    for word in sentence.split():
        single_word_list.append(word)
print(single_word_list)
