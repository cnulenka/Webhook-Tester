def query_string_to_params(query_string: str) -> dict:
    params_dict = {}
    if len(query_string) > 0:
        params = query_string.split("&")
        for param in params:
            key_value = param.split("=")
            if len(key_value) == 2:
                params_dict[key_value[0]] = key_value[1]

    return params_dict
