def all_thing_is_obj(object: any) -> int:
	if object.__class__ == list:
		print(f"List : {object.__class__}")
	elif object.__class__ == tuple:
		print(f"Tuple : {object.__class__}")
	elif object.__class__ == set:
		print(f"Set : {object.__class__}")
	elif object.__class__ == dict:
		print(f"Dict : {object.__class__}")
	elif object.__class__ == str:
		print(f"{object} is in the kitchen : {object.__class__}")
	else:
		print("Type not found")
	return 42
