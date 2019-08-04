## Bài 1
print('Kết quả:')
x = 6
print(x)
print(6)
print('6')

## Bài 2
print('Kết quả:')
x = 7
print(x)
print('x')

## Bài 3
10 = x

## Bài 4
print('this is the first String','n','this is the second String')
print('this is the first String','\n','this is the second String')

## Bài 6
# Chương trình nhập vào tên, năm sinh của bạn và năm hiện tại==> in ra màn hình số tuổi hiện tại của bạn
your_name = input('Nhập Họ tên của bạn: ')
print('Họ tên của bạn là: ', your_name)
# Nhập năm sinh và năm hiện tại
current_year = input('Nhập năm hiện tại: ')
your_birthday = input('Nhập năm sinh của bạn')
# Ép kiểu để thực hiện tính toán
your_age = int(current_year) - int(your_birthday)
# In ra màn hình số tuổi hiện tại #cách1
print('Số tuổi hiện tại của bạn: : ', your_age)

# In ra màn hình số tuổi hiện tại #cách2
print('Số tuổi hiện tại của bạn: : %s'% your_age)


## Bài - del()
name, age = 'Trần Tiến Duật', 21
print('Giá trị của biến name: ', name)
print('Giá trị của biến age: ', age)
# delete biến name
del(name)
print('Giá trị của biến name: ', name)
print('Giá trị của biến age: ', age)

## Bài - type()
name, age = 'Trần Tiến Duật', 21
print('Kiểu dữ liệu của biến name: ', type(name))
print('Kiểu dữ liệu của biến age: ', type(age))
# Ép kiểu biến age
age = float(age)
print('Kiểu dữ liệu của biến age: ', type(age))
# Ép kiểu biến name
float(name)
print('Kiểu dữ liệu của biến name: ', type(name))


## ADVANCED - formatting
one = 'first String'
two = 'second String'
# first way - old - cannot re-arranging order of arguments
print('%s %s' % (one, two))
# second way - new - possible to re-arranging order of arguments
print('{1} {0}'.format(one, two))

## ADVANCED - str() & repr
import datetime
today = datetime.datetime.now()

# Prints readable format for date-time object
print('This is the way that the user can understand: ', str(today))
# prints the official format of date-time object
print('This is the \"official\" representation that we can reconstruct the object: ', repr(today))


# A Python program to demonstrate that a function
# can be defined inside another function and a
# function can be passed as parameter.

# Adds a welcome message to the string
def messageWithWelcome(str):

    # Nested function
    def addWelcome():
        return "Welcome to "

    # Return concatenation of addWelcome()
    # and str.
    return  addWelcome() + str

# To get site name to which welcome is added
def site(site_name):
    return site_name

# passing function as an argument
print (messageWithWelcome(site("GeeksforGeeks")))