function f = critCircuit(matrix)

% Function which takes a distance matrix as an input,
% and outputs a list of the critical circuit(s) in the following form:
% [starting node, lambda, length of circuit]

critCircuits = [];
for p = 1:size(matrix,2)
    A = (1/p)*maxplusMP(matrix,p);
    d = diag(A);
    m = max(d);
    for r = 1:length(d)
        if abs(d(r)- m)<10e-10
            critCircuits = [critCircuits; r, m, p];
        end
    end
end
%Extract only the circuits with maximum weight
maxWeight = max(critCircuits(:,2));
critCircuits(abs(critCircuits(:,2)-maxWeight)>10e-10,:) = [];
f = critCircuits;
end
    