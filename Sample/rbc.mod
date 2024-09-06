% Basic RBC Model
%–––––––––––––––––––––-
% 0. Housekeeping (close all graphic windows)
%–––––––––––––––––––––-
%close all;
%–––––––––––––––––––––-
% 1. Defining variables
%–––––––––––––––––––––-
var y c k n a;
varexo z;
parameters beta chi delta alpha rho sigma;
%–––––––––––––––––––––-
% 2. Calibration
%–––––––––––––––––––––-
alpha = 0.4; %0.33;
beta = 0.95; %0.99;
delta = 0.1; %0.025;
chi = 2;
rho = 0.95;
sigma = 1; %2;

%–––––––––––––––––––––-
% Load External Parameters (for loops)
%–––––––––––––––––––––-
%load rho;
%set_param_value('rho',rho);
%load sigma;
%set_param_value('sigma',sigma);

%–––––––––––––––––––––-
% 3. Model
%–––––––––––––––––––––-
model;
exp(c)^-sigma = beta*exp(c(+1))^-sigma*(alpha*exp(a(+1))*exp(k)^(alpha-1)*exp(n(+1))^(1-alpha)+1-delta);
chi = exp(c)^-sigma*(1-alpha)*exp(a)*exp(k(-1))^alpha*exp(n)^-alpha;
exp(c)+exp(k) = exp(a)*exp(k(-1))^alpha*exp(n)^(1-alpha)+(1-delta)*exp(k(-1));
exp(y) = exp(a)*exp(k(-1))^alpha*exp(n)^(1-alpha);
a = rho*a(-1)+z;
end;
%–––––––––––––––––––––-
% 4. Computation
%–––––––––––––––––––––-
initval;
k = log(2);
c = log(0.5);
n = log(0.3);
a = 0;
z = 0;
end;
shocks;
var z = 1;
end;
check;
steady;
stoch_simul(order = 1, irf=50);
%stoch_simul(order = 1, irf=40, nograph) y c k n a;












