from collections import defaultdict
from typing import List
class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king_name = kingName
        self.graph = defaultdict(list)
        self.dead = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.graph[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        result = []
        self.dfs(self.king_name, set(), result)
        return result
    
    def dfs(self, person, visited, result):
        if person not in self.dead and person not in visited:
            result.append(person)
        visited.add(person)
        for child in self.graph[person]:
            if child not in visited:
                self.dfs(child, visited, result)


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
