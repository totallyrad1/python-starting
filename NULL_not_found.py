def NULL_not_found(object: any) -> int:
	if object or object == 0 or object == None or object == '':
		if object == '':
			print(f"Empty: {object} {object.__class__}")
		elif object == None:
			print(f"Nothing: {object} {object.__class__}")
		elif object.__class__ == float:
			print(f"Cheese: {object} {object.__class__}")
		elif object.__class__ == int:
			print(f"Zero: {object} {object.__class__}")
		elif object.__class__ == bool:
			print(f"Fake: {object} {object.__class__}")
		else:
			print(f"Type not Found")
			return 1
		return 0
	return 0
