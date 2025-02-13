%Constant expectations
a=1.5
un=0.05
m=0
for t=1:1:20
    pe(t)=0.2
    e(t)=0
end

for t=1:1:20
if t<10
  if t==1
   p(t)=m+m+e(t)

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


figure (3001)
sgtitle("Constant Expectations")
t=1:1:20;
subplot(1,2,1)
plot(t,p(t))
title("Inflation")
xlabel("period")
ylabel("%")
xline(0)
grid on
t=1:1:20
subplot(1,2,2)
plot(t,u(t))
title("Unemployment")
xlabel("period")
ylabel("%")
xline(0)


%Static expectations 



for t=1:1:20
  
    e(t)=0
end


for t=1:1:20
if t<10
    m=0
  if t==1
   p(t)=m+m+e(t)
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
figure(3002)
sgtitle("Static Expectations")
t=1:1:20;
subplot(1,2,1)
plot(t,p(t))
title("Inflation")
xlabel("period")
ylabel("%")
xline(0)
grid on
t=1:1:20
subplot(1,2,2)
plot(t,u(t))
title("Unemployment")
xlabel("period")
ylabel("%")
xline(0)

% Rational expectations 


for t=1:1:20
  
    e(t)=0
end


for t=1:1:20
if t<10
    m=0
  if t==1
   p(t)=m+m+e(t)
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

figure(3003)
sgtitle("Rational Expectations")
t=1:1:20;
subplot(1,2,1)
plot(t,p(t))
title("Inflation")
xlabel("period")
ylabel("%")
xline(0)
grid on
subplot(1,2,2)
plot(t,u(t))
title("Unemployment")
xlabel("period")
ylabel("%")
xline(0)