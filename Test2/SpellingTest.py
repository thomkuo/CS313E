import sys

def spelling_test(s, l):
    for i in l:
        if i == s[0:len(i)]:
            reference_dict = l.copy()
            reference_dict.remove(i)
            recur = spelling_test_helper(s, reference_dict, i)
            if recur == True:
                return True
    return False

def spelling_test_helper(s, l, compare):
    #base case
    if compare == s:
        return True
    else:
        for i in l:
            alternate = compare + i
            if alternate == s[0:len(alternate)]:
                l.remove(i)
                return spelling_test_helper(s, l, alternate)



def main():
    s = input()
    lines = sys.stdin.readlines()
    print(spelling_test(s, [line.replace('\n', '') for line in lines]))
if __name__ == "__main__":
    main()


        
        
