clear all
m = 1;
k = 1/8;
p = 3/4;

a = 0;
b = 20;
h = 0.2;
x = a:h:b;
s = size(x);
points = s(2);
hold on; 

yp = @(t) 3 * exp(-0.5 * t) - 2 * exp(-0.25 * t);
plot(x, yp(x), 'r');

X = zeros(points);
XX = zeros(points, 1);
t = 0;
endval = yp(b);

d = abs(heul(t, points, h) - endval);
step = 1;
prec = 1e-8;
while d > prec
    t = t + step;
    newval = heul(t, points, h);
    if abs(newval - endval) < prec
        break
    end
    newd = abs(newval - endval);
    if newd > d
        t = t - step;
        step = -step / 2;
    else
        t = t + step;
    end
    d = newd;
end
X(1) = t;
XX(1) = 1;
for i=2:points
    X(i) = X(i - 1) + (-(3/4) * X(i - 1) - (1/8) * XX(i - 1)) * h;
    XX(i) = XX(i - 1) + X(i) * h / 2 + X(i - 1) * h / 2;
end
plot(x, XX, 'b');
hold off;
