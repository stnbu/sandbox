import hashlib
from math import log2, ceil

def hash_string(s):
    return hashlib.sha256(s.encode()).hexdigest()

class MerkleTree:
    """
    A naive Merkle tree implementation using SHA256
    """
    def __init__(self, data):
        self.data = data
        next_pow_of_2 = int(2**ceil(log2(len(data))))
        self.data.extend([0] * (next_pow_of_2 - len(data)))
        self.tree = ["" for x in self.data] + \
                    [hash_string(str(x)) for x in self.data]
        for i in range(len(self.data) - 1, 0, -1):
            self.tree[i] = hash_string(self.tree[i * 2] + self.tree[i * 2 + 1])

    def get_root(self):
        return self.tree[1]

    def get_val_and_path(self, id):
        val = self.data[id]
        auth_path = []
        id = id + len(self.data)
        while id > 1:
            auth_path += [self.tree[id ^ 1]]
            id = id // 2
        return val, auth_path

def verify_merkle_path(root, data_size, value_id, value, path):
    cur = hash_string(str(value))
    tree_node_id = value_id + int(2**ceil(log2(data_size)))
    for sibling in path:
        assert tree_node_id > 1
        if tree_node_id % 2 == 0:
            cur = hash_string(cur + sibling)
        else:
            cur = hash_string(sibling + cur)
        tree_node_id = tree_node_id // 2
    assert tree_node_id == 1
    return root == cur

if __name__ == "__main__":
    breakpoint()
    m = MerkleTree(["Yes", "Sir", "I Can", "Boogie"])
