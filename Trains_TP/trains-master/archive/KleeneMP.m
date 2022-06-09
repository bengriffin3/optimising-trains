function output = KleeneMP(A,kleene)
% calculates [A]+ in MaxPlus algebra or Kleenestar 
% returns kleene star operation if input is 2
  
Ak      = maxmult(A,A);
output  = max(Ak,A);

while Ak ~= A
    Ak      = maxmult(A,Ak);
    output  = max(Ak,output);
end

if nargin == 2
    E                           = -Inf*ones(size(A));         %identity matrix
    E(boolean(eye(size(E))))    = 0;
    output                      = max(output,E);
end


end
