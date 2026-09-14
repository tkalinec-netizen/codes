tree <- function(nIter, xsh=0, fn="", ttl=""){
  graphics.off();
  
  ## ord - order/depth, xsh - x-shift, fn - file name,
  ##  ttl - plot title.
  
  # start of growing

  
  # movong about angle 60°
  
  
  tree_iter <- function(x,y,angle,Iter){
    x2=y2=0; 
    d2r=pi/180.0;
    a1 <- angle*d2r; 
    d1=0;
    d = Iter;
    
    if(Iter<=0) {return()}
    if(Iter>0)
    { 
      
      x2=x+cos(a1)*d*10.0;
      y2=y+sin(a1)*d*10.0;
      segments(x, y, x2, y2, col='darkgreen');
      tree_iter(x2,y2,angle-20,Iter-1);
      tree_iter(x2,y2,angle+20,Iter-1);
    }
   }
    
  
    #plot(X,Y, type = 'o', axes = FALSE, ylab = "",xlab = "")
    cat(" *** START FRT:", date(), "\n");
    m=50*nIter;
    if(fn=="") {pf=paste0("FRTR", nIter, ".png")} else {pf=paste0(fn, ".png")};
    if(ttl=="") {ttl=paste0("Fractal tree, nIter - ", nIter)};
    cat(" *** Plot file -", pf, "title:", ttl, "\n");
    ##plot(NA, xlim=c(0,m), ylim=c(-m,0), xlab="", ylab="", main=ttl);
    plot(NA, xlim=c(0,m), ylim=c(0,m), xlab="", ylab="", main=ttl, axes = FALSE);
    tree_iter(m/2+xsh,0,90,nIter);
   #print(max(segments))
   # dev.copy(png, filename=pf, width=m, height=m);
  #  dev.off(); graphics.off();
    cat(" *** END FRT:",date(),"\n");
   

}

