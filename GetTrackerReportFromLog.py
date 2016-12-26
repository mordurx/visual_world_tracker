#!/usr/bin/python
# -*- coding: iso-8859-1 -*-ç
import string
from itertools import *
#########  Structure of the data file  #########
class DataFile:
   def __init__(self, ia_width, ia_height,NameOutputFile,data_experiment):
      
      self.outputfile = NameOutputFile #ubicacion archivo de salida
      self.ia_width = int(ia_width)    #ancho area de interes foto
      self.ia_height = int(ia_height)  # largo area de interes foto
      
      self.data_experiment=data_experiment #datos del experimento del opensesame
      self.logFile=open(self.outputfile,'r') #open file
      #print self.data_experiment
      #self.start_SampleTime=0 #indice , indica el tiempo en cual ocurrio la ultimo sampleo.	  	
      #self.newData=""
      #self.item=0
      #self.csi=0
      self.trialTime=0
      sample=0
      self.contador_trial=0
      self.csi=0
      self.dataOpenSesame=""
      self.head="csi\tx\ty\ttime\tIA\tsample\tCS_START_TIME\tCS_END_TIME\tTRIAL_TIME\tCS_START\tCS_END\tUser\titem\tcondExp\timg_1\timg_2\timg_3\timg_4\tcrit_obj\tsound_trial\t" \
      "sent_dur\tsent_onset\tdisplay_onset\tdisplay_offset\tpost_view\ttrial\tstart_audio\tend_audio\tpic_onset\tpicsoffset\ttrial_Onset\ttrial_offset" 

   def GetSample(self,line ,infile):
         infile=infile.strip()
         self.dataOpenSesame=""
         line=line.strip() #quitar espacios en blanco
         arrayLine=line.split("\t") #separar por tab
         #print arrayLine
         nextArrayLine=infile.split("\t") #separar por tab
         time=arrayLine[3]
         self.csi=int(arrayLine[0])
         nextTime=nextArrayLine[3]
         Nextcsi=int(nextArrayLine[0])
         #print Nextcsi
         

         if self.csi==1:
            self.trialTime=0
            self.contador_trial=self.contador_trial+1
            self.mis_datos=self.data_experiment[self.contador_trial-1]
            #print self.mis_datos
         

         if Nextcsi==1:
            trialEnd=int(self.mis_datos[-1])
            sample=trialEnd-int(time)
            nextTime=trialEnd
            self.trialTime=self.trialTime+sample
            
         else:
            sample=int(nextTime)-int(time)
            if self.csi!=1:
               self.trialTime=self.trialTime+sample



         for data in self.mis_datos:
            self.dataOpenSesame=self.dataOpenSesame+"\t"+str(data)
         #print self.csi,sample,time,nextTime   
         return self.csi,sample,time,nextTime,self.trialTime,self.trialTime,self.dataOpenSesame

   def TrialTime(self,line ,infile):
         infile=infile.strip()
         line=line.strip() #quitar espacios en blanco
         arrayLine=line.split("\t") #separar por tab
         nextArrayLine=infile.split("\t") #separar por tab
         #busco csi
         csi=int(arrayLine[0])
         Nextcsi=int(nextArrayLine[0])
         time=arrayLine[3]
         nextTime=nextArrayLine[3]

         if Nextcsi==1 or csi==1:
            self.trialTime=0
         else:
            sample=int(nextTime)-int(time)
            self.trialTime=self.trialTime+sample
            
         return csi,self.trialTime
         
         
   def Generate(self):
      file1 = open(self.outputfile,"r")
      lines =  file1.read().splitlines()
      file1.close()
      outputFile=open(self.outputfile,'w')
      outputFile.write(self.head+"\n")
      for i in range(len(lines)):
        line = lines[i]
        try:
           
           next_line = lines[i+1]
           #csi,self.trialTime= self.TrialTime(line,next_line)
           csi,sample,time,nextTime, self.trialTime,cs_start,self.dataOpensesame=self.GetSample(line,next_line)
           cs_end=sample+self.trialTime
           line=line.strip() 
           line1=line+"\t"+str(sample)+"\t"+str(time)+"\t"+str(nextTime)+"\t"+str(self.trialTime)+"\t"+str(cs_start)+"\t"+str(cs_end)+self.dataOpensesame
           outputFile.write(line1+"\n")
           #print csi,self.trialTime
        except (ValueError,IndexError):
           #print "llego al final!"
           line=line.strip() #quitar espacios en blanco
           arrayLine=line.split("\t") #separar por tab
           time=int(arrayLine[3])
           csi=int(arrayLine[0])
           sample=int(self.mis_datos[-1])-time
           nextTime=int(self.mis_datos[-1])
           self.trialTime=self.trialTime+sample
           cs_end=sample+self.trialTime
           for data in self.mis_datos:
              self.dataOpenSesame=self.dataOpenSesame+"\t"+str(data)
           line1=line+"\t"+str(sample)+"\t"+str(time)+"\t"+str(nextTime)+"\t"+str(self.trialTime)+"\t"+str(cs_start)+"\t"+str(cs_end)+self.dataOpensesame
           outputFile.write(line1+"\n")
           #csi,sample,time,nextTime=self.GetSample(line,int(self.mis_datos[-1]))
           continue 
      outputFile.close()
        #print line
        #print next_line
        
         
         

            
   def EventLog(self):
      logFile=open(self.inputfile,'r')
      patt="start_recording"
      patt2="pic onset"
      patt3="comienza audio"
      patt4="pic offset"
      patt11="stop_recording"
      patt22="pic offset"
      patt33="termina audio"
      
      output=[]
      tupleTrial=[]
      flagStartTrail=0
      flagStartPics=0
      flagStartAudio=0

      #flag end time
      flagEndTrial=0
      flagEndPic=0
      flagEndAudio=0
      for line in logFile:
         isFound=line.find(patt)
         isFound2=line.find(patt2)
         isFound3=line.find(patt3)
         
         isFound11=line.find(patt11)
         isFound22=line.find(patt22)
         isFound33=line.find(patt33)
         if isFound!=-1:
            arrayLine=line.split("\t") #convierne la linea en array
            tupleTrial.append(arrayLine[2])
            flagStartTrail=1
         if isFound2!=-1:
            arrayLine=line.split("\t") #convierne la linea en array
            tupleTrial.append(arrayLine[2])
            flagStartPics=1
         if isFound3!=-1:
            arrayLine=line.split("\t") #convierne la linea en array
            tupleTrial.append(arrayLine[2])
            flagStartAudio=1
         if isFound11!=-1:
            arrayLine=line.split("\t") #convierne la linea en array
            tupleTrial.append(arrayLine[2])
            flagEndTrial=1
         if isFound22!=-1:
            arrayLine=line.split("\t") #convierne la linea en array
            tupleTrial.append(arrayLine[2])
            flagEndPic=1
         if isFound33!=-1:
            arrayLine=line.split("\t") #convierne la linea en array
            tupleTrial.append(arrayLine[2])
            flagEndAudio=1
            
         if  flagStartTrail==1 and flagStartPics==1 and flagStartAudio==1 and flagEndTrial==1 and flagEndPic==1 and flagEndAudio==1:
            output.append(tupleTrial)
            tupleTrial=[]
            flagStartTrail=0
            flagStartPics=0
            flagStartAudio=0
            flagEndTrial=0
            flagEndPic=0
            flagEndAudio=0
      logFile.close()
      return output
   def InsadeOF(self,dic,arrayCoords): #indica que elemento estoy viendo en el trial!!
      X=float(arrayCoords[0]) #coord X del tracker
      Y=float(arrayCoords[1]) #coord Y del tracker
      img1X=float(dic["img_1x"])
      img1Y=float(dic["img_1y"])
      #img2
      img2X=float(dic["img_2x"])
      img2Y=float(dic["img_2y"])
      #img3
      img3X=float(dic["img_3x"])
      img3Y=float(dic["img_3y"])
      #img4
      img4X=float(dic["img_4x"])
      img4Y=float(dic["img_4y"])
      #print arrayCoords
      if img1X<X<img1X+self.ia_width and img1Y<Y<img1Y+self.ia_height:
         area_de_interes=1
      elif img2X<X<img2X+self.ia_width and img2Y<Y<img2Y+self.ia_height:
         area_de_interes=2
      elif img3X<X<img3X+self.ia_width and img3Y<Y<img3Y+self.ia_height:
         area_de_interes=3
      elif img4X<X<img4X+self.ia_width and img4Y<Y<img4Y+self.ia_height:
         area_de_interes=4
      else:
         area_de_interes='.'
      return area_de_interes   
   
#data=[[0, 3, u'vis', u'panal.png', u'balde.png', u'rosquilla.png', u'pipeta.png', 3, u'anillo.ogg', 1000, 2000, 0, 3000, 0, 1, 38145.0, 39145.0, 36149, 39153.0, 36149, 39153.0], [0, 1, u'vis', u'mondadientes.png', u'fuente.png', u'brasero.png', u'caballito.png', 1, u'aguja.ogg', 1000, 2000, 0, 3000, 0, 2, 48141.0, 49141.0, 46146, 49147.0, 46146, 49147.0], [0, 2, u'vis', u'cafe.png', u'baldosas.png', u'rosquilla.png', u'pistola.png', 2, u'ajedrez.ogg', 1000, 2000, 0, 3000, 0, 3, 58110.0, 59110.0, 56108, 59121.0, 56108, 59121.0]]
#DataFile(200,200,'subject-0.txt',data).Generate()
