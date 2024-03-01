Vertex = type('Vertex', (tuple[int],), dict())


class Graph:
    Adj: dict[Vertex, list[Vertex]] = dict()