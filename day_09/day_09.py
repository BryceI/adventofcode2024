import functools

input = open('day_09/input_09_sample.txt').read()
print(input)
 
# filesystem is compacted (no free space available), not-dense format (string, one block per char) for disk map.
# recursive function for computing filesystem checksum. current_index is the index of the head of the list
def filesystem_checksum(filesystem: str, current_index: int):
    if len(filesystem) == 0:
        return 0
    return int(filesystem[0]) * current_index + filesystem_checksum(filesystem[1:], current_index + 1)

def file_id(file_index:int):
    if file_index % 2 == 0:
        return file_index // 2
    else:
        return 0

# #end_position is [file_index, position_within_file]
# def end_file_id(end_position:list, dense_filesystem_length: int):
#     file_index = dense_filesystem_length - end_position[0] - 1
#     if file_index % 2 == 0:
#         return file_index // 2
#     else:
#         return 0

def next_position(dense_filesystem: str, current_position:list):
    return['123', [1,2]]


# dense_filesystem: string representing the dense version of the filesystem
# original_filesystem_length: int representing the overall length of the dense filesystem. Needed to calculate file_ids of files at end of filesystem
# file_index: int representing the current index that the current_position pointer is pointing to. The index of the pointer in dense_filesystem space. 
#     Note that file_id = file_index // 2 if file_index % 2 == 0
#     For the end_position pointer, file_id = file_length
# 
def dense_filesystem_checksum(dense_filesystem:str, original_filesystem_length: int, file_index: int, current_index:int, current_position:tuple, end_position:tuple):
    if len(dense_filesystem) == 0:
        return 0
    
    return 42

print("checksum is ", filesystem_checksum(input, 0))
print("checksum is ", filesystem_checksum('0099811188827773336446555566', 0))

print("checksum is" , dense_filesystem_checksum('2333133121414131402', len('2333133121414131402'), 0, 0, [0, 0], [len('2333133121414131402') - 1, 0]))


filesystem_length = len("2333133121414131402")
end_pointer = [ filesystem_length - 1, 0]

for index, entry in enumerate("2333133121414131402"):
#    print(entry, file_id(index))
    print(end_file_id([end_pointer[0] - index, end_pointer[1]], filesystem_length))