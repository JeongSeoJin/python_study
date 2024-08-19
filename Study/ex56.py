#예외처리
#calculater

try:
    print("This is a calculater only for debation")
    nums = []
    nums.append(int(input("write here the first number : ")))
    nums.append(int(input("write here the second number : ")))
    nums.append(int(nums[0] / nums[1]))
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError:
    print("you got Error")
except ZeroDivisionError as err: #에러에대한 처리 가능
    print(err)
except Exception as err:
    print("알 수 없는 에러가 발생하였습니다.")
    print(err)