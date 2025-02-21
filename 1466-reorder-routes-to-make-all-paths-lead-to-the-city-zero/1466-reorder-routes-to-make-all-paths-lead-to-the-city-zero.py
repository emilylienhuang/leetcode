class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        # keep track of the directed graph
        adj_list = collections.defaultdict(list)
        for n1, n2 in connections:
            adj_list[n1].append(n2)

        seen = set()
        seen.add(0)
        
        changed = 0

        while len(seen) < n:
            check_next = []
            for from_node, to_node in connections:
                if to_node in seen:
                    # if i can get to the destination, then I have visited where it is from
                    seen.add(from_node)
                elif from_node in seen:
                    # if I can only get where I'm from not where I'm to I need to reverse an edge
                    seen.add(to_node)
                    changed += 1
                else:
                    # I need to see if I can get to this location in the next iteration
                    check_next.append((from_node, to_node))
            connections = check_next
        return changed
