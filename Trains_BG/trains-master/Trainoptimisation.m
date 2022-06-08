testmatrix = A

% Number of stations per train
number_stations = ones(length(testmatrix))
% Number of trains per cycle
number_stations_t = number_stations + number_stations'
% Initialise
testmatrix_update = testmatrix;
eigenvalue_vec = []
stations_vec = []
for i = 1:100
circuits = testmatrix+testmatrix';
% Divide by number of trains
circuit_ptrain = circuits./number_stations_t;
% Find max circuit
[max_num] = max(circuits(:));
% Find and store the value and position of eigenvalue
[eigenvalue] = max(circuit_ptrain(:))
eigenvalue_vec = [eigenvalue_vec; eigenvalue];
[row, col] = find(ismember(circuit_ptrain, max(circuit_ptrain(:))));

% If more than one option for max value, locate the specific critical
% circuit
L = length(row);
if L>1
    vec = [zeros(length(row),1)];
    for ii = 1:length(row)
        vec(ii) = testmatrix_update(row(ii),col(ii));
    end
         [val, idx] = max(vec);
    row = row(idx);
    col = col(idx);
end

% Add a train to the critical circuit; this alters the test matrix and no.
% of stations
testmatrix_update(row,col) = testmatrix_update(row,col)*number_stations(row,col)/(number_stations(row,col)+1);
number_stations(row,col) = number_stations(row,col)+1;
stations = sum(sum(number_stations));
stations_vec = [stations_vec; stations];
number_stations_t = number_stations + number_stations';
end

% Plot adjacency matrix
G2 = digraph(testmatrix)
figure(1)
plot(G2)
figure(2)
plot(eigenvalue_vec,stations_vec)