# my task solution
def lowercase_count(strng):
    return len([j for j in strng if j in (chr(i) for i in range(97, 123))])


print(lowercase_count("abcABC123!@#$%^&*()_-+=}{[]|\':;?/>.<,~"))
print(lowercase_count("abcdefghijklmnopqrstuvwxyz"))
print(lowercase_count("abcABC123"))
print(lowercase_count("srbz2qaq8kef/#8h"))

# codewars task best solution
"""You have not earned access to this kata's solutions
Solutions are locked for kata ranked far above your rank. 
Rank up or complete this kata to view the solutions. :)
"""
"""
                        This is important!
                        
Today, 03/21/2023, "good people" from codewars reset my statistics, 
reset my rank. From the correspondence, I realized that my "kata" is very similar to the "kata" of Sansei. 
I also realized that, judging by the zeroing, I have not solved a single task myself since May 2022.
I am very grateful to these "kind people" from the codewars team.
P.S. I propose to ban mathematics and 4 mathematical operations, to ban Newton's second law
F = m * a, write as a = b * c, as well as any other similarity..."""