# How to label the data for supervised learning
For supervised learning you may often need a csv file with the
filenames and labels. Just look at the following example.

You have a folder with files: 

<img src="images/data.png" alt="Your data">

You want a csv file like that: 

<img src="images/csv.png" alt="Csv file">

Take the following steps: 

    pip install label

If you haven't already installed pandas and glob, also run:

    pip install pandas glob3

and if you use python2:

    pip install pandas glob2

You can then start the python interpreter from the terminal typing:

    python

Then within the Python interpreter, you can use the label package:

    from label import create_csv

and start the step-by-step instruction typing:

    create_csv()

<img src="images/scr1.png" alt="Screenshot 1"> <br/>

<img src="images/scr2.png" alt="Screenshot 2"> <br/>

<img src="images/scr3.png" alt="Screenshot 3"> <br/>

<img src="images/scr4.png" alt="Screenshot 4"> <br/>

<img src="images/scr5.png" alt="Screenshot 5"> <br/>

<img src="images/scr6.png" alt="Screenshot 6"> <br/>
    
