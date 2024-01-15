
# def main():





# if __name__ == "__main__":
#     main()



import math


def split_check(total, number_of_people):
    if number_of_people <= 1:
        raise ValueError("More than 1 person is required.")
        # 手動引發異常
    return math.ceil(total/ number_of_people)

# 把可能有問題的 code放進try block
try:
    total_due = float(input("What is the total?  "))  # 這個assignment never happen
    number_of_people = int(input("How many people?  "))
    amount_due = split_check(total_due, number_of_people)
except ValueError as err:
    print("Oh! no! That's not a valid value")
    print("({})".format(err))
else:
    print("Each person owes $ {}".format(amount_due))



# def suggest(product_idea):
#     if len(product_idea) < 3:
#         raise ValueError('More than 3 character are required')
#     return product_idea + "inator"
#
# try:
#     product_idea = input("What's your idea? ")
#     ans = suggest(product_idea)
# except ValueError as err:
#     print("oh no!")
#     print("({})".format(err))
# else:
#     print(ans)