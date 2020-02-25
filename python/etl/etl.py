def transform(legacy_data):
    transformed_data = {}

    for key in legacy_data:
        if isinstance(legacy_data[key], list):
            for i in legacy_data[key]:
                transformed_data[i.lower()] = key
        else:
            transformed_data[legacy_data[key].lower()] = key

    return transformed_data