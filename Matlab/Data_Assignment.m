%%
%
clear all;

% Load matrices
load('GDP_data')


%%
% Create a plot of Nominal and Real GDP for EA 
% Base year 2015


yyears = 1995:1:2022;
figure(1)
plot(yyears, nominal_gdp(:, 1) / 1e6, 'LineWidth', 2); 
hold on
plot(yyears, real_gdp(:, 1) / 1e6, 'LineWidth', 2); 
grid on
ylabel('\fontsize{14}{20}\selectfont GDP (in Millions)', 'Interpreter', 'latex', 'FontSize', 14);



% Add a vertical line at 2015
xline(2015, 'k--', {'Base Year = 2015'}, 'LineWidth', 2); 
title('\fontsize{14}{20}\selectfont Euro Area', 'Interpreter', 'latex', 'FontSize', 14);
legend('Nominal GDP', 'Real GDP', 'Location', 'northwest');

saveas(gcf, 'GDP_EA.png');

%%
% Create a plot of Nominal and Real GDP for Greece 
% Base year 2015

yyears = 1995:1:2022;
figure (2)
plot(yyears, nominal_gdp(:, 2) / 1e6, 'LineWidth', 2); 
hold on
plot(yyears, real_gdp(:, 2) / 1e6, 'LineWidth', 2); 
grid on
ylabel('\fontsize{14}{20}\selectfont GDP (in Millions)', 'Interpreter', 'latex', 'FontSize', 14);

% Add a vertical line at 2015
xline(2015, 'k--', {'Base Year = 2015'}, 'LineWidth', 2); 
title('\fontsize{14}{20}\selectfont Greece', 'Interpreter', 'latex', 'FontSize', 14);
legend('Nominal GDP', 'Real GDP', 'Location', 'northwest');
saveas(gcf, 'GDP_Greece.png');

%%
%
% Compute GDP deflators 
gdp_deflator = (nominal_gdp ./ real_gdp) * 100;

% Plot GDP deflator for EA
figure(3)
plot(yyears, gdp_deflator(:,1), 'LineWidth', 2);
grid on;
xlabel('Year');
ylabel('GDP Deflator');

% Find the index of the year where the GDP deflator is 100 (base year)
base_year_index = find(gdp_deflator(:,1) == 100);

% Display the base year
base_year = yyears(base_year_index);
disp(['Base Year: ', num2str(base_year)]);

% Add a vertical line at the base year
xline(base_year, 'k--', {'Base Year'}, 'LineWidth', 2);
title('\textbf{\fontsize{14}{20}\selectfont Euro Area}', 'Interpreter', 'latex');
saveas(gcf, 'GDP_Deflator_EA.png');

%%
% Plot GDP deflator for Greece
figure(4)
plot(yyears, gdp_deflator(:,2), 'LineWidth', 2);
grid on;
xlabel('Year');
ylabel('GDP Deflator');

% Find the index of the year where the GDP deflator is 100 (base year)
base_year_index = find(gdp_deflator(:,2) == 100);

% Display the base year
base_year = yyears(base_year_index);
disp(['Base Year: ', num2str(base_year)]);

% Add a vertical line at the base year
xline(base_year, 'k--', {'Base Year'}, 'LineWidth', 2);
title('\textbf{\fontsize{14}{20}\selectfont Greece}', 'Interpreter', 'latex');
saveas(gcf, 'GDP_Deflator_Greece.png');
%%
years = 1995:2022;  

% Taking logs
log_real_gdp = log(real_gdp);
log_gdp_deflator = log(gdp_deflator);
log_nominal_gdp = log(nominal_gdp);

% Compute growth rates of real GDP, GDP deflator and nominal GDP
growth_rate_real_gdp = diff(log_real_gdp(:, 1)) * 100;
growth_rate_gdp_deflator = diff(log_gdp_deflator(:, 1)) * 100;
growth_rate_nominal_gdp=diff(log_nominal_gdp(:, 1)) * 100;

% Compute nominal GDP growth by summing real GDP growth and GDP deflator growth
nominal_gdp_growth = growth_rate_real_gdp + growth_rate_gdp_deflator;

% Compare the growth rate of nominal GDP and its decomposition
DIST=abs(growth_rate_nominal_gdp-nominal_gdp_growth);
if min(DIST)>10^(-9)
    display('Error in your computations, growth rate and decomposition mismacth')
end
%%

% Plot the decomposed growth rates
figure(5)
subplot(3, 1, 1);
plot(years(2:end), nominal_gdp_growth, 'LineWidth', 2);
hold on;
yline(0, 'k--', 'LineWidth', 2); 
grid on;
xlabel('\textbf{Year}', 'Interpreter', 'latex');
ylabel('\textbf{(\%)}', 'Interpreter', 'latex');
title('\textbf{Nominal GDP Growth}', 'Interpreter', 'latex');

subplot(3, 1, 2);
plot(years(2:end), growth_rate_real_gdp, 'LineWidth', 2);
hold on;
yline(0, 'k--', 'LineWidth', 2); 
grid on;
xlabel('\textbf{Year}', 'Interpreter', 'latex');
ylabel('\textbf{(\%)}', 'Interpreter', 'latex');
title('\textbf{Real GDP Growth}', 'Interpreter', 'latex');

subplot(3, 1, 3);
plot(years(2:end), growth_rate_gdp_deflator, 'LineWidth', 2);
hold on;
yline(0, 'k--','LineWidth', 2); 
grid on;
xlabel('\textbf{Year}', 'Interpreter', 'latex');
ylabel('\textbf{(\%)}', 'Interpreter', 'latex');
title('\textbf{GDP Deflator Growth}', 'Interpreter', 'latex');

sgtitle('\textbf{Decomposition of Nominal GDP Growth in EA}', 'Interpreter', 'latex');
saveas(gcf, 'Growth_rates_EA.png');

%%

growth_rate_real_gdp = diff(log_real_gdp(:, 2)) * 100;
growth_rate_gdp_deflator = diff(log_gdp_deflator(:, 2)) * 100;

% Compute nominal GDP growth by summing real GDP growth and GDP deflator growth
nominal_gdp_growth = growth_rate_real_gdp + growth_rate_gdp_deflator;

% Plot the decomposed growth rates for Greece
figure(6)
subplot(3, 1, 1);
plot(years(2:end), nominal_gdp_growth, 'LineWidth', 2);
hold on;
yline(0, 'k--', 'LineWidth', 2); 
grid on;
xlabel('\textbf{Year}', 'Interpreter', 'latex');
ylabel('\textbf{(\%)}', 'Interpreter', 'latex');
title('\textbf{Nominal GDP Growth}', 'Interpreter', 'latex');

subplot(3, 1, 2);
plot(years(2:end), growth_rate_real_gdp, 'LineWidth', 2);
hold on;
yline(0, 'k--', 'LineWidth', 2); 
grid on;
xlabel('\textbf{Year}', 'Interpreter', 'latex');
ylabel('\textbf{(\%)}', 'Interpreter', 'latex');
title('\textbf{Real GDP Growth}', 'Interpreter', 'latex');

subplot(3, 1, 3);
plot(years(2:end), growth_rate_gdp_deflator, 'LineWidth', 2);
hold on;
yline(0, 'k--','LineWidth', 2); 
grid on;
xlabel('\textbf{Year}', 'Interpreter', 'latex');
ylabel('\textbf{(\%)}', 'Interpreter', 'latex');
title('\textbf{GDP Deflator Growth}', 'Interpreter', 'latex');

sgtitle('\textbf{Decomposition of Nominal GDP Growth in Greece}', 'Interpreter', 'latex');
saveas(gcf, 'Growth_rates_Greece.png');

%%
% Plot the decomposition of nominal GDP growth into its components using stacked bars
% For EA
growth_rate_real_gdp = diff(log_real_gdp(:, 1)) * 100;
growth_rate_gdp_deflator = diff(log_gdp_deflator(:, 1)) * 100;

% Compute nominal GDP growth by summing real GDP growth and GDP deflator growth
nominal_gdp_growth = growth_rate_real_gdp + growth_rate_gdp_deflator;


figure(7);
bar(years(2:end), [growth_rate_real_gdp(:,1), growth_rate_gdp_deflator(:,1)], 'stacked', 'LineWidth', 1.5);
hold on;
plot(years(2:end), growth_rate_nominal_gdp(:,1), 'k-', 'LineWidth', 2);  
xlabel('\textbf{Year}', 'Interpreter', 'latex', 'FontSize', 14);
ylabel('\textbf{Growth Rate (\%)}', 'Interpreter', 'latex', 'FontSize', 14);
title('\textbf{EA Nominal GDP Decomposition}', 'Interpreter', 'latex', 'FontSize', 14);
legend({'\textbf{Real GDP Growth}', '\textbf{GDP Deflator Growth}', '\textbf{Nominal GDP Growth}'}, ...
    'Location', 'southwest', 'Interpreter', 'latex', 'FontSize', 10);

grid on;
saveas(gcf, 'GDP_Decomposition_EA.png');

%%

% Plot the decomposition of nominal GDP growth into its components using stacked bars
% For Greece
growth_rate_real_gdp = diff(log_real_gdp(:, 2)) * 100;
growth_rate_gdp_deflator = diff(log_gdp_deflator(:, 2)) * 100;

% Compute nominal GDP growth by summing real GDP growth and GDP deflator growth
nominal_gdp_growth = growth_rate_real_gdp + growth_rate_gdp_deflator;


figure(8);
bar(years(2:end), [growth_rate_real_gdp, growth_rate_gdp_deflator], 'stacked', 'LineWidth', 1.5);
hold on;
plot(years(2:end), nominal_gdp_growth, 'k-', 'LineWidth', 2);  
xlabel('\textbf{Year}', 'Interpreter', 'latex', 'FontSize', 14);
ylabel('\textbf{Growth Rate (\%)}', 'Interpreter', 'latex', 'FontSize', 14);
title('\textbf{Greece Nominal GDP Decomposition}', 'Interpreter', 'latex', 'FontSize', 14);
legend({'\textbf{Real GDP Growth}', '\textbf{GDP Deflator Growth}', '\textbf{Nominal GDP Growth}'}, ...
    'Location', 'southwest', 'Interpreter', 'latex', 'FontSize', 10);
grid on;
saveas(gcf, 'GDP_Decomposition_Greece.png');
