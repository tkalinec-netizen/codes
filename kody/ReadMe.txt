Návod na spouštìní jednotlivých skriptù v programu R.

1) triangle.R

 - Jou 2 typy vykreslení.


 -triangle(type, nIter)

    - nIter - poèet iterací

    - type - èíselný parametr v rozmezí 1-2

 - type = 1
  - pøíklad od Jonase Lundgrena, vykreslení pomocí bodù komplexní roviny
  - Pøíklad volání: triangle(1,8) 

 - type = 2

   - Vykreslení odebráním støedového troúhelníku. Výchozí troúhelník je obarvený èernou barvou, odebrané bílou.

   - Pøíklad volání: triangle(2,8) 

2) cantor_set.R
   draw_cantor.R
 - parametry
  - x, y poèáteèní souøadnice
  - len délka intervalu
  - iter poèet iterací
 - volání draw_cantor(1,1,100,5)

3) koch_snowflake.R

 - Paramety 
  - nIter poèet iterací 
  - type - celoèíslní parametr v rozmezí 1-2, typ fraktálu

 - type = 1
   - Kochova vloèka na polygonu
   - Pøíklad volání koch_snowflake(5,1)

 - type 2 
   - Vykreslení fraktálního útvaru na jedné úseèce
   - Pøíklad volání koch_snowflake(5,2)

4) Molecule.R

 - Vykereslení fraktálního útvaru ve tvaru molekuly.

 - Pøíklad volání molecule(5) - 5. iterace

5) JuliaSet.R

 - Pro barevné vykreslení odkomentujte kód v sekci "#uncomment for colors draw".


 - Výsledný obrázek je uložen do souboru 'Julia.jpg'
 - Pøíklad volání JuliaSet(150,-0.7,-0.4), kde první parametr je maximílní poèet iterací na jednom pixelu. 
   Komplexné rovina je dána rovnicí y = -0.7x - 0.4i

 - Pozn.
	Je potøeba upravit nastavení kódu, aby výsledná výstup odpovídal požadované vizualizaci.

6) tree.R
   Fraktální útvar binární strom
   
  - Export do obrázku, možnost nastavit parametry
  - nIter poèet iterací
  - volání tree(5)