def difference(first: int, second: int) -> int:
    return first - second


# function used with GXX
def string_size_list(element_list: list, footer_pointer_list: list[int]) -> list[int]:
    size_list = []
    for i in range(len(element_list) - 1):
        size = element_list[i+1].name_pointer - element_list[i].name_pointer
        size_list.append(size)
    last_size = footer_pointer_list[0] - element_list[-1].name_pointer
    size_list.append(last_size)
    return size_list