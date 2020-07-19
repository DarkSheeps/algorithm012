def preorder(root: 'Node'):
    res_list = []
    def n_tree(root):
        if not root:
            return
        res_list.append(root.val)
        for child in root.children:
            n_tree(child)
    n_tree(root)
    return res_list

if __name__ == '__main__':

    print(preorder([1,3,5,6,2,4]))
