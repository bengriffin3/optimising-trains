function f = addTrain(matrix)

% Function which takes as input a network matrix
% Finds the critical circuit of shortest length
% Finds longest track in that circuit
% Adds a train to that track
% Returns matrix of new network

cC = critCircuit(matrix);
L = cC(1,3);
W = cC(1,2)*L;
cC(abs(cC(:,3)-L)>10e-10,:) = [];
disp('lambda before')
disp(cC(1,2))
nodes = nchoosek(cC(:,1),L);
paths = [];
for r = 1:size(nodes,1)
    paths = [paths; perms(nodes(r,:))];
end
delete = [];
for r = 1:size(paths,1)
    wght = matrix(paths(r,1),paths(r,size(paths,2)));
    for s = 1:(size(paths,2)-1)
        wght = wght + matrix(paths(r,s+1),paths(r,s));
    end
    
    if (abs(wght-W)>10e-10)
        delete = [delete; r];
    end
end
paths(delete(1:end),:) = [];

paths = paths(1,:);
weights = [];
for t = 1:length(paths)-1
    weights = [weights matrix(paths(t+1),paths(t))];
end
weights = [weights matrix(paths(1),paths(end))];
w = max(weights);
weights(abs(weights - w)>10e-10) = 0;
tr = find(weights);
tr = tr(1);
paths = circshift(paths,-tr + 1);
track = [paths(1),paths(2)];
matrix(paths(2),paths(1));
    
A = -Inf*ones(size(matrix,1)+1);
A(1:size(matrix,1),1:size(matrix,1)) = matrix;
A(track(2),size(A,1)) = w;
A(size(A,1),track(1)) = 0;
A(track(2),track(1)) = -Inf;
A(size(A,1),size(A,2)) = -Inf;

f = round(A);
cC = critCircuit(f);

disp('lambda after')
disp(cC(1,2))

end
