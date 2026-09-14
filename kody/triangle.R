sierpienskiTriangle <- function(nIter = 5, type = 1){
  graphics.off();
  
  if (type == 1){
    print ("Body:")
    
    a = (5 + sqrt(as.complex(-3))/2);
    # Generate point sequence
    z = c(0, 5);
    for (k in 1:nIter){
      z = c(z, z+a, z+5)/2;
    }
    # Close triangle
    z = c(z, a, 0);
    plot(z,type = "l",axes = FALSE)
  }
  
  if (type == 2){
    s = 2; #length of side
    px = c(0,s/2,s);
    py = c(0,s,0);
    iter = nIter;
    
    ttl=paste0("Sierpinski triangle, nIter - ", iter);
    
    plot.new()
    plot(px,py,type = "l",axes = FALSE, xlab='',ylab='') #after fisrst iteration
    plot(px,py,type="n",axes = FALSE,xlab='',ylab='',main = ttl)
    polygon(px,py,col='black')
    
   # for first iteration
    recursion <- function(x,y,iter){
    
    xn1 = x[1]+(x[3] - x[1])/2;
    xn2 = xn1 + (x[3] - xn1)/2;
    xn3 = x[1]+(xn1 - x[1])/2;
    
    yn1 = y[1];
    yn2 =y[2] - (y[2] - y[1])/2;
    yn3 = yn2;
    
    it_x = c(xn1, xn2, xn3)
    it_y = c(yn1, yn2, yn3)
    
    #  s = s/2;
     # it0_x = c(s/2, s, 3*s/2);
     # it0_y = c(sqrt(3*(s^2)/4), 0, sqrt(3*(s^2)/4));
      
      #plot.new()
     polygon(it_x,it_y,col='white')
     
     
     if (iter > 1){
       recursion(c(x[1],xn3,xn1),c(y[1],yn3,yn1),iter-1);
       recursion(c(xn1,xn2,x[3]),c(yn1,yn2,y[3]),iter-1);
       recursion(c(xn3,x[2],xn2),c(yn3,y[2],yn2),iter-1);
       
       
     }
     
     iter <- iter - 1;
       
     
    }
     
    recursion(px,py,iter)
    
    
    #png(file="notitle.png",width=400, height=350)
    #dev.off()
    
  }
}

