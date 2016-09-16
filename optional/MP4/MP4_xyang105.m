%Question a
load('digit6.mat')
M_matrix = mean(d);
d1 = d;
Covariance = 1/784*d1*d1';
[ev,ed] = eig(Covariance);

ed(1,1)

%Question b and c(c will change 5 to 2 below)
Y = ev*d1;
Cy = 1/784*Y*Y';

V = zeros(1,784);
for m = 1:784
    V(m) = real(Cy(m,m));  
end;

Sort_v = sort(abs(V));
Index = zeros(1,2);
for m = 1:784
    for n = 1:2
        if real(Cy(m,m)) == Sort_v(1,785-n)
            Index(1,n) = m;
        end;
    end;
end;

select_v = zeros(2,784);
for m = 1:2
    for n = 1:784
        select_v(m,n) = real(ev(Index(m),n));
    end;
end;

P = select_v*d1;

R = select_v(1:2,1:784)'*P;

random_n = [950,634,748,201,262];
%randi([1 958],1,2);

for n = 1:5
    figure;
    imagesc(reshape(R(:,random_n(n)),28,28))
    hold on
    title(['Reconstructed graph of sample number ' num2str(random_n(n)) ' using top 5 components']);
end;

