%question 1%
fileID = fopen('customers.csv');

C = textscan(fileID,'%s %s %s %s %s %s %s',...
'Delimiter',',','EmptyValue',-Inf);
fclose(fileID);

Lastname = C{4};
Dist = zeros(401,401);
for i = 2:401
    for ii = 2:401
        Dist(i,ii) = Edit_Dist(Lastname{i,1},Lastname{ii,1});
    end;
end;

%question 2%

customerid = C{1};
fid=fopen('MP3.xyang105.txt','wt');
for i = 2:401
    
    fprintf(fid,'%s\t',customerid{i,1});
    for ii = 2:401
        if Dist(i,ii) < 3 && Dist(i,ii)~=0
            fprintf(fid,'%s\t',customerid{ii,1});
        end;
    end;
    fprintf(fid,'\n');
end;
fclose(fid);