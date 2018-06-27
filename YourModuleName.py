#------------------------------------------------------------------------------------------------------------------#
#Section 1: Import necessary librariesd
#This is where to import the required libraries
#------------------------------------------------------------------------------------------------------------------#
import os
import unittest
import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *
#include any additional libraries required for what you are trying to do 


#------------------------------------------------------------------------------------------------------------------#
#Section 2: Basic module class
#This is where to provide information on your module
#------------------------------------------------------------------------------------------------------------------# 
class YourModuleName(ScriptedLoadableModule):
  """Uses ScriptedLoadableModuleWidget base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """ 
  #This is your initalization 
  def __init__(self, parent):
    ScriptedLoadableModule.__init__(self, parent)
    self.parent.title= "Your Module"
    self.parent.categories=["Insert Slicer category here"]
    #self.parent.dependencies = ["Insert names of exisiting Slicer modules that you will be using here"]
    self.parent.contributors=["Your name"]
    self.parent.helpText="""Write about what your module does here."""
    self.parent.helpText = self.getDefaultModuleDocumentationLink()
  

#------------------------------------------------------------------------------------------------------------------#
#Section 3: Module widget class
# This class contains the widget (GUI) portion of the code.
# This is where to code portion of your module that the user interacts with.
#------------------------------------------------------------------------------------------------------------------# 

class YourModuleNameWidget(ScriptedLoadableModuleWidget):
  """Uses ScriptedLoadableModuleWidget base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """
#*******************************************************************************************************************#
#Section 3.1: Module widget initalization 
#this is where to initalize variables and nodes that will be used within this class
#*******************************************************************************************************************# 
  def __init__(self, parent=None):
    ScriptedLoadableModuleWidget.__init__(self, parent)

    # In this section set member variables equal to None
    self.exampleVariable = None 
    self.exampleNode= None 
    self.exampleTransformNode = None 
    
    #In this section set Slicer module and your modules logics equal to a shorter varaible name 
    self.logic = YourModuleNameLogic()
    #slicer module example 
    self.resliceLogic = slicer.modules.volumereslicedriver.logic()

#*******************************************************************************************************************#
#Section 3.2: Module widget set-up 
#this is where to create widgets and connect them to logic functions
#*******************************************************************************************************************# 
  def setup(self):
    # this is the function that implements all GUI 
    ScriptedLoadableModuleWidget.setup(self)
    
    # This sets the view being used to the red view only 
    slicer.app.layoutManager().setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutOneUpRedSliceView)
  
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Section 3.2.1: Ultrasound connection ang widgets
#the following code provides a GUI to connect to an external ultrasound scanner throught the PlusServer
#this section also provides examples of other widgets that can be used 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# 
   
  ##################################################################################################################
  #This section creates all the widgets
  #This is where you will create the type of widget and what it will say 
  ##################################################################################################################
   
    #This code block creates a collapsible button 
    
    #This defines which type of button you are using 
    self.usButton = ctk.ctkCollapsibleButton()
    #This is what the button will say 
    self.usButton.text = "Ultrasound Connection"
    #This actually creates that button

    #This descirbes the type of widget 
    self.inputIPLineEdit = qt.QLineEdit()
    #This sets a placehoder example of what should be inputted to the line edit 
    self.inputIPLineEdit.setPlaceholderText("127.0.0.1")
    #This is the help tooltip 
    self.inputIPLineEdit.toolTip = "Put the IP address of your ultrasound device here"
    

    #This code block is the exact same as the one above only it asks for the server port 
    self.inputPortLineEdit = qt.QLineEdit()
    self.inputPortLineEdit.setPlaceholderText("18944")
    self.inputPortLineEdit.setValidator(qt.QIntValidator())
    self.inputPortLineEdit.toolTip = "Put the port ID of the OpenIGTLink here (18944)"

    #This is a push button 
    self.connectButton = qt.QPushButton()
    self.connectButton.setDefault(False)
    #This button says connect 
    self.connectButton.text = "Connect"
    #help tooltip that explains the funciton 
    self.connectButton.toolTip = "Connects to Ultrasound"
    #adds the widget to the layout 
    
    self.freezeButton = qt.QPushButton()
    self.freezeButton.text = "Freeze"
    self.freezeButton.toolTip = "Freeze the ultrasound image for fiducial placement"
   

    # Combobox for image selection
    self.imageSelector = slicer.qMRMLNodeComboBox()
    self.imageSelector.nodeTypes = ["vtkMRMLScalarVolumeNode"]
    self.imageSelector.selectNodeUponCreation = True
    self.imageSelector.addEnabled = False
    self.imageSelector.removeEnabled = False
    self.imageSelector.noneEnabled = True
    self.imageSelector.showHidden = False
    self.imageSelector.showChildNodeTypes = False
    self.imageSelector.setMRMLScene( slicer.mrmlScene )
    self.imageSelector.setToolTip( "Pick the image to be used." )

    self.checkBox = qt.QCheckBox()
    self.checkBox.text = "This is a check box"
    self.checkBox.toolTip = "This an example check box" 
    
    #### EXAMPLE: to access the functionality of a check box you can use an if statement
    #### if self.checkBox.isChecked() == True: 
    
    self.radioButton = qt.QRadioButton()
    self.radioButton.text = "This is an example radio button"
    self.radioButton.toolTip = "This an example radio button" 
    
    self.sliderWidget = slicer.qMRMLSliderWidget()
    self.sliderWidget.minimum = 0.00
    self.sliderWidget.maximum = 100.00 
    
    self.resetButton = qt.QPushButton('Reset')
    self.resetButton.setDefault(False)
    self.resetButton.toolTip = "This Button Resets the Module"

  ##################################################################################################################
  #This section adds the containers to the parent widget 
  ##################################################################################################################  
    self.layout.addWidget(self.usButton)
    #This creates a variable that describes layout within this collapsible button 
    self.usLayout = qt.QFormLayout(self.usButton)
    self.usLayout.addRow("Server IP:", self.inputIPLineEdit)
    self.usLayout.addRow("Server Port:", self.inputPortLineEdit)
    self.usLayout.addWidget(self.connectButton)    
    self.usLayout.addRow("US Volume: ", self.imageSelector)
    self.usLayout.addRow(self.freezeButton)
    self.shortcut = qt.QShortcut(qt.QKeySequence('f'), slicer.util.mainWindow())
    self.usLayout.addRow(self.checkBox) 
    self.usLayout.addRow(self.radioButton) 
    self.usLayout.addRow(self.sliderWidget)

     # Add vertical spacer
    self.layout.addStretch(1)

  ##################################################################################################################
  #This section connects the widgets to functions 
  ################################################################################################################## 
    self.connectButton.connect('clicked(bool)', self.onConnectButtonClicked)
    self.freezeButton.connect('clicked(bool)', self.onConnectButtonClicked)
    self.inputIPLineEdit.connect('textChanged(QString)', self.onInputChanged)
    self.inputPortLineEdit.connect('textChanged(QString)', self.onInputChanged)
    self.imageSelector.connect('currentNodeChanged(vtkMRMLNode*)', self.onImageChanged)

    # Disable buttons until conditions are met
    self.connectButton.setEnabled(False) 
    self.freezeButton.setEnabled(False) 

  ##################################################################################################################
  #This section specifies what happens when you activate each widget 
  ################################################################################################################## 
  def onConnectButtonClicked(self):
    if self.connectorNode is None:
        self.connectorNode = slicer.vtkMRMLIGTLConnectorNode()
        # Adds new MRML node, note there is no need for self here as it is its own node
        slicer.mrmlScene.AddNode(self.connectorNode)
        # Configures the connector
        self.connectorNode.SetTypeClient(self.inputIPLineEdit.text, int(self.inputPortLineEdit.text))
    if self.connectorNode.GetState() == slicer.vtkMRMLIGTLConnectorNode.STATE_CONNECTED:
      # Connected
      self.connectorNode.Stop()
      self.connectButton.text = "Connect"
      self.freezeButton.text = "Unfreeze" 
    else:
      # This starts the connection
      self.connectorNode.Start()
      self.connectButton.text = "Disconnect"
      self.freezeButton.text = "Freeze"

  #This allows you to change things without breaking your code 
  def onImageChanged(self, index):
    if self.imageNode is not None:
      # Unparent
      self.imageNode.SetAndObserveTransformNodeID(None)
      self.imageNode = None

    self.imageNode = self.imageSelector.currentNode()
    self.imageSelector.currentNode().SetAndObserveTransformNodeID(self.outputRegistrationTransformNode.GetID())

    slicer.app.layoutManager().sliceWidget('Red').sliceLogic().GetSliceCompositeNode().SetBackgroundVolumeID(self.imageSelector.currentNode().GetID())
    # Configure volume reslice driver, transverse
    self.resliceLogic.SetDriverForSlice(self.imageSelector.currentNode().GetID(), slicer.mrmlScene.GetNodeByID('vtkMRMLSliceNodeRed'))
    self.resliceLogic.SetModeForSlice(self.resliceLogic.MODE_TRANSVERSE, slicer.mrmlScene.GetNodeByID('vtkMRMLSliceNodeRed'))
    slicer.app.layoutManager().sliceWidget("Red").sliceController().fitSliceToBackground()

  def onInputChanged(self, string):
    if re.match("\d{1,3}\.\d{1,3}\.\d{1,3}[^0-9]", self.inputIPLineEdit.text) and self.inputPortLineEdit.text != "" and int(self.inputPortLineEdit.text) > 0 and int(self.inputPortLineEdit.text) <= 65535:
      self.connectButton.enabled = True
      self.freezeButton.enabled = True
      if self.connectorNode is not None:
        self.connectorNode.SetTypeClient(self.inputIPLineEdit.text, int(self.inputPortLineEdit.text))
    else:
      self.connectButton.enabled = False
      
#------------------------------------------------------------------------------------------------------------------#
#Section 4: Module logic class
# This class contains the logic or functionality of your module 
# This is where you should include functions that will be called on within your setup  
#------------------------------------------------------------------------------------------------------------------# 

class YourModuleNameLogic(ScriptedLoadableModuleLogic):
  pass 