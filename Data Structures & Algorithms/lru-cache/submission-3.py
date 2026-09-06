class ListNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class LRUCache:
    def __init__(self, capacity: int):
        self.store = {}
        self.ptrs = {}
        self.capacity = capacity
        self.head = None
        self.lhs = None
        self.rhs = None

    def cachify(self, key: int) -> None:
        # Get the element for the given key
        el = self.ptrs.get(key)
        
        # If lhs and rhs are already pointing to el, or rhs is pointing to el, no action is needed
        if (self.lhs == el and self.rhs == el) or (self.rhs == el):
            return

        # Case 1: If el is the leftmost node (self.lhs)
        elif self.lhs == el:
            # Move lhs to the extreme right
            temp = self.lhs.right  # Temporarily store the next node
            if temp:
                temp.left = None  # Disconnect the new lhs from the old lhs
            self.rhs.right = self.lhs  # Move lhs to the right of rhs
            self.lhs.left = self.rhs   # Link lhs back to rhs
            self.lhs.right = None      # Mark lhs as the new end

            # Update lhs and rhs pointers
            self.lhs = temp             # New lhs is the next node in the list
            self.rhs = self.rhs.right   # New rhs is the old lhs now at the end

        # Case 2: If el is a middle element, move it to the right
        else:
            # Move the middle element el to the extreme right
            prev = el.left
            next_node = el.right

            if prev:
                prev.right = next_node  # Link previous node to next node
            if next_node:
                next_node.left = prev   # Link next node back to previous node

            self.rhs.right = el         # Move el to the right of rhs
            el.left = self.rhs          # Set rhs as the previous of el
            el.right = None             # Mark el as the new end

            # Update rhs pointer to the new end
            self.rhs = el



    def add(self, key: int, value: int) -> None: 
        self.store[key] = value
        if self.rhs:
            node = ListNode(key)
            self.rhs.right = node
            node.left = self.rhs
            self.rhs = self.rhs.right
            self.ptrs[key] = node
        else:
            self.head = ListNode(key)
            self.lhs = self.head
            self.rhs = self.head
            self.ptrs[key] = self.head


    def removeOldest(self) -> None:
        # delete from the store
        x = self.lhs.val
        del self.store[x]
        del self.ptrs[x]

        # if lone el, reset everything
        if self.lhs == self.rhs:
            self.lhs = self.rhs = self.head = None
        # else just move right
        else:
            # print(self.head, self.lhs.val, self.rhs.val)
            self.lhs = self.lhs.right
            self.lhs.left = None
            # self.head = self.head.right

    def get(self, key: int) -> int:
        if key in self.store:
            # bring it to the most recently used
            self.cachify(key)
            
            return self.store.get(key)
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        if key in self.store:
            self.store[key] = value
            # bring it to most recently used
            self.cachify(key)

        else:
            
            if len(self.store) >= self.capacity:
                # print('here?', self.store, key, len(self.store), self.capacity)    
                # delete the most recently used one
                self.removeOldest()
                # add a new key to the store
                self.add(key, value)
            else:
                self.add(key, value)

        print(
    'put', key,
    'LHS:', getattr(self.lhs, 'val', 'None'),
    'RHS:', getattr(self.rhs, 'val', 'None'),
    'store:', self.store
)
        if self.lhs.right:
            print('mid:', self.lhs.right.val)




            
