mydict={"Fast" : "Pradeep",
        "a" : 100,
        'b' : [1,2,3,4,5] ,
        "mydict1" : {"Pradeep" : "pawar",
                   "c" : [10,20,30,40]
                   }
}
#print(type(mydict)) #the dictionary is of a seperate data called dict
#print(mydict.keys())# This prints the keys that is fast , a, b , mydict1
#print(type(mydict.keys()))#The data type of keys is dict_keys
#print(list(mydict.keys()))#This arannges the keys of dictionary into a list
#print(type(list(mydict.keys())))
#print("\n")
#print(type(mydict['mydict1']['c'][0]))
#print("\n")
#print(mydict.values())
#print(mydict)
updatedict= {'1' : '2',
             "mydict1" : {'Prajwal' : 'Pawar'                 
             }
}
#mydict.update(updatedict)#Updates the mydict dictionary with updatedict it also rewrites if there are same varibale ka name
print(mydict.get("Fast1"))#THe main differnece between these two methods is that when we enter a key word that isnt present in the dictionary the .get method gives NONE as output but the other method gives error
print(mydict["Fast"])
print(mydict)
