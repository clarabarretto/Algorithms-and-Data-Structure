class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key
        self.height = 1


class AVL:
    def __init__(self):
        self.root = None

    def commands(self, entrada):
        try:
            if entrada[0] == "INSERIR":
                self.insert(self.root, entrada[1])
            elif entrada[0] == "DELETAR":
                self.delete(self.root, entrada[1], False)
            elif entrada[0] == "ALTURA":
                self.height(self.root, False)
            elif entrada[0] == "MAXIMO":
                self.maximo(self.root)
            elif entrada[0] == "MINIMO":
                self.minimo(self.root, False)
            elif entrada[0] == "FIM":
                print(self.printTree(self.root))
        except:
            print()

    def insert(self, node, key):
        if self.root is None:
            self.root = Node(key)
            print(f"{key} INSERIDO")

        if node is None:
            return Node(key)

        elif key.lower() < node.key.lower():
            new_subtree = self.insert(node.left, key)
            new_subtree.parent = node.left
            node.left = new_subtree

        elif key.lower() > node.key.lower():
            new_subtree = self.insert(node.right, key)
            new_subtree.parent = node.right
            node.right = new_subtree

        else:
            print(f"{key} JA EXISTE")
            return

        if node.key.lower() == self.root.key.lower():
            print(f"{key} INSERIDO")

        node.height = 1 + max(
            self.height(node.left, True), self.height(node.right, True)
        )
        b = self.balanced(node)

        if b > 1 and key.lower() < node.left.key.lower():
            return self.rightRotate(node)

        if b < -1 and key.lower() > node.right.key.lower():
            return self.leftRotate(node)

        if b > 1 and key.lower() > node.left.key.lower():
            node.left = self.leftRotate(node.left)
            return self.rightRotate(node)

        if b < -1 and key.lower() < node.right.key.lower():
            node.right = self.rightRotate(node.right)
            return self.leftRotate(node)

        return node

    def delete(self, node, key, silent=True):
        if node is None:
            if not silent:
                print(f"{key} NAO ENCONTRADO")
            return node

        elif key.lower() < node.key.lower():
            node.left = self.delete(node.left, key, silent)

        elif key.lower() > node.key.lower():
            node.right = self.delete(node.right, key, silent)

        else:
            if not silent:
                print(f"{key} DELETADO")

            if (
                self.root.left is None
                and self.root.right is None
                and key.lower() == self.root.key.lower()
            ):
                self.root = None
                return self.root

            if node.left is None:
                temp = node.right
                if node.key.lower() == self.root.key.lower():
                    self.root = temp
                node = None
                return temp

            elif node.right is None:
                temp = node.left
                if node.key.lower() == self.root.key.lower():
                    self.root = temp
                node = None
                return temp

            temp = self.minimo(node.right, True)
            old_key = node.key
            node.right = self.delete(node.right, temp.key)
            node.key = temp.key

            if self.root is not None and old_key.lower() == self.root.key.lower():
                self.root = node

        if node is None:
            return node

        node.height = 1 + max(
            self.height(node.left, True), self.height(node.right, True)
        )

        balance = self.balanced(node)

        if balance > 1 and self.balanced(node.left) >= 0:
            return self.rightRotate(node)

        if balance < -1 and self.balanced(node.right) <= 0:
            return self.leftRotate(node)

        if balance > 1 and self.balanced(node.left) < 0:
            node.left = self.leftRotate(node.left)
            return self.rightRotate(node)

        if balance < -1 and self.balanced(node.right) > 0:
            node.right = self.rightRotate(node.right)
            return self.leftRotate(node)

        return node

    def minimo(self, node, silent):
        if node is None and not silent:
            print("ARVORE VAZIA")
            return
        while node.left is not None:
            node = node.left
        if not silent:
            print(f"MENOR: {node.key}")
        return node

    def maximo(self, node):
        if node is None:
            print("ARVORE VAZIA")
            return
        while node.right is not None:
            node = node.right
        print(f"MAIOR: {node.key}")
        return node

    def leftRotate(self, node):
        rightSubTree = node.right
        x = rightSubTree.left

        rightSubTree.left = node
        node.right = x

        node.height = 1 + max(
            self.height(node.right, True), self.height(node.right, True)
        )
        rightSubTree.height = 1 + max(
            self.height(rightSubTree.right, True), self.height(rightSubTree.right, True)
        )

        if node.key == self.root.key:
            rightSubTree.height = 0
            self.root = rightSubTree

        return rightSubTree

    def rightRotate(self, node):
        leftSubTree = node.left
        x = leftSubTree.right

        leftSubTree.right = node
        node.left = x

        node.height = 1 + max(
            self.height(node.right, True), self.height(node.right, True)
        )
        leftSubTree.height = 1 + max(
            self.height(leftSubTree.right, True), self.height(leftSubTree.right, True)
        )

        if node.key == self.root.key:
            self.root = leftSubTree

        return leftSubTree

    def balanced(self, node):
        if node is None:
            return 0
        return self.height(node.left, True) - self.height(node.right, True)

    def height(self, node, silent=True):
        if node is None:
            height = 0
        else:
            if node.height == 0:
                node.height = 1 + max(self.height(node.left), self.height(node.right))
            height = node.height
        if not silent and height == 0:
            print("ARVORE VAZIA")
        elif not silent:
            print(f"ALTURA: {height}")
        return height

    def printTree(self, node):
        resposta = ""
        if self.root is None:
            return "ARVORE VAZIA"
        if node is not None:
            resposta += self.printTree(node.left) + " "
            resposta += node.key + " "
            resposta += self.printTree(node.right) + " "
        return resposta.strip()


end = False
avl = AVL()

while not end:
    try:
        entrada = input().split()
        end = avl.commands(entrada)
    except EOFError:
        break
