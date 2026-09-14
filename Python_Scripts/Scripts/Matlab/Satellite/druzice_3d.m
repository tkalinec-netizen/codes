function [sx,sy,sz]=druzice_3d
clc

m_zeme=5.9736e24; % kg    
m=83; % kg
k=6.672e-11; % N*m^2*kg^-2
t_konec=1.2e4; % cas vypoctu
povrch_zeme=6378e3; % m
% Pocatecni podminky
r0=povrch_zeme+250e3; %m
v0=7.8e3; %m/s
theta_s=0; %deg
phi_s=65; %deg
theta_v=90; %deg
phi_v=0; %deg

%prevod souradnic
[sx0, sy0, sz0]=sph2cart(theta_s*pi/180, phi_s*pi/180, r0);
[vx0, vy0, vz0]=sph2cart(theta_v*pi/180, phi_v*pi/180, v0);
% Soustava diferencialnich rovnic popisujici pohyb
%dx/dt=vx
%dy/dt=vy
%dy/dt=dz
%vx/dt=-Fg/m*cos(theta)*cos(phi)
%vy/dt=-Fg/m*sin(theta)*cos(phi)
%vz/dt=-Fg/m*sin(phi)
    function dsv=dif_rce(~,sv)
        dsv=zeros(6,1);
        [theta,phi,r]=cart2sph(sv(1),sv(2),sv(3));
        Fg=k*m_zeme*m/r^2;
        dsv(1)=sv(4);
        dsv(2)=sv(5);
        dsv(3)=sv(6);
        dsv(4)=-Fg/m*cos(theta)*cos(phi);
        dsv(5)=-Fg/m*sin(theta)*cos(phi);
        dsv(6)=-Fg/m*sin(phi);
    end 
%reseni diferencialnich rovnic
rel_tol=1e-8;
abs_tol=1e-8;
options=odeset('RelTol',rel_tol,'AbsTol',[abs_tol abs_tol abs_tol abs_tol...
    abs_tol abs_tol]);
[t,Y]=ode45(@dif_rce,[0 t_konec],[sx0,sy0,sz0,vx0,vy0,vz0],options);
% Prevod na fyzikalni veliciny
sx=Y(:,1);sy=Y(:,2);sz=Y(:,3);
vx=Y(:,4);vy=Y(:,5);vz=Y(:,6);
%Korekce vypoctu pro pohyblivou zemi
[theta,phi,r]=cart2sph(sx,sy,sz);
theta=theta-7.29e-5.*t;
[sx,sy,sz]=sph2cart(theta,phi,r);
% graf ve 3d
fig1=figure;
hold on;
axis equal;
% Zeme
[xm,ym,zm]=sphere(24);
mesh(xm*povrch_zeme/1000,ym*povrch_zeme/1000,zm*povrch_zeme/1000,'EdgeColor'...
    ,[0 0 1],'FaceColor',[0 1 1]);
%rovnik a greenwichsky polednik

tp=linspace(0,2*pi,100);
plot3(povrch_zeme/1000*cos(tp),povrch_zeme/1000*sin(tp),zeros(length(tp)),...
    'k','LineWidth',1.5);

plot3(povrch_zeme/1000*sin(tp),zeros(length(tp)),povrch_zeme/1000*cos(tp),...
    '--k','LineWidth',1.5);
% misto startu druzice
plot3(sx0/1000,sy0/1000,sz0/1000,'.r','MarkerSize',30);
view(127.5,30);
%plot3(sx/1000,sy/1000,sz/1000,'r','LineWidth',1.5);
title('Trajektorie pohybu družice','Color',[1 1 1]);
%xlabel('x (km)','Color',[1 1 1]);ylabel('y (km)','Color',[1 1 1]);
%zlabel('z (km)','Color',[1 1 1]);

%Zavislost phi na case
figure;
[theta,phi,r]=cart2sph(sx,sy,sz);
plot(t/60,phi*180/pi);
grid on;
xlabel('t (min)');ylabel('phi (deg)');
title('Trajektorie pohybu družice');

figure(fig1);
set(fig1,'Color',[0 0 0]);
set(gca,'Color',[0 0 0]);
nframe=123;
mov(1:nframe)=struct('cdata',[],'colormap',[]);
for i=1:nframe
    %t=0:t_konec/(nframe-1):t_konec;
    hold on
    plot3(sx(1:i*7)/1000,sy(1:i*7)/1000,sz(1:i*7)/1000,'r','LineWidth',1.5);
    length(sx);
    pause(0.1)
    mov=getframe(gcf)
end

end