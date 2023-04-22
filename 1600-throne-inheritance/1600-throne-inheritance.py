class ThroneInheritance:

    def __init__(self, kingName: str):
        self.ThroneInheritance = defaultdict(list)
        self.ThroneInheritance['start'].append(kingName)
        self.deathList = set()
        
    def birth(self, parentName: str, childName: str) -> None:
        self.ThroneInheritance[parentName].append(childName)
        
    def death(self, name: str) -> None:
        self.deathList.add(name)

    def getInheritanceOrder(self) -> List[str]:
        def DFS(node,visited,ans):
            for i in self.ThroneInheritance[node]:
                if i not in visited:
                    if i not in self.deathList:
                        ans.append(i)
                    visited.add(i)
                    DFS(i,visited,ans)
            return ans
        return DFS('start',set(),[])
                    
            


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()