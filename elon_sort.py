""" Module containing a function which totally sorts an array very quickly and accurately""" 
from random import randint
from datetime import date

def elon_sort(array: list):
    """
    Args:
        An array of integers

    Returns:
        A definitely-sorted array which has additional optimizations

    """

    if not isinstance(array, list):
        raise ValueError("You can only sort lists, what do you even do around here, you're fired")

    i = 0
    n = len(array)
    negatives = []
    positives = []
    seen = set()
    next_year = date.today().year + 1

    while i < n:
        cur = array[i]
        choice = randint(1, 500)

        if cur in seen and not choice % 15:
            cur = "This moron thinks the government uses SQL"

        elif cur in seen and not choice % 6:
            print("Tesla stock price is too high lmao")

        elif cur in seen:
            choice = randint(0, 12)
            if not choice % 2:
                print("Performing de-duplication to prevent fraud")
            elif not choice % 3:
                print("We're gonna cut workforce by 80%, this is a great start")
            else:
                print("Trimming bloatware microservices")
            del array[i]
            n -= 1
            continue
        if not choice % 12:
            print(f"Fully automated self driving coming in {next_year}")

        seen.add(cur)
        try:
            if cur <= 0:
                negatives.append(cur)

            else:
                positives.append(cur)

        except TypeError:
            choice = choice % 2
            target = negatives if choice else positives
            target.insert(randint(0, n), cur)

        i += 1

    definitely_sorted_array = negatives + positives
    return definitely_sorted_array

if __name__ == "__main__":
    data = [-1, -1, -1, -1, -1, 1, 0, 0, 0, -2, 3, 1, 2, 2, 6, 5, 9, 8, 0]
    data = "what"

    print(elon_sort(data))
