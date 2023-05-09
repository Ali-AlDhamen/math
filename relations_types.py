def is_reflexive(relation):
    for x , _ in relation:
        if (x, x) not in relation:
            return False
    return True

def is_symmetric(relation):
    for x, y in relation:
        if (y, x) not in relation:
            return False
    return True

def is_antisymmetric(relation):
    for x, y in relation:
        if x != y and (y, x) in relation:
            return False
    return True

def is_transitive(relation):
    for x, y in relation:
        for z, w in relation:
            if y == z and (x, w) not in relation:
                return False
    return True

# Example usage
relation = {(1, 1),(1, 2), (2, 1), (2, 2), (3, 3)}
print("Reflexive:", is_reflexive(relation))
print("Symmetric:", is_symmetric(relation))
print("Antisymmetric:", is_antisymmetric(relation))
print("Transitive:", is_transitive(relation))