#100 cats
#Homework should be uploaded at GitHub.com. Result of this HW should be a link to your GitHub code
#One day you decide to arrange all of your 100 cats in a giant circle. 
#Initially, none of your cats have any hats on. 
#You walk around the circle 100 times, always starting at the same spot, 
#with the first cat (cat # 1). 
#Every time you stop at a cat, you either put a hat on it if it doesn’t have one on, 
#or you take its hat off if it has one on.


def cats():
    cats = [False] * 100

    for i in range(1,101):
        for a in range(i-1,100,i):
            cats[a] = not cats[a]

    cats_with_hats = [j+1 for j, cat in enumerate(cats) if cat == True]
    return cats_with_hats

cats()


#Make function that can calculate hat with any amount of rounds and cats
def any_cats():
    cats_num = int(input("Enter number of cats:"))
    round_num = int(input("Enter number of rounds:"))
    cats = [False] * cats_num

    for i in range(1,round_num + 1):
        for a in range(i-1,cats_num,i):
            cats[a] = not cats[a]

    cats_with_hats2 = [j+1 for j, cat in enumerate(cats) if cat == True]
    return cats_with_hats2

any_cats()
