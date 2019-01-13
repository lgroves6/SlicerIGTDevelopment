---
title: 'Tutorial for Developing Image-Guided Intervention Modules Using 3D Slicer'
tags:
- Tutorial
- 3D Slicer Modules
- Slicer IGT 
- Image-guided Interventions
authors:
- name: Leah Groves 
  affiliation: "1, 2" 
- name: Golafsoun Ameri 
  affiliation: 1 
- name: Terry M. Peters
  affiliation: "1, 2" 
affiliations:
- name: Robarts Research Institute
  index: 1
- name: Western University 
  index: 2
date: January 13 2019
bibliography: paper.bib
---

# Summary

This paper presents an overview of a blog (http://computerassistedsurgery.robarts.ca) that was developed as a learning-module for the 3D Slicer [@fedorov20123d] architecture and module development for image-guided therapy (IGT) applications. Image-guided therapies are medical procedures that use computer-based systems that provide navigation facilities and supplemental procedure information to help the physician precisely visualize and target the surgical site. This learning-module focuses on the development of 3D Slicer IGT scripted modules. In addition to providing the first top-to-bottom description of 3D Slicer architecture, this blog covers the components required to develop an IGT module in 3D Slicer. These components include (1) the PlusServer within the Plus Toolkit [@Lasso2014a], a platform for data capture and broadcasting, and (2) the 3D SlicerIGT Extension [@ungi2016open], a platform for receiving the broadcasted data in 3D Slicer for further processing and visualization. This information is presented as an interactive blog in which examples, demonstrations, and sample codes are provided to facilitate implementation of an IGT module for a novice developer.

# Statement of Need

There is a plethora of various resources pertaining to 3D Slicer and the Plus ToolKit. However, there is a lack of an educational platform, for beginner developers, that consolidates information on the development of a 3D Slicer module that interacts with the PlusServer through the Plus Toolkit and other pre-existing IGT modules. Our objective is to bring together and present key concepts in 3D Slicer module development with a focus on image-guided interventions in a simple way. Ultimately, our goal is to reduce the learning curve for IGT module development with 3D Slicer for beginners.

# Summary of Module Contents 
The following subjects are covered in detail within the learning-module. 
1. 3D Slicer Architecture:
    * MRML Scenes: In 3D Slicer, the MRML scene can be thought of as the workspace, consisting of everything that you interact with, including streaming data, segmentations, models, view layout, etc. In addition, the scene can include components that are not directly visualized.
    * Widgets: These are the building blocks or individual components of the graphic user interface in a 3D Slicer module. 
    * Logic: The logic controls the bulk of the processing of any application, will respond to input from the GUI and control the MRML nodes and the view.
  
2. IGT Module Development:
    * Slicer Components: This covers the definition of 3D Slicer module types, 3D Slicer extensions, and the SlicerIGT extension. 
    * PlusServer Components: This covers an explanation of the PlusServer and the OpenIGTLinkIF module for broadcasting and receiving data.
    * This section also illustrated the specific steps required to stream images and tracking data into 3D slicer using the aforementioned components. 
    
3. Examples and Demonstrations:
    * SlicerIGT extension installation 
    * PlusServer Configuration file creation 
    * Calibration of ultrasound probe and tracked tools 

4. Create your own module: 
    * Development modes: This section contains a description of two methods to develop a module in 3D Slicer, their respective advantages, and associated sample code. 
    * Create a module: This section explains the steps required to generate the necessary files for the creation of a module. 
    * Add module to an extension: This section explains the steps required to make a module publically available.

