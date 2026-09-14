koch_snowflake <- function (nIter, type){
  #dev.off()
  
  if (type == 1){
    
    #   Author: Jonas Lundgren <splinefit@gmail.com> 2010
    a <- 1/2 + sqrt(as.complex(-3))/6;
    b <- 1-a ;
    c <- 1/2 + sqrt(as.complex(-3))/2;
    d <- 1 - c;
    z <- 1;
    for (k in 1:nIter){
      z = Conj(z);
      z = c(a*z, b*z+a);
    }
    
    z = c(0, z ,1-c*z, 1-c-d*z);
    
    ttl=paste0("Koch snowflake, nIter - ", nIter);
    
    plot(z,type = 'l',xlab = "", ylab = "",col = 'blue',axes= FALSE,main=ttl)
    png(filename="snowflake")
    plot(z,type = 'l', axes= FALSE,xlab = "", ylab = "",col = 'blue')
    dev.off()
  }
  
  #Define verticies of triangle
  if (type == 2){
    vA = c(0,0);
    vB = c(1,0);
    vC = c(0.5,sqrt(3)/2);
    
    flake_points = c(vA, vB, vC)
    

    X = c(vA[1],vB[1],vC[1])
    Y = c(vA[2],vB[2],vC[2])
    #plot(X,Y,type = 'l', axis= FALSE)
    
    plot(c(vA[1],vB[1]),c(vA[2],vB[2]),type='n', axes= FALSE,xlab = "", ylab = "")
    par(new=FALSE)
    
    # recusion
    snowflake <- function(p1,pend,nIter){
      if (nIter > 1){
        
        side = (pend-p1);
        Pcent = p1 + side/2;
        side = side/3;
        p2 = p1+side;
        x3 = Pcent[1] + side[2]*sqrt(3)/2;
        y3 = Pcent[2] - side[1]*sqrt(3)/2;
        p3 = c(x3,y3)
        p4 = pend-side;
        PxNew <- c(p1[1],p2[1],p3[1],p4[1],pend[1]);
        PyNew <- c(p1[2],p2[2],p3[2],p4[2],pend[2]);
        # lines(c(p2[1],p4[1]),c(p2[2],p4[2]), col = 'white')
        if (nIter > 5){ # setting origin line
           lines(PxNew,PyNew,type='l')
        }
     
  
        
        snowflake(p1,p2,nIter-1);
        snowflake(p2,p3,nIter-1);
        snowflake(p3,p4,nIter-1);
        snowflake(p4,pend,nIter-1);
        
        
        #plot(c(vA[1],vB[1]),c(vA[2],vB[2]),type='n', axis= FALSE)
        
      }
    else
    {
 
      lines(c(p1[1],pend[1]),c(p1[2],pend[2]),type='l',col = 'red')
      
    }
      
    
    }
    snowflake(vA,vB,nIter)
    
    #dev.off()
    
  }
  

}