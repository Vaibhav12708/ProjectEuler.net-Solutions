from itertools import permutations

def generate_permutations():
    numbers = [0,1,2,3,4,5,6,7,8,9]
    all_permutations = list(permutations(numbers))
    return all_permutations

def main():
    permutations_list = generate_permutations()
    
    print("Total possible permutations:", len(permutations_list))
    print(permutations_list[999999])

if __name__ == "__main__":
    main()
