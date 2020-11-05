@echo off
set "CurDir="
for %%a in ("%cd%") do set "CurDir=%%~nxa"
if NOT "%CurDir%" == "assignment2" exit

if exist %CD%\src\test\testcases\ (
    echo "Cleaning testcases"
	rmdir /Q /S %CD%\src\test\testcases\
)
    echo "Creating testcases"
    mkdir %CD%\src\test\testcases\

if exist %CD%\src\test\solutions\ (
    echo "Cleaning solutions"
	rmdir /Q /S %CD%\src\test\solutions\
)
    echo "Creating solutions"
    mkdir %CD%\src\test\solutions\

if exist %CD%\src\test\solutionsSample (
    echo "Cleaning solutions"
	rmdir /Q /S %CD%\src\test\solutionsSample
)

if exist %CD%\output\ (
    echo "Cleaning Output..."
    rmdir /Q /S %CD%\output\
)
    echo "Creating Output..."
    mkdir %CD%\output\
    mkdir %CD%\output\test

if exist %CD%\test\solutions\ (
    echo "Copying solution sample"
    mkdir %CD%\src\test\solutionsSample
    robocopy %CD%\test\solutions %CD%\src\test\solutionsSample /move /NFL /NDL /NJH /NJS /nc /ns /np
)

if exist %CD%\test\check.py (
    echo "Copying check.py"
    robocopy %CD%\test\ %CD%\src\ check.py /move /NFL /NDL /NJH /NJS /nc /ns /np
)

if exist %CD%\test\LexerSuite.py (
    echo "Rename old LexerSuite.py to LexerSuite_old.py"
    ren %CD%\src\test\LexerSuite.py LexerSuite_old.py
    echo "Copying LexerSuite.py"
    robocopy %CD%\test\ %CD%\src\test\ LexerSuite.py /move /NFL /NDL /NJH /NJS /nc /ns /np
)

if exist %CD%\test\ParserSuite.py (
    echo "Rename old ParserSuite.py to ParserSuite_old.py"
    ren %CD%\src\test\ParserSuite.py ParserSuite_old.py
    echo "Copying ParserSuite.py"
    robocopy %CD%\test\ %CD%\src\test\ ParserSuite.py /move /NFL /NDL /NJH /NJS /nc /ns /np
)

if exist %CD%\test\TestUtils.py (
    echo "Rename old TestUtils.py to TestUtils_old.py"
    ren %CD%\src\test\TestUtils.py TestUtils_old.py
    echo "Copying TestUtils.py"
    robocopy %CD%\test\ %CD%\src\test\ TestUtils.py /move /NFL /NDL /NJH /NJS /nc /ns /np
)

if exist %CD%\src\test\testLexer.py (
    del %CD%\src\test\testLexer.py /f /q
)

if exist %CD%\src\test\testParser.py (
    del %CD%\src\test\testParser.py /f /q
)

cd src

echo "Cleaning and Generatting..."
python run.py clean
python run.py gen

echo.
echo "=============================================="
echo "Testing Lexer..."
python run.py test LexerSuite

cd ..
if exist %CD%\src\test\LexerSuite.txt (
    robocopy %CD%\src\test\ %CD%\output\ LexerSuite.txt /move /NFL /NDL /NJH /NJS /nc /ns /np
    del %CD%\src\test\ParserSuite.txt /f /q
)
cd src

echo.
echo "=============================================="
echo "Testing Parser..."
python run.py test ParserSuite

echo.
echo "=============================================="
echo "Testing ASTGen..."
python run.py test ASTGenSuite

cd ..
if exist %CD%\src\test\ParserSuite.txt (
    robocopy %CD%\src\test\ %CD%\output\ ParserSuite.txt /move /NFL /NDL /NJH /NJS /nc /ns /np
    del %CD%\src\test\LexerSuite.txt /f /q
)
cd src

if exist %CD%\test\solutionsSample\ (
    if exist %CD%\check.py (
        echo.
        echo "=============================================="
        echo "Checking solution..."
        echo.
        python check.py
    )
)
cd ..

@echo off

if exist %CD%\src\check.txt (
    robocopy %CD%\src\ %CD%\output\ check.txt /move /NFL /NDL /NJH /NJS /nc /ns /np
    start %CD%\output\check.txt
)

if exist %CD%\src\test\LexerSuite_old.py (
    robocopy %CD%\src\test\ %CD%\output\test\ LexerSuite.py /move /NFL /NDL /NJH /NJS /nc /ns /np
    ren %CD%\src\test\LexerSuite_old.py LexerSuite.py
)

if exist %CD%\src\test\ParserSuite_old.py (
    robocopy %CD%\src\test\ %CD%\output\test\ ParserSuite.py /move /NFL /NDL /NJH /NJS /nc /ns /np
    ren %CD%\src\test\ParserSuite_old.py ParserSuite.py
)

if exist %CD%\src\test\TestUtils_old.py (
    robocopy %CD%\src\test\ %CD%\output\test\ TestUtils.py /move /NFL /NDL /NJH /NJS /nc /ns /np
    ren %CD%\src\test\TestUtils_old.py TestUtils.py
)

if exist %CD%\src\check.py (
    robocopy %CD%\src\ %CD%\output\test\ check.py /move /NFL /NDL /NJH /NJS /nc /ns /np
)

if exist %CD%\src\test\solutionsSample\ (
    robocopy %CD%\src\test\solutionsSample\ %CD%\output\test\solutions /move /NFL /NDL /NJH /NJS /nc /ns /np
)

pause >nul