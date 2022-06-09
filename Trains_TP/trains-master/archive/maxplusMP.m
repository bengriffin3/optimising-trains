function f = maxplusMP(matrix,power)

% Code which computes the k'th max plus power of a matrix

if size(matrix,1) ~= size(matrix,2)
    error('Matrix is not square')
end

if power == 1
    f = matrix;
elseif power == 0
    f = eye(size(matrix,1));
    f(f==0) = -Inf;
    f(f==1) = 0;
else
f = matrix;    
    for p = 2:power
        ff = zeros(size(matrix));
        for i = 1:size(matrix,1)
            for j = 1:size(matrix,2)
                entry = zeros(size(matrix,2),1);
                for r = 1:size(matrix,1)
                    entry(r) = matrix(i,r) + f(r,j);
                end
                ff(i,j) = max(entry);
            end
        end
        f = ff;
    end
end
   
end