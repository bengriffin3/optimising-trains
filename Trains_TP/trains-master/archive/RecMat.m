function R = RecMat(A,T,d)
% Recovery matrix given adjacency matrix A, interdeparture time T and
% initial timetable d (mx1-vector)

M   = KleeneMP(A-T);
R   = d - d' - M;

end