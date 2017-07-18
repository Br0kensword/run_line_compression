This project was completed using Python 3 to take advantage of how easy it is to manipulate text/strings in the language.

Took some time to reasearch compression, run-line seemed the easiest to impelment with decent results given the amount of time I had to work with, attempted to incorporate burrows-wheeler transforms but was too complicated/ didnt always preserve the image after decoding. With this method, if the ascii image is big enough and has enough repitition the compression works fairly well (as the case was with data.txt and akira.txt). That being said often times I found that the encoded data could be larger than the original if there wasnt enough repitition (in the case of cloud.txt and ff7.txt). If a file would lead to an inefficient use of space I would just send the original file as that way we would at least do no worse than the original file size.

This project requires Python 3 to work. All imported modules are Python builtins and should not require extra instillation.

To run the main project:
python ascii_transport.py --file yourinput.txt  
# --file takes either the name of the txt file if its in the same directory as ascii_transport.py or the path to file if its somewhere else

To run unittests:
python ascii_test.py #please place the following test files in the same directory as ascii_test.py (empty.txt, data.txt, cloud.txt) for unittests to work properly
