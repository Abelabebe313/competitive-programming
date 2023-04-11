"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        import_dict = defaultdict(list)
        
        for i in range(len(employees)):
            import_dict[employees[i].id] =  [employees[i].importance, employees[i].subordinates]
        visited = set()
        total = 0
        def DFS(ID):
            nonlocal total
          
            visited.add(ID)
            total += import_dict[ID][0]
            
            for child in import_dict[ID][1]:
                if child not in visited:
                    DFS(child)
            
        DFS(id) 
        return total