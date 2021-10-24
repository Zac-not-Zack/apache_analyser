# Projet “Automatisation des tâches d’administration système”
Contributors : WONG Hoe Ziet & BIN AZMI Adam

# Overview
This is a project of the module "Automatisation of System Administration Tasks" for the course of Diplôme Universitaire Technologie (DUT) Réseaux & Télécommunications.

The main function of the project is to analyse the access log file of an Apache server. The project is consisted of functions that are built to be able to inspect and analyse the data extracted from the log file and provide insights to client notably in the security and commercial point of view. The details and explanation of each the functions can be found below. The project also contains a simple Command Line Interface (CLI) that will facilitate the usage of the functions.

# Targetted User
Our targetted audience is the mainly the user of Apache server, specifically the server adminstrator or development team. This program can also eventually serve as model for other server who uses the same logging format.

# Installation
The package of the project will be available on PyPi soon after the complete structuring and validation. Stay tuned!

# Usage
In the version 1.0.0 of this module, it contains a total of 10 functions that are conceived to facilitate the analyse of a running Apache server. Thanks to our CLI you can choose whichever functions that you wish. 

**Note : You will have to use "option --a" when running the code for the first time to convert the file into the format of JSON**
  
  ## 1. convert_json (option --a)
  This function is used to convert a log file to json format. **This function must be used when running the module for the first time.**
  ```ruby
  projet_function.py path/to/your/log/file --a
  ```
  ## 2. count_os (option --b)
  This function will help to detect the exploitation system (OS) used by clients. It generates percentage and graph showing the usage of each OS.
  ```ruby
  projet_function.py path/to/your/log/file --b
  ```
   ## 3. average_os (option --c)
  It helps to calculate the average size of objects requested by clients. On top of that, it also provides the maximum and minimum size of objects requested. This allow us to anticipate the traffic on the server, adapt the contains and adapt the bandwidth of the network according to the calculation.
  ```ruby
  projet_function.py path/to/your/log/file --c
  ```
   ## 4. trafic_du_jour (option --d)
  This function is used to track the volume of visitors of the day, allowing us to monitor the current traffic on the server.
  ```ruby
  projet_function.py path/to/your/log/file --d
  ```
   ## 5. count_method (option --e)
  With this function, we can observe and analysis the request methods used by the visitors. The analyse is carried on 4 most common request methods : GET, POST, HEAD and PUT. It also generates percentage and graph to provide a clearer representation.
  ```ruby
  projet_function.py path/to/your/log/file --e
  ```
   ## 6. heure_creuse (option --f)
  This function allow us to identify the peak hour on a server. This is undoubtedly crucial from the commercial point of view. For example, it will help to provide an insight on the best time to publish contains on a website.
  ```ruby
  projet_function.py path/to/your/log/file --f
  ```
   ## 7. count_os (option --b)
  This function will help to detect the exploitation system (OS) used by clients. It generates percentage and graph showing the usage of each OS.
  ```ruby
  projet_function.py path/to/your/log/file --b
  ```
