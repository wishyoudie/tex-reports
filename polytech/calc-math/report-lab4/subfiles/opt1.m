clear all;
hold on;
f = @(x) x.^4 - 3 * x.^3 + 2 * x.^2 - x + 1;
stv = 0;
h = 1e-2;
endv = 2;
x = stv:h:endv;
gold = (1 + sqrt(5)) / 2;
iter = 0;
while endv - stv > h
    iter = iter + 1;
    left = endv - (endv - stv) / gold;
    right = stv + (endv - stv) / gold;
    if (f(left) < f(right))
        endv = right;
    else
        stv = left;
    end
end
x0 = (stv + endv) / 2
iter
plot(x, f(x), 'black');
plot(x0, f(x0), '.', 'MarkerSize', 30);