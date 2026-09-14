molecule <- function(nIter = 5){
  
  graphics.off();
  
  a <- (1 + sqrt(as.complex(-3)))/2;
  b <- (1 - sqrt(as.complex(-3)))/2;
  c <- c(1, a,-b, -1, -a, b);
  
  u <- 0;
  for (k in 1:nIter){
    u = c(u+1, -u, u-1);
  }
  u = c(u, 1-u, 2+u, 3-u, 4+u, 5-u);

  u = u %% 6; #Modulo
 # print(u)
  
  z <- cumsum(c[u+1]);
  
  z <- c(0, as.complex(z/2^nIter));


  ttl=paste0("Molecule, nIter - ", nIter);
  plot(z, axes = FALSE, main = ttl,xlab = "", ylab = "")
 
  
  #coords = c(1,  (1 + sqrt(as.complex(-3)))/2, -(1 - sqrt(as.complex(-3)))/2, -1, -(1 + sqrt(as.complex(-3)))/2, (1 - sqrt(as.complex(-3)))/2)
  #plot(c(coords,coords[1]),type = "l",axes = FALSE)
  #dev.off()
  

} 

