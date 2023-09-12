def main():
    # We start from an 8 letter sequence
    start = "AACCGGTT"

    # We finish on an 8 letter sequence
    end = "AAACGGTA"
    
    # We have a list of acceptable intermediate sequences
    bank = ["AACCGGTA","AACCGCTA","AAACGGTA","TACCGGTT"]

    # We need to find the shortest path from beginning to end

    path = find_path(start,end,bank)

    print(path)

    if path:
        print(len(path))
    else:
        print(-1)



def find_path(start,end,bank):

    if not end in bank:
        bank.append(end)

    paths = [[start]]

    while True:
        print("Paths",paths)
        paths = extend_paths(paths,bank)

        if not paths:
            # We've run out of avenues to try
            return []
        
        # Check if we have a solution
        for path in paths:
            if path[-1] == end:
                return path

def extend_paths(paths,bank):
    new_paths = []
    for path in paths:
        # Get the last step
        last = path[-1]
        for seq in bank:
            if seq in path:
                # Never repeat
                continue

            if one_away(last,seq):
                p = path.copy()
                p.append(seq)
                new_paths.append(p)

    return new_paths
        
def one_away(a,b):

    if a==b: 
        return False

    diff = False

    for i in range(len(a)):
        if a[i] != b[i]:
            if diff:
                return False
            diff = True


    return diff

if __name__ == "__main__":
    main()