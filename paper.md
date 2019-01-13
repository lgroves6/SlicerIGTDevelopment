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
-name: Terry M. Peters
 affiliation:"1,2"
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

# _Statement of Need_

There is a plethora of various resources pertaining to 3D Slicer and the Plus ToolKit. However, there is a lack of an educational platform, for beginner developers, that consolidates information on the development of a 3D Slicer module that interacts with the PlusServer through the Plus Toolkit and other pre-existing IGT modules. Our objective is to bring together and present key concepts in 3D Slicer module development with a focus on image-guided interventions in a simple way. Ultimately, our goal is to reduce the learning curve for IGT module development with 3D Slicer for beginners. A user who follows the tutorial from start to end will learn: (1) an overview of 3D Slicer architecture, (2) how to create a configuration file for the PlusServer, (3) how to perform basic tool calibrations, (4) how to create a scripted module with basic IGT functionality, and (5) how to make their module public.

