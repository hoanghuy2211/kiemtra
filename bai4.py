
n = int(input("Nhập số nguyên dương n = "));

def tong(n):
    t = 0;
    while (n > 0):
        t = t + n % 10;
        n = int(n / 10);
    return t;

print("Tổng các chữ số của", n, "là", tong(n));
6
