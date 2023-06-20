

def check_ids(ids: str, raising=True) -> list[int]:
    msg = "Invalid params. Please specify idVendor:idProduct"
    args = ids.split(':')
    if len(args) != 2:
        if raising:
            raise ValueError(msg)
        else:
            print(msg)
    return [int(arg, 16) for arg in args]
