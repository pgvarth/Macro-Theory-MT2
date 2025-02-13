erandom=sqrt(0.01)*randn(1000,1)
for i=101:1000
   e(i-100)=erandom(i)
end



%constant expectations
a=1.5
un=0.05
m=0
for t=1:1:900
    pe(t)=0.01
end

for t=1:1:900
if t<10
  if t==1
   p(t)=m+0+e(t)

   u(t)=pe(t)/a-p(t)/a+un

  
  else
      p(t)=m+p(t-1)+e(t)

      u(t)=pe(t)/a-p(t)/a+un

     
  end

else 
    m=0.005
  p(t)=m+p(t-1)+e(t)

  u(t)=pe(t)/a-p(t)/a+un

  p(t)=m+p(t-1)+e(t)
end
end

t=1:1:900

f6=figure(6);
p1=plot(t,u(t),'LineWidth',2);
hold on

p2=plot(t,p(t),'LineWidth',2);
hold on
legend([p1 p2],{'unemployment','inflation'})
xlim([0 900])
title("Inflation and Unemployment under Constant Expectations")

xlabel("period")
ylabel("%")
%Static expectations 






for t=1:1:900
if t<10
    m=0
  if t==1
   p(t)=m+0+e(t)
   pe(t)=m

   u(t)=pe(t)/a-p(t)/a+un

  
  else
      p(t)=m+p(t-1)+e(t)
      
      pe(t)=p(t-1)

      u(t)=pe(t)/a-p(t)/a+un

     
  end

else

  m=0.005
  p(t)=m+p(t-1)+e(t)
  pe(t)=p(t-1)
  u(t)=pe(t)/a-p(t)/a+un
  

end
end

t=1:1:900

f7=figure(7);
p3=plot(t,u(t),'LineWidth',2);
hold on

p4=plot(t,p(t),'LineWidth',2);
hold on
legend([p3 p4],{'unemployment','inflation'})
xlim([0 900])
title("Inflation and Unemployment under Static Expectations ")

xlabel("period")
ylabel("%")

% Rational expectations 





for t=1:1:900
if t<10
    m=0
  if t==1
   p(t)=m+0+e(t)
   pe(t)=m

   u(t)=pe(t)/a-p(t)/a+un

  
  else
      p(t)=m+p(t-1)+e(t)
      
      pe(t)=p(t)

      u(t)=pe(t)/a-p(t)/a+un

     
  end

else 
    m=0.005
  p(t)=m+p(t-1)+e(t)
  pe(t)=p(t)
  u(t)=pe(t)/a-p(t)/a+un

end
end


t=1:1:900

f8=figure(8);
p5=plot(t,u(t),'LineWidth',2);
hold on

p6=plot(t,p(t),'LineWidth',2);
hold on
legend([p5 p6],{'unemployment','inflation'})
xlim([0 900])
title("Inflation and Unemployment under Rational Expectations ")

xlabel("period")
ylabel("%")