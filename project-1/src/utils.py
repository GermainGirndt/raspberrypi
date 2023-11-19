def validate_not_empty_array_of_instance(array, instance_type: type, variable_name: str):
    if not array or not isinstance(array, list):
        raise TypeError(f"{variable_name} must be of type list")
            
    for element in array:
        if not isinstance(element, instance_type):
            raise TypeError(f"Elements must be of type {instance_type}. Found: {type(element)}")

    if len(array) < 1:
        raise ValueError(f"{variable_name} must contain at least one element")