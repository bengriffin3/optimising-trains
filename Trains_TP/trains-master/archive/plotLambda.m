tic
%dist1 = singDist;
%dist2 = lonDist;
%dist3 = chengduDist;
%dist4 = rottDist;
dist5 = nyDist;
%sing = lambda(dist1);
%lond = lambda(dist2);
%chengdu = lambda(dist3);
%rott = lambda(dist4);
ny = lambda(dist5);
for i = 1:50
    hold on
    %dist1 = addTrain(dist1);
    %dist2 = addTrain(dist2);
    %dist3 = addTrain(dist3);
    %dist4 = addTrain(dist4);
    dist5 = addTrain(dist5);
    %sing = [sing lambda(dist1)];
    %lond = [lond lambda(dist2)];
    %chengdu = [chengdu lambda(dist3)];
    %rott = [rott lambda(dist4)];
    ny = [ny lambda(dist5)];
%     plot(1:1:i+1,sing,'r')
%     hold on
%     plot(1:1:i+1,lond,'b')
%     legend('singapore','london')    
%     pause
end
figure(1)
%plot(1:1:21,sing,'r')
hold on
%plot(1:1:21,lond,'b')
%plot(1:1:21,chengdu,'g')
%plot(1:1:21,rott,'k')
plot(1:1:101,ny,'y')
legend('singapore','london','chengdu','rotterdam','central ny')
title('lambda vs. #stations added')

% figure(2)
% sing = sing./lambda(singDist);
% lond = lond./lambda(lonDist);
% chengdu = chengdu./lambda(chengduDist);
% rott = rott./lambda(rottDist);
% ny = ny./lambda(nyDist);
% plot(1:1:21,sing,'r')
% hold on
% plot(1:1:21,lond,'b')
% plot(1:1:21,chengdu,'g')
% plot(1:1:21,rott,'k')
% plot(1:1:21,ny,'y')
% legend('singapore','london','chengdu','rotterdam','central ny')
% title('scaled lambda vs. #stations added')
toc
