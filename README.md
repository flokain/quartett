# vogelquartett
this is a python program to  renders a set of quartett cards from a google spreadsheet as pdf.
as an example there is a sheet for a bird quartett checked in.

#requirements
- python 3.5+
- Install the required packages for python using
`pip install src/requirements.txt`

# usage
to run the example:
1. put all image date in the correct resource folder. watch out for the naming conneventions.(look them up in the template.svg and xmlManipulator.py)
2. call the script 
    ```console
    cd src
    python quartettCreator.py
    ```
3. evaluate the result in the `out/pdf` folder