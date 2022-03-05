# Classifying-road-signs

For our traffic sign data set, we are going to access a repository on BitBucket of typical German traffic sign images. The main problem is we're going to be dealing with a smaller data set that can be classified into many more classes,this can make it a lot more difficult for our network to learn properly with a high accuracy rate.That being said, preprocessing these images in a correct way is going to be crucial to our success. Pre processing and preparing data sets is extremely important in the field of deep learning.

We will use a new technique for dealing with smaller data sets that will allow our network to learn more effectively.

**Dataset link:** [Click here](https://bitbucket.org/jadslim/german-traffic-signs) 

The repository contains CSV and Piclke file.
CSV, which is a spreadsheet that contains all of our traffic signs,along with their labeled names, a comma separated values type documents.


The rest of the files are Pikul files that contain our respective training, testing and validation Pickled files in Python essentially contain serialized data that can be unpicked when desired, since the character stream contains all the information necessary to reconstruct the serialized object and thus unpick a link would be the inverse operation of pickling. So as to deserialized the Python object and make use of it in our program, the characters stream state is often more convenient to store and transfer, which makes pickling an important operation in Python.

<h1 align="center">Traffic sign images</h1>


<p align="center"><img src="https://github.com/RIT-MESH/Classifying-road-signs/blob/main/2.PNG?raw=true"alt="Sublime's custom image"/>
</p>


<h1 align="center">Distribution of the train dataset</h1>


<p align="center"><img src="https://github.com/RIT-MESH/Classifying-road-signs/blob/main/1.PNG?raw=true"alt="Sublime's custom image"/>
</p>


<h1 align="center">Losses</h1>


<p align="center"><img src="https://github.com/RIT-MESH/Classifying-road-signs/blob/main/3.PNG?raw=true"alt="Sublime's custom image"/>
 </p> 
  
  
 <h1 align="center">Accuracy</h1>


<p align="center"><img src="https://github.com/RIT-MESH/Classifying-road-signs/blob/main/4.PNG?raw=true"alt="Sublime's custom image"/>
  </p>
  


## Final output :


   


Original Image           |  Predicted Sign
:-------------------------:|:-------------------------:
<a href="https://github.com/RIT-MESH/Classifying-road-signs/blob/main/5.PNG" target="_blank"><img src="https://github.com/RIT-MESH/Classifying-road-signs/blob/main/5.PNG" width=450 height=200 ></a>  |  <a href="https://github.com/RIT-MESH/Classifying-road-signs/blob/main/6.PNG" target="_blank"><img src="https://github.com/RIT-MESH/Classifying-road-signs/blob/main/6.PNG" width=450 height=200 ></a>



