from inspect import get_annotations
from typing import Dict, Callable, Any, Union

from objects.stubs import Text

def getCallSignature(instance: Callable[[Any], Any]) -> Dict[str, Text]:
	result: Dict[str, str] = {}
	check_obj = instance
	key_exceptions = ["channel", "self", "return"]
	for (argument, annotations) in get_annotations(check_obj).items():
		if argument not in key_exceptions:
			result[argument] = annotations
	# for key in inspect.getfullargspec(check_obj).args:
	# 	if key not in key_exceptions:
	# 		result[key] = ""
	# annot_args = inspect.getfullargspec(check_obj).annotations
	# for (key, value) in annot_args.items():
	# 	if key not in key_exceptions:
	# 		result[key] = value
	return result

def getKeyByValue(collection: Dict[Any, Any], check_value: Any) ->\
Dict[Any, Any]:
	new_collection = {}
	for (key, value) in collection.items():
		if value == check_value:
			new_collection[key] = value
	return new_collection