function program6(input)
%clc
global PolohaAxes Xmodul Ymodul Xbod Ybod color
global m h Xplot Yplot detekce Muvol Xdist Ydist
if nargin==0
    m=get(0,'ScreenSize');
    f=figure('Units','Pixels','Name','Kreslení','Position',[0.35*m(3) 0.45*m(4) ...
       0.47*m(3) 0.45*m(4)],'Menubar','none','NumberTitle','off','Tag','figure')
    axes('Parent',f,'Units','Pixels','Tag','axes','Position',[50 100 0.45*m(3)-62 0.45*m(4)-140]...
       ,'Color','white')
    uicontrol('Units','Normalized','Style','Radio','BackgroundColor',get(gcf,'Color')...
        ,'Tag','radioon','Position',[0.1 0.04 0.03 0.08],'Callback','program6 cursoron')
    uicontrol('Units','Normalized','Style','Radio','BackgroundColor',get(gcf,'Color')...
        ,'Tag','radiooff','Position',[0.47 0.04 0.03 0.08],'Value',1,'Callback'...
        ,'program6 cursoroff')
    uicontrol('Units','Normalized','Style','Text','Position',[0.13 0.025 0.16 0.08]...
        ,'Tag','texton', 'BackgroundColor',get(gcf,'Color'),'String','Cursor on'...
        ,'FontWeight','bold','FontSize',11)
    uicontrol('Units','Normalized','Style','Text','Position',[0.5 0.025 0.16 0.08]...
        ,'Tag','textoff', 'BackgroundColor',get(gcf,'Color'),'String','Cursor off'...
        ,'FontWeight','bold','FontSize',11)
    uicontrol('Units','Normalized','Style','Text','String','Souøadnice bodu:','Tag','text2'...
        ,'Position',[0.07 0.92 0.35 0.05],'BackgroundColor',get(gcf,'Color'),...
        'FontWeight','bold','FontSize',10)
    uicontrol('Units','Normalized','Style','Edit','Tag','edit1','Callback','program6 text'...
        ,'Position',[0.4 0.92 0.15 0.05],'BackgroundColor',get(gcf,'Color'),...
        'FontWeight','bold','FontSize',10,'String',0)
    uicontrol('Units','Normalized','Style','Edit','Tag','edit2','Callback','program6 text'...
        ,'Position',[0.6 0.92 0.15 0.05],'BackgroundColor',get(gcf,'Color'),...
        'FontWeight','bold','FontSize',10,'String',0)
    uicontrol('Units','Normalized','Style', 'Push','String','Konec', 'Position',...
        [0.85 0.05 0.13 0.12],'FontWeight','bold','BackgroundColor','yellow'...
       ,'Tag','konec','CallBack', 'program6 konec', 'FontSize',13);
   uicontrol('Units','Normalized','Style', 'Push','String','Clear', 'Position',...
        [0.3 0.15 0.13 0.12],'FontWeight','bold','BackgroundColor','yellow'...
       ,'Tag','konec','CallBack', 'program6 clear', 'FontSize',13);
   uicontrol('Units','Normalized','Style', 'Push','String','Color', 'Position',...
        [0.6 0.15 0.13 0.12],'FontWeight','bold','BackgroundColor','yellow'...
       ,'Tag','barva','CallBack', 'program6 barva', 'FontSize',13,'Enable','off');
   axis([0 1000 0 1000])
   detekce=0;
   Muvol=0;
   color='red';
   set(gca,'xtick',[],'ytick',[])
   %Ylimit=Xlimit;
   
else
    switch input
        case 'cursoron'
            set(findobj('Tag','radiooff'),'Value',0);
            set(findobj('Tag','radioon'),'Value',1);
            f=findobj('Tag','figure');
            figure(f);
            set(f,'Pointer','Crosshair');
            set(gca,'ButtonDownFcn','program6 klik-');
            set(gcf,'WindowButtonUpFcn', 'program6 klik+');
            set(f,'WindowButtonMotionFcn','program6 pohyb');
            PolohaAxes=get(gca,'Position');
            Xplot=get(gca,'Xlim');
            Yplot=get(gca,'Ylim');
            Xmodul=(Xplot(2)-Xplot(1))/(PolohaAxes(3));
            Ymodul=(Yplot(2)-Yplot(1))/(PolohaAxes(4));
            %set(h,'EraseMode','xor')
            set(findobj('Tag','barva'),'Enable','on')
        case 'cursoroff'
            set(findobj('Tag','radioon'),'Value',0);
            set(findobj('Tag','radiooff'),'Value',1);
            set(findobj('Tag','figure'),'Pointer','arrow');
            set(findobj('Tag','figure'),'WindowButtonMotionFcn','');
            set(findobj('Tag','barva'),'Enable','off');
            
        case 'pohyb'
            s=get(findobj('Tag','figure'),'CurrentPoint');
            %pf=get(findobj('Tag','figure'),'Position')
            X=s(1)-PolohaAxes(1);
            Y=s(2)-PolohaAxes(2);
            Xosal=X*Xmodul+Xplot(1);
            Yosal=Y*Ymodul+Yplot(1);
           
            if ((X>=0 && Y>=0)) && ((X<=PolohaAxes(3)) && Y<=PolohaAxes(4))
                Xosa=num2str(s(1)-PolohaAxes(1));
                Yosa=num2str(s(2)-PolohaAxes(2));
                set(findobj('Tag','edit1'),'String',Xosa);
                set(findobj('Tag','edit2'),'String',Yosa);
                Xdist=abs(Xosal-Xbod);
                Ydist=abs(Yosal-Ybod);
                
                if (detekce==1)&&(Muvol==0)
                    Xbod=Xosal;
                    Ybod=Yosal;
                    hold on
                    h=plot(Xbod,Ybod,'o');
                    set(h,'MarkerSize',4,'LineWidth',3);
                    %set(h,'MarkerFaceColor',color);
                    set(h,'Color',color);
                    set(h,'HitTest','off')
                    %set(h,'EraseMode','xor')
                    %set(h,'Xdata',Xosal,'Ydata',Yosal);
                end
                
            end
            
        case 'klik+'
               
             detekce=0;
             Muvol=1;
            
                    
        case 'klik-'
                Muvol=0;
                detekce=1;
                set(findobj('Tag','edit1'),'String',Xbod);
                set(findobj('Tag','edit1'),'String',Ybod);
                hold on
                %h=plot(Xbod,Ybod,'ro');
                
                %hold off
                %Muvol=1;
                %hold off
                
        case 'clear'   
            cla
            
        case 'barva'  
            color=uisetcolor;
            %if isempty(h)==0 && isempty(c)==0
            %    color=c;
            %    set(h,'MarkerFaceColor',color);
            %end
            
        case 'konec'
            close all
    end
end