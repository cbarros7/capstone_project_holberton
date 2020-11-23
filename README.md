# Customer segmentation applied in FinTech

## Objective

The aim of this project is to implement an automatic learning implementation algorithm for the segmentation of customers according to their financial behaviour.

## Introduction 

This project was developed for a finTech company, they already have a huge DataBase, and they need a machine learning ,model to predict payment customer’s behaviours, this will allow them make decisions, and increment the company’s productivity. This Project will help them and their customers to improve on fast loan study processes, It will only suggest a basic customer’s classification and the behaviour will be initially evaluated by their Grows/Financial/Risk managers. It is important to clarify that this project is not going to be in a deployment phase, it will be very limited to filtered excel data given by the customer, and the algorithm will not have self-training phases.

## Technologies
**1.) Frontend**
 + **Languages:** JavaScript
 + **Libraries:** D3.js
 + **Platforms:** AWS
 + **Frameworks:** Angular
 + **Resources:** [MDBootstrap Angular](https://mdbootstrap.com/docs/angular/)

**2.) Backend:**
 + **Languages:** NoSQL
 + **Libraries:** BOTO3
 + **Platforms:** AWS
 + **Resources:** [Tutorial DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStarted.Python.html)

**3.) Machine learning:**
 + **Languages:** Python
 + **Libraries:** Panda, Numpy, json, scikit-learn
 + **Platforms:** AWS
 + **Resources:** [scikit-learn](https://scikit-learn.org/stable/)
      

## Architecture

<p align="center">
  <a href="https://imgur.com/qyxu3CE">
    <img src="https://i.imgur.com/jRZnA9P.png" alt="monty" title="source: imgur.com"  />
  </a>

   <p align="center">
    End-to-end map for the data flowing through the system
    <br />   
  </p>
</p>

## APIs and Methods

 1. **API routes**
    
    + `/api/userRandom`
        
        **GET:** Returns a randomized array containing a user data set.

    + `/api/userCluster`
        
        **POST:** It returns a cluster classification given by Machine Learning algorithm.    
    
    + `/api/dbPost`
    
        **POST:** It Saves user data into a Database.
    
    + `/api/dbGet`
    
        **GET:** It Retrieves all user data from a Database.

2. **API endpoints:**
There will not be any API endpoints allowing other clients to use because we will be handling sensitive information of clients to Sempli. The API will be used only by the company (Sempli), and would only be consulted by the web client. 

3. **3rd party APIs:**
There will not be any 3rd party APIs on the project since we are not using any other source of information than the sensible data collected by the company (Sempli).


## Authors
+ [Andrés Hugueth](https://github.com/andreshugueth)
+ [Carlos Barros](https://github.com/cbarros7)
+ [Jose Vallejo](https://github.com/JoseAVallejo12) 
+ [Ronnie Barrios](https://github.com/ronniebm)
+ [Wilder Rincón](https://github.com/wildcox80) 
