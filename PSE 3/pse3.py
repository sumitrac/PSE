strand_1 = ["C", "G", "T", "G", "A", "T"]
strand_2 = "AGTGAA"

def compare_dna(strand_1, strand_2):
    len1 = len(strand_1)
    len2 = len(strand_2)
    mismatches = []
    count = 0
    
    for char in range(0, min(len1, len2)):
        if strand_1[char] != strand_2[char]:
            mismatches.append("^")
            count = count + 1 
        else:
            mismatches.append(" ")
        
    print(strand_1)
    print("".join(mismatches))
    print(strand_2)
    print(f" {count} in total.")

compare_dna(2, strand_2)