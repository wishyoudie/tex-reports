clear all;
A = rand(10);
[S, J] = eig(A);
for i = 1:15
    J(1,1) = J(1,1) * 10 ^ (i);
    A = S * J * inv(S);
    X = rand(10, 1);
    B = A * X;
    [Q, R] = qr(A);
    Y = inv(Q) * B;
    X1 = inv(R) * Y;
    pogr(i) = norm(X - X1) / norm(X);
end
plot(1:15, log10(pogr), 'b');
