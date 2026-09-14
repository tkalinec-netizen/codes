function []=kyvadlo2()
%% Pohyb kyvadla
  clear; clc;

global C C2;

m=1;
J=10;
g=9.81;
l0=0.3; %delka dratu

C=m*g*l0/J;

omega=sqrt(C)
om=sqrt(g/l0)
t_konec=100; %s
%tlumeni kyvadla
T=0;
C2=T/J;

% pocatecni podminky
phi0=50/180*pi; % pocatecni uhel vychyleni
omega0=0; % pocatecni uhlova rychlost


%kyvadlo netlumene
options = odeset('RelTol',1e-7);
[t,y] = ode45(@kyvadlofce,[0 t_konec],[phi0 omega0],options);

y2=phi0*exp(-C2*t).*cos(omega*t);

figure(1)
plot(t,y(:,1)*180/pi,'r')
hold on
plot(t,y2*180/pi,'b--')
hold off
title('Netlumene kmity kyvadla','FontSize',13);
legend('presne reseni','linearizovane reseni');
xlabel('Cas t [s]');
ylabel('Uhlova vychylka [ ^o]');

%kyvadlo tlumene

%tlumeni kyvadla
T=0.5;
C2=T/J;


[t,y] = ode45(@kyvadlofce,[0 t_konec],[phi0 omega0],options);

vychylka=l0*y(:,1); % vychylka
r=y(:,2)*l0; %rychlost kyvani hm. bodu
y2=phi0*exp(-C2*t).*cos(omega*t);
[vychylka r];

figure(2)
subplot(2,2,1)
plot(t,y(:,1)*180/pi,'r')
hold on
plot(t,y2*180/pi,'b--')

hold off
title('Tlumene kmity kyvadla','FontSize',13);
legend('presne reseni','linearizovane reseni');
xlabel('Cas t [s]');
ylabel('Uhlova vychylka [ ^o]');

subplot(2,2,2)
plot(t,vychylka,'black')
xlabel('Cas t [s]');
ylabel('Vychylka [m]');
title('Tlumene kmity vychylka','FontSize',13);

subplot(2,2,3)
plot(t,r,'g')
xlabel('Cas t [s]');
ylabel('Rychlost [m/s]');
title('Rychlost','FontSize',13);


    function dy=kyvadlofce(t,y)

        dy=zeros(2,1);
        dy(1)=y(2);
        dy(2)=-C*sin(y(1))-C2*y(2);

    end
f3=figure(3)
set(f3,'MenuBar','none')
simulace(l0,y(:,1),t_konec)
end

