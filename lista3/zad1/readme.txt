Implementacja radix sort znajduje się w lini 439 w pliku "sort.py", program uruchamiamy poprzez plik "main.py" z odpowiednimi parametrami,
można skorzystać z pomocy (parametr -h lub --help), analogicznie jak w liście poprzedniej.

Widac, że algorytm radix, jest szybszy od algorytmów quick i merge, lecz z pewnym ograniczeniem, w przypadku kiedy radix operuje na 
tablicach z liczbami rzędu n^3, różnica ta zaciera się, a dla n^4 (gdzie n^1 to 10 000) przewagę uzyskują algorytmy quick oraz merge,
wyniki te możemy zobaczyć odpalając program "tester.py". Radix sort zwiększa czas działania przy duzych liczbach ponieważ dodanie każdego dodatkowego 
rzędu wielkości wiąze sie z uruchomieniem procedury counting sort.

Zużycie pamięci mozna zbadać przu uruchomieniu pliku "memory.py", widać, że zakres z którego losowane są liczby ma znikomy wpływ na zużycie pamięci,
natomiast ilość liczb do posortowania robi tutaj dużą różnicę.
