n = int(input("Nhập số cần tính giai thừa: "))
try:
    int(n)
    def giaiThua(n):
        if n == 0:
            return 1
        return n * giaiThua(n - 1)
    print(giaiThua(n))
except :
    print("Đây không phải là một số, vui lòng nhập lại!")
