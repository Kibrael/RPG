
print()
print()
print("hello world {year}".format(year="10"))

#print(s.format(body_part="Leg", part_num="10", type="jnt"))

#take in base name string 
#take in args for name string formatting: body part, count, sub type
#how many parts?

def rename_stuffles(name_base="Leg_###_Jnt", index_start=0):
	"""
	name_base="{name}_{part_num}_{node_type}"
	"""
	#error message for bad string format
	if name_base.count("_") != 2:
		print("""invalid name base string entered. 
			\n Please enter name_base with format: part_###_node""")
		return

	print("\n\n")
	#create list to hold renamed objs
	renamed_objs = []

	#get objects in selection
	sel_objs = ["billy", "turkey", "stuffin"]
	print("selection objects:", sel_objs)
	#get count of # characters
	pounds = name_base.count("#")
	print("pounds: ", pounds)
	
	for i in range(len(sel_objs)):
		print("*" * 50)
		print("base name string:", name_base)
		#split name base string on _ because it is a known pattern
		name_base_parts = name_base.split("_")
		print(name_base_parts)
		#0 pad selection count to fill # characters properly
		part_count = str(i+index_start).zfill(pounds)
		print("count of # signs:", name_base.count("#"))
		#replace the # segment of the string, it will be the second item (index 1)
		
		name_base_parts[1] = part_count
		print("after substitution of # characters:", name_base_parts[1])

		#rejoin the string parts into the desired name
		new_name = "_".join(name_base_parts)
		print("new string name:", new_name)
		#rename each object using the new name string
			#call rename function on sel_objs[i] here
		#add new obj name to renamed_objs list
		renamed_objs.append(new_name)
		print()
		print()
	return renamed_objs

print(rename_stuffles())