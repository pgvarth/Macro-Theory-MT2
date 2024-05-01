clear all
%Parameters
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
%Steady state

Dbar=Cbar+Ibar-c_MPC*Tbar+Gbar-b*ibar;
ybar=(Dbar)/(1-c_MPC-alpha);


yt45=linspace(0,16,100);
xlabel('$Y_{t-1}$', 'Interpreter', 'latex', 'FontSize', 14);
ylabel('$Y_{t}$', 'Interpreter', 'latex', 'FontSize', 14);
hold on
% 45 degrees

plot(yt45,yt45,'LineWidth',2)

% 
yt= Dbar + (alpha+c_MPC).*yt45;

hold on
plot(yt45,yt,'LineWidth',2,'LineStyle','--')
scatter(ybar,ybar,'o','filled')
%scatter(ybar*0.5,ybar*0.5,'o','filled','LineWidth',10)
legend('$Y_{t}=Y_{t-1}$','$Y_{t}=D_{t}$','Equilibrium','Interpreter', 'latex', 'FontSize', 14)

grid on

%%
% Short run equilibrium and dynamics
alpha=0.1;
c_MPC=[0.6;0.7;0.8];

Dbar=Cbar+Ibar-c_MPC*Tbar+Gbar-b*ibar;
ybar=(Dbar)./(1-c_MPC-alpha);





for ii=1:3
    yt=ybar(ii)*0.9;
       
for j=1:15
yt(j+1) = Dbar(ii) + (alpha+c_MPC(ii))*yt(j);
end


figure (2)
plot((yt./yt(1)-1).*100)
hold on
grid on
legend(strcat('$\alpha$+$c$=', num2str(alpha+c_MPC)), 'Interpreter', 'latex', 'FontSize', 14)
xlabel('Horizon')
title('$Y_{t}$ as $\%$ deviation from $Y_{-1}$', 'Interpreter', 'latex', 'FontSize', 14)
end
