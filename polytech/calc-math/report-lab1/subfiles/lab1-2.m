clear all;
stv = 0;
endv = 20;
h = 1;
x = stv:h:endv;
s = size(x);
n = s(2);
hold on;
yp = @(t) exp(-0.5 * t) / (exp(-0.5) - exp(-0.25)) - exp(-0.25 * t) / (exp(-0.5) - exp(-0.25));
plot(x, yp(x), 'r');
ai = 1 / h^2 - 3/4 / (2 * h);
bi = -2 / h + 1/8;     
ci = 1 / h^2 + 3/4 / (2 * h);
a(1) = -ci / bi;
a(1) = ci / bi;
for i = 2:n
    a(i) = ci / (-bi - ai * a(i - 1));
    b(i) = (ai * b(i - 1)) / (-bi - ai * a(i - 1));
end
y = zeros(1, n);
y(n) = yp(endv);
for i = (n - 1):-1:1
    y(i) = a(i) * y(i + 1) + b(i);
end
plot(x, y, 'b');
hold off;