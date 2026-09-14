function []=kyvadlo()
%% Pohyb zavazi na pruzine
    clc
    m=1; % kg
    k=0.5;
    s0=0; % m
    v0=1; % m/s

    %cas_reseni
    t_konec=100; % s

    % soustava diferencialnich rovnic
    %ds/dt=v;
    %dv/dt=-k*s/m;

    function dx=dif_rce(t,x)
    % x=[s0, v0]
        dx=zeros(2,1);
        dx(1)=x(2);
        dx(2)=-k*(x(1))/m;
    end

    [t,y]=ode45(@dif_rce,[0,t_konec],[s0, v0]);
    
    f1=figure('Name','Pohyb zavazi bez ztraty energie', 'NumberTitle','off')
    subplot(1,2,1)
    plot(t,y(:,1),'r')
    title('Zavislost drahy na case')
    xlabel('t(s)')
    ylabel('s(m)')
    
    subplot(1,2,2)
    plot(t,y(:,2),'g')
    title('Zavislost rychlosti na case')
    xlabel('t(s)')
    ylabel('v(m/s)')
    
    function dx=dif_rce_2(t,x)
    % x=[s0, v0]
        dx=zeros(2,1);
        dx(1)=x(2)-0.1*x(1);
        dx(2)=-k*(x(1))/m;
    end
    [t,y]=ode45(@dif_rce_2,[0,t_konec],[s0, v0]);
    f2=figure('Name','Pohyb zavazi s tlumenymi kmity', 'NumberTitle','off')
    subplot(1,2,1)
    plot(t,y(:,1),'r')
    title('Zavislost drahy na case')
    xlabel('t(s)')
    ylabel('s(m)')
    
    subplot(1,2,2)
    plot(t,y(:,2),'g')
    title('Zavislost rychlosti na case')
    xlabel('t(s)')
    ylabel('v(m/s)')
    
end
