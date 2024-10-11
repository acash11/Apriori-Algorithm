from itertools import combinations

def read_txt_to_2d_array(file_path):
    with open(file_path, 'r') as file:
        # Reading each line and splitting it into list of values
        array_2d = [list(map(int, line.split())) for line in file]
    return array_2d

def is_subset_in_freq_list(subsets, Lk):
    for subset in subsets: 
        #print(list(subset))
        #print(subset, Lk)
        if list(subset) not in Lk:
            return False
        return True

def candidate_search(Lk, k:int) -> list:
    #print(Lk, k)
    cand_Ck = []
    for p in range(len(Lk)):
        for q in range(p + 1, len(Lk)):

            l1, l2 = list(Lk[p]), list(Lk[q])
            #print(l1[:k-1], "////////", l2[:k-1])
            if l1[:k-1] == l2[:k-1]:
                #print("yes!")
                candidate = tuple(sorted(set(l1) | set(l2)))
                #print("candidate: ", candidate)
                subsets = combinations(candidate, k)
                if is_subset_in_freq_list(subsets, Lk):
                    cand_Ck.append(candidate)
                    #print(candidate, " is in freq list")
            
    return cand_Ck

def apriori(filename: str, min_support: int) -> list:

    L = []
    L.append([])

    count = {}
    datafile = read_txt_to_2d_array(filename)
    #print(len(datafile))
    #print("sdfsdf", int(len(datafile) * min_support / 100))
    min_support = int(len(datafile) * min_support / 100)
    print("Minimum Support: ", min_support)

    for line in datafile:
        for item in line:
            count[item] = count.get(item, 0)+1
    
    #Works, gets counts of each item
    #print (count)

    for key in count:
        if count[key] >= min_support:
            #print(count[key])
            L[0].append([key])
    #Works, gets Lists of all items that meet the support count
    #print("###", L)

    k = 1
    while L[k-1]:
        C = candidate_search(L[k-1], k)
        C_counts = {}
        #print(C)

        for line in datafile:
            #print("line: ", line)
            for candidate in C:
                #print("candidate: ", list(candidate))
                if set(candidate).issubset(set(line)):
                    #print("candidate is in line")
                    C_counts[candidate] = C_counts.get(candidate, 0) + 1

        #print(C_counts)
        L.append([])
        k += 1
        for candidate in C_counts:
            if C_counts[candidate] >= min_support:
                L[k-1].append(list(candidate))

        #print(L)
        #print(L[k-1])

    return(L)

if __name__ == "__main__":
    print("10%\n", apriori("datafile.txt", 10))
    print("20%\n", apriori("datafile.txt", 20))
    print("30%\n", apriori("datafile.txt", 30))
    print("50%\n", apriori("datafile.txt", 50))