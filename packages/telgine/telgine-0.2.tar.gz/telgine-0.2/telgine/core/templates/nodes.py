class Node:
    body: list['Node']
    parent: 'Node'

    def add(self, node):
        node.parent = self
        self.body.append(node)

    def next(self) -> 'Node' | None:
        try:
            next_node_index = self.parent.body.index(self) + 1
        except IndexError:
            return None
        return self.parent.body[next_node_index]

    def prev(self) -> 'Node' | None:
        try:
            prev_node_index = self.parent.body.index(self) - 1
        except IndexError:
            return None
        return self.parent.body[prev_node_index]


class Expr(Node):
    def __init__(self, expr):
        self.expr = expr


class If(Node):
    test: Expr
    orelse: list[Node]

    def __init__(self, test, body: list[Node] | None = None, orelse: list[Node] | None = None):
        if orelse is None:
            orelse = []
        if body is None:
            body = []
        self.test = test
        self.body = body
        self.orelse = orelse

    def orelse_add(self, node: Node):
        node.parent = self
        self.orelse.append(node)


class For(Node):
    test: Expr

    def __init__(self, test: Expr, body: list[Node] | None = None):
        self.test = test
        self.body = body


class Else: pass


class Text(Node):
    text: str

    def __init__(self, text: str):
        self.text = text

    def __repr__(self):
        return self.text


class Tag(Node):
    name: str
    attrs: dict[str, str]

    def __init__(self, name: str, body: list[Node] | None = None, attrs: dict[str, str] | None = None):
        self.name = name
        self.body = body
        self.attrs = attrs

    def __repr__(self):
        return f'<{self.name}/>'

    def find(self, name) -> 'Tag' | None:
        for node in self.body:
            if node.name == name:
                return node
            return self.find(name)
        return None

    def mount(self):
        pass

    def unmount(self):
        pass

    def update(self):
        pass

    def render(self):
        pass


class Button(Tag):
    def render(self):
        pass



class Group(Tag):
    pass


class Message(Tag):
    pass


class Keyboard(Tag):
    pass
