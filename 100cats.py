#100 cats
def cats():
    cats = [False] * 100

    for i in range(1,101):
        for a in range(i-1,100,i):
            cats[a] = not cats[a]

    cats_with_hats = [j+1 for j, cat in enumerate(cats) if cat == True]
    return cats_with_hats

cats()

#Any cats
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
