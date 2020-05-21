W zadaniu pierwszym zostały zaprezentowane wszystkie struktury danych.
Zgodnie ze specyfikacja wybieramy konkretna strukturę wpisując jej nazwe
jako argument parametru "--type", wszystkie sktuktury udostępniają
funkcjonalności zawarte na liści a hmap została dodatkowo wyposażona w 
funkcję "print" która wypisuje wszystkie elementy w strukturze. Po 
uruchomieniu programu wpisujemy funckję po znaku ":" wraz z argumentem 
jeśli jest to wymagane, po  wpisaniu "exit" wyświetlą nam się wszystkie 
informacje związane z działaniem programu które były zawarte na liście
laboratoryjnej.

W wyniku testów wyszło, że optymalną granicą przy której powinniśmy
zmienić liste na rbt w hmap jest około 300 elementów, wtedy koszty związane 
z porządkowaniem drzewa przestają być większe niż liniowe przeszukiwanie listy.

Dla drzewa rbt wszystkie operacje mają czas logarytmiczny bez względu na rodzaj 
danych, ponieważ jest ono uporządkowane, czas operacji w zwykłem drzewie binarnym 
różni się w zależności od  prowadzania danych, średni czas możemy określić jako  
logarytmiczny, lecz w pesymistycznych przypadkach, np.  dla danych wprowadzonych 
w kolejności posortowanej czas będzie liniowy. W strukturze hmap czas dostępu do 
ze względu na jej specyficzną budowę może się różnić, możemy założyć że dla dobrze 
wymieszanych danych czas będzie stały, leczy gdy wprowadzimy duży zbiór danych
dla  których wartość funckji hashującej będzie taka sama otrzyamy czas logarytmiczny
ponieważ dane w komórkach sa przechowywane w drzewie rbt (mówimy o  dużej ilości danych).