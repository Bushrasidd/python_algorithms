# Initialize a list (list = []).
# You can perform the following commands on it as you read them from the input:
# insert,print,remove,append,sort,pop,reverse
# The program should first read an integer n (the number of commands), followed by n lines of commands. 
# Iterate through each command in order and perform the corresponding operation on your list.

# Example:

# Input:
# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print

# Output:
# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]


if __name__ == '__main__':
    n = int(input()) 
    my_list = []
    
    for i in range(n):
        cmd_parts = input().split()
        cmd = cmd_parts[0]
        
        if cmd == "insert":
            position = int(cmd_parts[1])
            num = int(cmd_parts[2])
            my_list.insert(position, num)
            
        elif cmd == "print":
            print(my_list)
            
        elif cmd == "remove":
            removable_item = int(cmd_parts[1])
            my_list.remove(removable_item)
            
        elif cmd == "append":
            item = int(cmd_parts[1])
            my_list.append(item)
            
        elif cmd == "sort":
            my_list.sort()
            
        elif cmd == "pop":
            my_list.pop()
            
        elif cmd == "reverse":
            my_list.reverse()
            