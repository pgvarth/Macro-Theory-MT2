clear all;
rhos = [0.2,0.5,0.9];
results = struct;
for i=1:length(rhos)
    rho=rhos(i);
    save rho;
    dynare rbc noclearall;
    results.(sprintf('rho%d',i)) = oo_;
end


%Plotting every variable in one graph
figure;
for j=1:length(var_list_)
    subplot(3,2,j);
    for i=1:length(rhos)
        plot(results.(sprintf('rho%d',i)).irfs.(sprintf('%s_z',char(var_list_(j)))));
        hold on;
        title(sprintf('%s_z',char(var_list_(j))));
    end
    legend(strcat('rho = ',string(rhos)));
    hold on;
    legend;
end

%Single variable plotting
%figure; 
%plot(results.rho1.irfs.y_z);
%hold on;
%plot(results.rho2.irfs.y_z);
%hold on;
%plot(results.rho3.irfs.y_z);
%title('Output');

