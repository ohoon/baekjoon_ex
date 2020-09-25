# map 함수 응용, print 다중 출력
a, b = map(int, input().split())
print("%d\n%d\n%d\n%d\n%d" % (a+b, a-b, a*b, a/b, a%b))