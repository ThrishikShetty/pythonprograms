test_dict = {'gfg': [7, 6, 3],'is': [2, 10, 3],'best': [19, 4]}
print("The original dictionary is : " + str(test_dict))
res = dict()
for key in sorted(test_dict):
  res[key] = sorted(test_dict[key])
print("The sorted dictionary : " + str(res))
