The whole  purpose of using the docker for building the data pipeline is to have separation
 of concern and having now relation with the native host and self contained and self dependent system 
 that can be run on any system while production using it 
  
  DATA pipeline is a steps through which data passes in order to get better 
  A lot of containers are included in the pipeline 

  Running in isolation that nothing get disturbed is main goal 
  plus it provides reproducibility
  we make the container  here and then save it as docker image and then run it in production 
  environment on the google cloud  and no dependency shit bro


  With Docker Compose, you can define your entire data pipeline environment
   in a single YAML file, ensuring that all services are
   configured and brought up in the correct order for integration testing
