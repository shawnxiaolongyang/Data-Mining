%Question 1 (|)

%L1
comet(ratings(:,4));
xlabel('Index of city');
ylabel('Crime Rating');

%L2
for i = 1:329
       if ratings(i,4) == max(ratings(:,4))
          names(i,:)
       end;
end;

%Question 1 (||)
%L1
boxplot(ratings(:,2));
ylabel('Housing');

%L2
a = [ratings,group];
boxplot(a(:,2),a(:,10))

%Question 1 (|||)
%L1
parallelcoords(ratings, 'group', group, 'standardize', 'on');
ylabel('Ratings');

%L2
parallelcoords(ratings, 'group', group,'standardize', 'on','quantile',.25);
ylabel('Ratings');






