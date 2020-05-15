import hashlib


class Node(object):
    def __init__(self, val=None, left=None, right=None):
        # Hash value of the node via hashlib.sha256(xxxxxx.encode()).hexdigest()
        self.val = val
        # Left node
        self.left = left
        # Right node
        self.right = right

    def __str__(self):
        return f':val={self.val},left={self.left},right={self.right}:'


class MerkleTrees(object):
    def __init__(self):
        self.root = None
        # txns dict: { hash_val -> 'file_path' } 
        self.txns = None
        self.level={}
        self.count=0
    def get_root_hash(self):
        return self.root if self.root else None

    def build(self, txns):
        """
        Construct a Merkle tree using the ordered txns from a given txns dictionary.
        """
        if len(txns) == 1:
            print("ROOT is")
            print(txns)
            for key, value in txns.items() :
                self.root=str(key)
            return txns.keys
        print(txns)
        # save the original txns(files) dict while building a Merkle tree.
        self.txns = txns
        txns_list = list(txns.keys())
        if len(txns_list)%2 != 0:
            txns_list.append(txns_list[-1])
        rootlist={}
        for index in range(0, len(txns_list)-1, 2):
            left = txns_list[index]
            right = txns_list[index+1]
            combine = left + right
            root = hashlib.sha256(combine.encode()).hexdigest()
            print("ROOT")
            print(root)
            current_node = Node(root, Node(left), Node(right))
            rootlist[root]="0"
            print("RootList")
            print(rootlist)
            self.level[self.count]=txns
            self.build(rootlist)



            


    def print_level_order(self):
        """
          1             1
         / \     -> --------------------    
        2   3       2 3
        """
        # TODO
        print(self.level)
        

    @staticmethod
    def compare(x, y):
        """
        Compare a given two merkle trees x and y.
        x: A Merkle Tree
        y: A Merkle Tree
        Pre-conditions: You can assume that number of nodes and heights of the given trees are equal.
        
        Return: A list of pairs as Python tuple type(xxxxx, yyyy) that hashes are not match.
        https://realpython.com/python-lists-tuples/#python-tuples
        """
        diff = []
        if x.get_root_hash() == y.get_root_hash():
            return diff
        
        # TODO
        
        return diff
