class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        out = []
        for i in range(len(path)):
            if path[i] == "" or path[i] == ".":
                continue
            elif path[i]=="..":
                if out:
                    out.pop(-1)
            else:
                out.append(path[i])
        path = "/".join(out)
        return "/"+path
        
