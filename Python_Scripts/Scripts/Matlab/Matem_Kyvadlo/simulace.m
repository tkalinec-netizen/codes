function simulace(l,phi,t)

rectangle('Position',[-l,-0.2*l,2*l,0.2*l],'FaceColor','r');
hold on
axis('equal')
axis 'off'
xlim([-l-0.1 l+0.1])
ylim([-l-0.1 l+0.1])
%uhel=linspace(phi,-phi,20);
uhel=phi;
x_poc=l*cos(uhel(1)-pi/2);
y_poc=l*sin(uhel(1)-pi/2);
h=plot([0 x_poc],[0 y_poc],x_poc,y_poc,'ko');
pause(1)
for i=1:length(uhel)
    x_poc=l*cos(uhel(i)-pi/2);
    y_poc=l*sin(uhel(i)-pi/2);
    pause(5/(t))
    delete(h)
    
    h=plot([0 x_poc],[0 y_poc],x_poc,y_poc,'ko','MarkerSize',7);
    %set(h,'MarkerSize',4,'LineWidth',3)
    drawnow expose;
    
 
end
