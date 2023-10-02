from spn.structure.Base import Node
import dill


def save(spn: Node, path: str):
    with open(path, "wb") as f:
        dill.dump(spn, f)


def load(path: str) -> Node:
    with open(path, "rb") as f:
        return dill.load(f)
