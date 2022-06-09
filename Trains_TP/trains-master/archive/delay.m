function output = delay(AdMat,t_d, rho)
% AdMat: adjacency matrix; 
% t_d: initial delay
% rho: traffic rate


[lambda,v] = maxeig(AdMat);
s = size(v,1);
%T = ceil(lambda/5)*5;           %planned departure time (in 5 mins) 
T = lambda/rho;

%delay on any node of the critical circuit
f = critCircuit(AdMat);
critical_node=f(1,1);

% planned and real departure time
d0 = v;                               %planned departure time
x0 = v + eye(s,critical_node)*t_d;    %departure time (lambda+delay)


% finding when the delay goes out of the system
k = 0;
x = x0;
while k<=1000
    k = k+1;
    d = d0 + k*T;                       %(k+1)th planned departure timee
    x = max(maxmult(AdMat,x),d);        %x(k+1) = max(Ax(k),d(k+1))
    del_trains = sum(x>d);              %number of delayed trains
    
    if del_trains == 0
        output = k;
        break
    elseif k == 1000
        output = 'Delay does not go out of the system in 1000 steps.';
    end   

end

end

