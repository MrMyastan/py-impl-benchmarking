# py-impl-benchmarking
for a school sci project\
i used pypy 2.7 v7.3.3, jython 2.7.2 (and AdoptOpenJDK 11.0.9.1), cpython 2.7.18, ironpython 2.7.11 (and .NET 5.0.100)\
like any decent programmer i copypasted and then slightly adjusted the calculating pi code from [this stackoverflow answer](https://stackoverflow.com/questions/45113790/calculating-pi-to-the-nth-digit)\
aaaaand the n-body simulation stuff was taken from [here](pybenchmarks.org/u64q/program.php?test=nbody&lang=python&id=1)\
aaaaaaaaaaaaaaaaaaand the recursive fib was borrowed from @jesse-toftum\
![graph of average total execution times](https://github.com/MrMyastan/py-impl-benchmarking/blob/main/graph.png?raw=true)\
![graph of total execution times and averages](https://github.com/MrMyastan/py-impl-benchmarking/blob/main/graph.png?raw=true)\
theres some more data about how long each interpreter took for each individual test in the output if you want to look, the only thing i noticed that seemed worth noting was that PyPy took ~60 seconds calculating pi (most of its time) and jython did it in ~13\
the benchmark program happens to also be (i think) a valid python3 program so maybe ill test it with cpython 3 and pypy 3 one of these days
