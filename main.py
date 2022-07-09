# keyword arguments


print("\n== Guess Correct Order of Name == ")
print("Input your full name in an unordered way: ")
st_name = input("1st name: ")
nd_name = input("2nd name: ")
rd_name = input("3rd name: ")
tries = 1
count_invalid = 0
guess_name = st_name + ' ' + nd_name + ' ' + rd_name
print("\nThe name: ", guess_name)
is_it_right = input("Is it right (y/n) or stop (s): ")

while (is_it_right != 's' and is_it_right != 'S') and (is_it_right != 'y' and is_it_right != 'Y') and tries < 6:
    # if count_invalid == 0:
    tries += 1

    # if count_invalid > 0:
    #     count_invalid -= 1

    if is_it_right == 'n' and is_it_right == 'n' and tries == 2:
        guess_name = st_name + ' ' + rd_name + ' ' + nd_name
    elif is_it_right == 'n' and is_it_right == 'n' and tries == 3:
        guess_name = nd_name + ' ' + st_name + ' ' + rd_name
    elif is_it_right != 'n' and is_it_right != 'N':
        count_invalid += 1

    # if count_invalid > 0:
    #  if tries == 4:
    #     tries -= 1
        print("\n[Invalid input]")
        print("tries: ", tries)
        is_it_right = input("Would you want to stop (y/n)? ")
    # else:
    #     print("\n[Invalid input]")
    #     print("tries: ", tries)
    #     is_it_right = input("Would you want to stop (y/n)? ")

    if tries <= 3 and count_invalid == 0:
        print("\nThe name: ", guess_name)
        is_it_right = input("Is it right (y/n) or stop (s): ")

    if tries > 3:
        if tries == 4:
            print("\nI lost, I've guessed wrong 3 times")
            is_it_right = input("Would you want to stop guessing (y/n): ")
            print("count invalid: ", count_invalid)

        if is_it_right == 'n' and is_it_right == 'n' and tries == 4:
            guess_name = nd_name + ' ' + rd_name + ' ' + st_name
        elif is_it_right == 'n' and is_it_right == 'n' and tries == 5:
            guess_name = rd_name + ' ' + st_name + ' ' + nd_name
        elif is_it_right == 'n' and is_it_right == 'n' and tries == 6:
            guess_name = rd_name + ' ' + nd_name + ' ' + st_name

        if count_invalid == 0:
            print("\nThe name: ", guess_name)
            is_it_right = input("Is it right (y/n) or stop (s): ")

if is_it_right == 'y' or is_it_right == 'Y':
    print("\n[Good Game! :)]")

if is_it_right == 'N' or is_it_right == 'n':
    print("\n[I lost, will try again later!]")

if is_it_right == 's' or is_it_right == 'S':
    print("\n[Lets play again later!]")


# Order of Guessing possibilities:
# 123
# 132
# 213
# 231
# 312
# 321
