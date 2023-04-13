clear all;
k = 3;
for i = 1:k
    J(i, i) = rand(1);
end
S = orth(rand(k));
for i = 1:15
    A = S * J * inv(S);
    B = rand(3, 1);
    X = inv(A) * B;
    [L, U] = lu(A);
    Y = inv(L) * B;
    X1 = inv(U) * Y;
    dlu(i) = norm(X - X1) / norm(X);
    [Q, R] = qr(A);
    Y = inv(Q) * B;
    X1 = inv(R) * Y;
    dqr(i) = norm(X - X1) / norm(X);
    C = chol(A);
    X1 = inv(C)) * inv(C')* B;   
    cholesky(i) = norm(X - X1) / norm(X);
end
hold on
plot(1:15, dlu, 'r');
plot(1:15, dqr, 'b');
plot(1:15, cholesky, 'black');