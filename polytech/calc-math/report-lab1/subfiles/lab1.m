clear all;
stv = 0;
endv = 20;
h = 0.2;
x = stv:h:endv;
s = size(x);
n = s(2);
hold on;
yp = @(t) exp(-0.5 * t) / (exp(-0.5) - exp(-0.25)) - exp(-0.25 * t) / (exp(-0.5) - exp(-0.25));
plot(x, yp(x), 'r');
X = zeros(n);
XX = zeros(n, 1);
t = 0;
endval = yp(endv);
d = abs(heul(t, n, h) - endval);
step = 1;
prec = 1e-10;
while d > prec
    t = t + step;
    newval = heul(t, n, h);
    if abs(newval- endval) < prec
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
XX(1) = 0;
for i = 2:n
    X(i) = X(i - 1) + ((-3/4) * X(i-1) - (1/8) * XX(i - 1)) * h;
    XX(i) = XX(i - 1) + X(i) * h / 2 + X(i - 1) * h / 2;
end
plot(x, XX, 'b');
hold off;
function heul = heul(t, n, h)
    X(1) = t;
    XX(1) = 0;
    for i = 2:n
        X(i) = X(i - 1) + ((-3/4) * X(i-1) - (1/8) * XX(i - 1)) * h;
        XX(i) = XX(i - 1) + X(i) * h / 2 + X(i - 1) * h / 2;
    end
    heul = XX(n);
end