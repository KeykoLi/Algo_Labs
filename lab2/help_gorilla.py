"""Main module"""
from exeption import BananasNotFound


# Горила Джекі  із зоопарку Мюнхена любить їсти банани. На складі зоопарку є N кошиків (piles) з бананами,
# у і-тому кошику є певна кількість бананів Х. Кошики знаходяться під охороною, але охорона здійснює обхід зоопарку
# на Н годин, протягом якого Джекі може поласувати своєю улюбленою стравою.

# Джекі може з'їсти за годину К бананів. Кожну годину вона вибирає кошик з бананами і їсть К бананів звідти.
# Якщо кошик має менше, ніж К бананів, вона з'їдає всі банани з нього і більше не буде їсти бананів протягом цієї години.
# Джекі любить їсти повільно, але все ж хочеться закінчити споживання всіх бананів, перш ніж охоронці повернуться.

# Напишвть функцію, яка повертає мінімальне ціле число К, яке дозволить Джекі з'їсти всі банани на складі протягом Н
# годин, поки повернеться охорона.

# Приклад 1:
# piles = `[3,6,7,11]`,
# H = 8
# Результат:
# 4

# Важливо:
# 1 <= piles.length <= 10^4
# piles.length <= H <= 10^9
# 1 <= `piles[i]` <= 10^9

def eat_bananas(piles, h_time):
    validator = validation(piles, h_time)
    if validator is True:
        try:
            if 1 <= min(piles) <= 10**9:
                left, right = 1, max(piles)
            else:
                raise BananasNotFound

            while left < right:
                mid = left + (right - left) // 2
                hours_required = 0
                for pile in piles:
                    hours_required += (pile + mid - 1) // mid
                if hours_required <= h_time:
                    right = mid
                else:
                    left = mid + 1
            print(f"the minimum K integer that will allow Jackie to eat all the bananas"
                  f" in stock during {h_time} hours until security returns - {left}.")
            return left

        except BananasNotFound:
            print("There are not bananas in one of piles")

    else:
        print("Check array length ")


def validation(piles, h_time):
    if 1 <= len(piles) <= 10**4 and len(piles) <= h_time <= 10**9:
        return True


if __name__ == '__main__':
    # piles1 = [2, 2, 2, 3]
    # H1 = 8
    # print(eat_bananas(piles1, H1))

    piles2 = [3, 6, 7, 11]
    H2 = 4
    eat_bananas(piles2, H2)
