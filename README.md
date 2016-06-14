# gantthelper
Python tool wrapping around the pgfgantt LaTeX library to make drawing Gantt charts easier

Requires the pgfgantt LaTeX library, and the dateutil Python library.

## Example usage:

    # Generate tex source
    python example.py > [example.tex](/example.tex)
    
    # Compile tex to pdf
    pdflatex example.tex
    
    # Convert tex to ppm
    pdftoppm example.pdf example
    
    # Convert ppm to png
    convert example-1.ppm [example.png](/example.png)

## Some notes:

    - Tasks and groups will be reordered according to their start dates -- this is
      apparent in the example plot (Task 3 comes before Task 2).
      
    - Dependencies between tasks can currently not be specified.
    
    - Task progress indication is planned, but not yet available.
