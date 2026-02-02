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
            