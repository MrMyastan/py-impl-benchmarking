echo Jython
for ($i = 0; $i -lt 5; $i++)
{
	Measure-Command { java -jar .\jython-2.7.2\jython.jar .\tests\test.py | Out-Default }
}

echo IronPython
for ($i = 0; $i -lt 5; $i++)
{
	Measure-Command { .\IronPython-2.7\ipy.exe .\tests\test.py | Out-Default }
}

echo CPython
for ($i = 0; $i -lt 5; $i++)
{
	Measure-Command { .\cpython-2.7.18\python.exe .\tests\test.py | Out-Default }
}

echo PyPy
for ($i = 0; $i -lt 5; $i++)
{
	Measure-Command { .\pypy2.7-v7.3.3-win32\pypy.exe .\tests\test.py | Out-Default }
}