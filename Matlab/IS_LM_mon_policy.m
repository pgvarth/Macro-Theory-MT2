clear all
%Structural parameters

alpha=0.1; % Marginal propensity to invest
c_MPC=0.5;  % Marginal propensity to consume
b=0.5;
ibar=0.04;


%Autonomous expenses

Cbar=0.6;
Ibar=0.2;

% Fiscal policy
Gbar=1.7;
Tbar=1.7;


%% Model
%Dynamic IS
% Steady state

Dbar=Cbar+Ibar-c_MPC*Tbar+Gbar-b*ibar;
y0=(Dbar)/(1-c_MPC-alpha);



yt45=linspace(0,16,1000);

% 45 degrees
plot(yt45,yt45)
yt= Dbar + (alpha+c_MPC).*yt45;

hold on
plot(yt45,yt,'LineWidth',2,'LineStyle','--')
grid on
scatter(y0,y0,'o','filled')

xlabel('$Y_{t-1}$', 'Interpreter', 'latex', 'FontSize', 14);
ylabel('$Y_{t}$', 'Interpreter', 'latex', 'FontSize', 14);


%%
% New Steady state

% Exogenous increase in nominal interest rate
ibar=ibar+0.01;  

Dbar=Cbar+Ibar-c_MPC*Tbar+Gbar-b*ibar;
ybar=(Dbar)/(1-c_MPC-alpha);


yt45=linspace(0,16,100);
yt= Dbar + (alpha+c_MPC).*yt45;
hold on
plot(yt45,yt,'LineWidth',2,'LineStyle','--')
scatter(ybar,ybar,'o','filled')

legend('$Y_{t}=Y_{t-1}$','$Y_{t,0}=D_{t,0}$','Equilibrium 0','$Y_{t,1}=D_{t,1}$','Equilibrium 1','Interpreter', 'latex', 'FontSize', 14)
title('Monetary Policy $i$','Interpreter', 'latex', 'FontSize', 14)


%%
% Short run equilibrium and dynamics



Dbar=Cbar+Ibar-c_MPC*Tbar+Gbar-b*ibar;

gamma=0.7;




yt=y0;
C(1)=Cbar+c_MPC*(y0-Tbar);
I(1)=Ibar+alpha*y0 -b*ibar;
L(1)=gamma*y0;
for j=1:20
yt(j+1) = Dbar + (alpha+c_MPC)*yt(j);
L(j+1)=gamma*yt(j);
C(j+1)=Cbar+c_MPC*(yt(j)-Tbar);
I(j+1)=Ibar+alpha*(yt(j)) -b*ibar;
end


figure (2)
subplot(2,2,1)
plot((yt./yt(1)-1).*100)
hold on
grid on
xlabel('Horizon')
title('Output $Y_{t}$','Interpreter', 'latex', 'FontSize', 14)
subplot(2,2,2)
plot((C./C(1)-1).*100)
hold on
grid on
xlabel('Horizon')
title('Consumption $C_{t}$','Interpreter', 'latex', 'FontSize', 14)
subplot(2,2,3)
plot((I./I(1)-1).*100)
hold on
grid on
xlabel('Horizon')
title('Investment $I_{t}$','Interpreter', 'latex', 'FontSize', 14)
subplot(2,2,4)
plot((L./L(1)-1).*100)
hold on
grid on
xlabel('Horizon')
title('Labour $L_{t}$','Interpreter', 'latex', 'FontSize', 14)


