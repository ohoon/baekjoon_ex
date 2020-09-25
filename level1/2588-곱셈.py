# print 다중 출력, 몫&나머지 활용
a = int(input())
b = int(input())
print("%d\n%d\n%d\n%d" % (a*(b%10), a*(int(b/10)%10), a*int(b/100), a*b))