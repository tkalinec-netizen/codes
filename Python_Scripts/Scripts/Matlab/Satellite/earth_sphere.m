function [xx,yy,zz] = earth_sphere(varargin)
%EARTH_SPHERE Generate an earth-sized sphere.
%   [X,Y,Z] = EARTH_SPHERE(N) generates three (N+1)-by-(N+1)
%   matrices so that SURFACE(X,Y,Z) produces a sphere equal to 
%   the radius of the earth in kilometers. The continents will be
%   displayed.
%
%   [X,Y,Z] = EARTH_SPHERE uses N = 50.
%
%   EARTH_SPHERE(N) and just EARTH_SPHERE graph the earth as a 
%   SURFACE and do not return anything.
%
%   EARTH_SPHERE(N,'mile') graphs the earth with miles as the unit rather
%   than kilometers. Other valid inputs are 'ft' 'm' 'nm' 'miles' and 'AU'
%   for feet, meters, nautical miles, miles, and astronomical units
%   respectively.
%
%   EARTH_SPHERE(AX,...) plots into AX instead of GCA.
% 
%  Examples: 
%    earth_sphere('nm') produces an earth-sized sphere in nautical miles
%
%    earth_sphere(10,'AU') produces 10 point mesh of the Earth in
%    astronomical units
%
%    h1 = gca;
%    earth_sphere(h1,'mile')
%    hold on
%    plot3(x,y,z)
%      produces the Earth in miles on axis h1 and plots a trajectory from
%      variables x, y, and z

%   Copyright 1984-2010 The MathWorks, Inc. 

%% Input Handling
[cax,args,nargs] = axescheck(varargin{:}); % Parse possible Axes input
error(nargchk(0,2,nargs)); % Ensure there are a valid number of inputs
clc

% Handle remaining inputs.
% Should have 0 or 1 string input, 0 or 1 numeric input
j = 0;
k = 0;
kk=6.672e-11; % N*m^2*kg^-2
n = 50; % default value
units = 'km'; % default value
m_earth=5.9736e24;
m=83; 
v0=7.8e3; %m/s
theta_s=0; %deg
phi_s=55; %deg
theta_v=90; %deg
phi_v=0; %deg
t_konec=1.24e4;

for i = 1:nargs
    if ischar(args{i})
        units = args{i};
        j = j+1;
    elseif isnumeric(args{i})
        n = args{i};
        k = k+1;
    end
end

if j > 1 || k > 1
    error('Invalid input types')
end

%% Calculations

% Scale factors
Scale = {'km' 'm'  'mile'            'miles'           'nm'              'au'                 'ft';
         1    1000 0.621371192237334 0.621371192237334 0.539956803455724 6.6845871226706e-009 3280.839895};

% Identify which scale to use
try
    myscale = 6378.1363*Scale{2,strcmpi(Scale(1,:),units)};
    r0=myscale+250; %km
catch %#ok<*CTCH>
    error('Invalid units requested. Please use m, km, ft, mile, miles, nm, or AU')
end
[sx0, sy0, sz0]=sph2cart(theta_s*pi/180, phi_s*pi/180, r0*1000);

[vx0, vy0, vz0]=sph2cart(theta_v*pi/180, phi_v*pi/180, v0);     
% -pi <= theta <= pi is a row vector.
% -pi/2 <= phi <= pi/2 is a column vector.
theta = (-n:2:n)/n*pi;
phi = (-n:2:n)'/n*pi/2;
cosphi = cos(phi); cosphi(1) = 0; cosphi(n+1) = 0;
sintheta = sin(theta); sintheta(1) = 0; sintheta(n+1) = 0;

x = myscale*cosphi*cos(theta);
y = myscale*cosphi*sintheta;
z = myscale*sin(phi)*ones(1,n+1);

rel_tol=1e-8;
abs_tol=1e-8;
options=odeset('RelTol',rel_tol,'AbsTol',[abs_tol abs_tol abs_tol abs_tol...
    abs_tol abs_tol]);
[t,Y]=ode45(@dif_rce,[0 t_konec],[sx0,sy0,sz0,vx0,vy0,vz0],options);

% Scaling to the physical quantities
sx=Y(:,1);sy=Y(:,2);sz=Y(:,3);

% Correction calculations for the floating earth
[th,ph,r]=cart2sph(sx,sy,sz);
th=th-7.29e-5.*t;
[sx,sy,sz]=sph2cart(th,ph,r);

%% Plotting

if nargout == 0
    cax = newplot(cax);

    % Load and define topographic data
    load('topo.mat','topo','topomap1');

    % Rotate data to be consistent with the Earth-Centered-Earth-Fixed
    % coordinate conventions. X axis goes through the prime meridian.
    % http://en.wikipedia.org/wiki/Geodetic_system#Earth_Centred_Earth_Fixed_.28ECEF_or_ECF.29_coordinates
    %
    % Note that if you plot orbit trajectories in the Earth-Centered-
    % Inertial, the orientation of the contintents will be misleading.
    topo2 = [topo(:,181:360) topo(:,1:180)]; %#ok<NODEF>
    
    % Define surface settings
    props.FaceColor= 'texture';
    props.EdgeColor = 'none';
    props.FaceLighting = 'phong';
    props.Cdata = topo2;
%     n=20;
%     theta = (-n:2:n)/n*pi;
%     phi = (-n:2:n)'/n*pi/2;
%     cosphi = cos(phi); cosphi(1) = 0; cosphi(n+1) = 0;
%     sintheta = sin(theta); sintheta(1) = 0; sintheta(n+1) = 0;
% 
%     xx = myscale*cosphi*cos(theta);
%     yy = myscale*cosphi*sintheta;
%     zz = myscale*sin(phi)*ones(1,n+1);
%     hold on;
%     surface(xx,yy,zz);
%     colormap([1  1  1; 1  1  1])
    % Create the sphere with Earth topography and adjust colormap
    surface(x,y,z,props,'parent',cax)
    
    colormap(topomap1)
    hold off
    

% Replace the calls to surface and colormap with these lines if you do 
% not want the Earth's topography displayed.
%     surf(x,y,z,'parent',cax)
%     shading flat
%     colormap gray
    
    % Refine figure
    axis equal
    hold on
    axis vis3d
    set(gcf,'color','k','renderer','zbuffer','inverthardcopy','off','name',...
   'Earth at 4 Pixels per Degree, by Tomas Kalinec','NumberTitle','off')
    set(gca,'color','k')
    ylabel(['Y [' units ']'],'Color','white')
    zlabel(['Z [' units ']'], 'Color','white')
    view(127.5,30)
    hold on
    h1=plot3(sx0/1000,sy0/1000,sz0/1000,'.r','MarkerSize',30);
    %plot3(sx/1000,sy/1000,sz/1000,'r','LineWidth',1.5);
    tp=linspace(0,2*pi,100);
    plot3(myscale*cos(tp),myscale*sin(tp),zeros(length(tp)),...
    'c');
    % Simulation of the satellite on the orbit
    nframe=123;
    mov(1:nframe)=struct('cdata',[],'colormap',[]);
    for i=1:nframe
        %t=0:t_konec/(nframe-1):t_konec;
        
        delete(h1);
        plot3(sx(1:i*7)/1000,sy(1:i*7)/1000,sz(1:i*7)/1000,'r','LineWidth',1.5);
        h1=plot3(sx(i*7)/1000,sy(i*7)/1000,sz(i*7)/1000,'.r','MarkerSize',30);
        length(sx);
        pause(0.1)
        mov=getframe(gcf)
    end

else
    xx = x; yy = y; zz = z;
end
    function dsv=dif_rce(~,sv)
        dsv=zeros(6,1);
        [th,ph,r]=cart2sph(sv(1),sv(2),sv(3));
        Fg=kk*m_earth*m/r^2;
        
        dsv(1)=sv(4);
        dsv(2)=sv(5);
        dsv(3)=sv(6);
        dsv(4)=-Fg/m*cos(th)*cos(ph);
        dsv(5)=-Fg/m*sin(th)*cos(ph);
        dsv(6)=-Fg/m*sin(ph);
    end 
end
