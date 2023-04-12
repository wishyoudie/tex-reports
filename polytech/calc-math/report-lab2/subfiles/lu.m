clear all;
A = rand(10);
[S, J] = eig(A);
for i = 1:15
    J(1,1) = J(1,1) * 10 ^ (i);
    A = S * J * inv(S);
    X = rand(10, 1);
    B = A * X;
    [L, U] = lu(A);
    Y = inv(L) * B;
    X1 = inv(U) * Y;
    pogr(i) = norm(X - X1) / norm(X);
    con(i) = cond(A);
end
plot(1:15, log10(pogr), 'b');
pause;
plot(1:15, log10(con), 'r');
