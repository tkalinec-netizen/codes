JuliaSet <- function(MaxIter, a, b){
  
  #c = ax + bi 
  # a,b  Complex parameter, connected to coordinate of the Mandelbrot set in a complex plane. Constants here.
  #JuliaSet(150,-0.7,-0.4)
  
  #JuliaSet(150,-0.73,-0.19)
  
  #a=-0.7;b=-0.4
  Limits=c(-2,2)
  # MaxIter=60
  cl=colours()
  Step=seq(Limits[1],Limits[2],by=0.005)
  PointsMatrix=array(0,dim=c(length(Step)*length(Step),3))
  a1=0
  ttl = paste0("Julia set, a = ", a, ", b =", b);
  plot(0,0,xlim=Limits,ylim=Limits,col="white",type = 'n', axes = FALSE, main = ttl)
  
  for(x in Step)
  {
    for(y in Step)
    {
      n=0
      DIST=0
      x1=x;y1=y # Original x and y are saved.
      while(n<MaxIter & DIST<3)
      {
        newx=x1^2-y1^2+a  # x axis is real
        newy=2*x1*y1+b    # y axis is complex
        DIST=newx^2+newy^2
        x1=newx;y1=newy
        n=n+1
      }
      if(DIST<3) colour=24 
      else colour=10*n #uncomment for colors draw
      if (DIST>3.5) colour=1 #only black color
      #points(x,y, pch=".", col=cl[colour])
      a1=a1+1
      PointsMatrix[a1,]=c(x,y,colour)
    }
  }
  par(new=TRUE)
  
 # X11()
  png(filename = 'Julia.jpg')
  #ttl = paste0("Julia set, a = ", a);
  
  plot(PointsMatrix[,1], PointsMatrix[,2], xlim=Limits, ylim=Limits, col=cl[PointsMatrix[,3]], pch=".", xaxt='n', yaxt='n',
       main =ttl, xlab='',ylab='')
  
  dev.off()
  dev.off()
}