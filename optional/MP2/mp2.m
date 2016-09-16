A = sort(randi([-10,10],1,10));
B1 = A-randi([1,5]);
Co1 = (10*sum(A.*B1)-sum(A)*sum(B1))/(sqrt(10*sum(A.*A)-sum(A)^2)*sqrt(10*sum(B1.*B1)-sum(B1)^2));

B2 = B1 + 5*sqrt(std(B1)*std(A))*randi([-1,1],[1 10]);
B2 = fix(B2);
Co2 = (10*sum(A.*B2)-sum(A)*sum(B2))/(sqrt(10*sum(A.*A)-sum(A)^2)*sqrt(10*sum(B2.*B2)-sum(B2)^2));


C1 = -A+randi([1,5]);
Ce1 = (10*sum(A.*C1)-sum(A)*sum(C1))/(sqrt(10*sum(A.*A)-sum(A)^2)*sqrt(10*sum(C1.*C1)-sum(C1)^2));
C2 = C1 + 3*sqrt(std(C1)*std(A))*randi([-1,1],[1 10]);
C2 = fix(C2);
Ce2 = (10*sum(A.*C2)-sum(A)*sum(C2))/(sqrt(10*sum(A.*A)-sum(A)^2)*sqrt(10*sum(C2.*C2)-sum(C2)^2));