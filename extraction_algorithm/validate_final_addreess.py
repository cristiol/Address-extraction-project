

def validate_final_address(final_address):
    not_null_count = len([field for field in final_address.values() if field])
    if not_null_count <= 3:
        return None
    else:
        return final_address

