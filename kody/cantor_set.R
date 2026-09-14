

draw_cantor <- function ( x,  y,  len, iter){
  X <-  c(x,x+len)
  Y <- c(y,y)
  ttl=paste0("Cantor set, nIter - ", iter);
  plot(X,Y, type = 'n',xlim=c(0,len),ylim=c(-len,len), axes = FALSE, main = ttl,xlab = "", ylab = "")
  par(new=TRUE)
  cantor_set(x,  y,  len,iter)
  
  #cantor_set(x,  y,  -len)

}

 cantor_set <- function ( x,  y,  len, iter) {
   

    #if (abs(len) >= 1)
   if (iter >= 1 )
   {
      X <-  c(x,x+len)
      Y <- c(y,y)
      
     # print(X)
     # print(Y)
     # plot(X,Y, type = 'n')
      par(new=TRUE)
      
      lines(X,Y, type = 'l');
      
    
     # lines(X+1,Y+20, type = 'l');
      y <- y + 10;
      cantor_set(x,y,len/3,iter-1);
      cantor_set(x+len*2/3,y,len/3,iter-1);
     
   
    }
}

