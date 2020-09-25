# map 함수 응용, print 다중 출력
a, b, c = map(int, input().split())
print("%d\n%d\n%d\n%d" % ((a+b)%c, ((a%c)+(b%c))%c, (a*b)%c, ((a%c)*(b%c))%c))