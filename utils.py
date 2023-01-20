from inspect import getfullargspec
from typing import Dict, Callable, Any, Union, Tuple

from objects.commands import Required
from objects.stubs import Text

def getCallSignature(instance: Callable[[Any], Any]) -> Dict[str, Text]:
	result: Dict[str, str] = {}
	check_obj = instance
	key_exceptions = ["channel", "self", "return"]
	arg_spec = getfullargspec(check_obj)
	for parameter in arg_spec.args:
		if parameter not in key_exceptions:
			result[parameter] = ""
	for (parameter, annotation) in arg_spec.annotations.items():
		if parameter not in key_exceptions:
			result[parameter] = annotation
	return result

def getKeyByValue(collection: Dict[Any, Any], check_value: Any) ->\
Dict[Any, Any]:
	new_collection = {}
	for (key, value) in collection.items():
		if value == check_value:
			new_collection[key] = value
	return new_collection