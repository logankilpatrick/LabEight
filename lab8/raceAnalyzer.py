#Logan Kilpatrick
#Lab 8
#12/4/2017

import re

class RaceAnalyzer:
    
    def __init__(self):
        #create multiple data structures for the search paramaters. 
        #parse user input using a regex
        #loop through the file 
        #takes in no parameters.... returns nothing....
        #created 3 data types structures! 
        
        
        #create list of list 
        self.raceTypeList = []
        rowFiveOpen = ["  50 MILE OPEN"] 
        rowFiveMaster = ["  50 MILE MASTER"]
        rowTenOpen = ["  100 MILE OPEN"] 
        rowTenMaster = ["  100 MILE MASTER"]
        
        #create Dictonary! 
        self.nameDict = {}
        
        #create count list
        self.countList = []
        self.i = 0 
        
        defaultFileName = "lab8input.txt"
        
        washingtonCount = 0
        oregonCount = 0
        californiaCount = 0
        britishColumbiaCount = 0
        utahCount = 0
        idahoCount = 0
        maineCount = 0
        
        with open(defaultFileName) as f:    
            next(f)#skips the first line 
            for line in f:
                if "Bib" in line: 
                    next(f)
                
                else:
                    splitData = re.search('(\"[^"]+\")[^"]+(\"[^"]+\")\D+(\d+ \w+)\s+(\w+)\D+(\S+)', line, re.IGNORECASE)   #still need to accept DNF 
                    #print(splitData.group(1), splitData.group(2), splitData.group(3),  splitData.group(4), splitData.group(5))
                    #print(splitData.group(2))
                    self.nameDict[splitData.group(1)] = ("Name: " + splitData.group(1) +"\nDistance: " + splitData.group(3) + "\nTime: "+ splitData.group(5))
                    
                    if not splitData:
                        print(line)
                        
                    self.i += 1
                    #     name                location            distance             type of race        time 
                    if ( (splitData.group(3).strip()) == "50 Mile"):
                        if( (splitData.group(4).strip()) == "Open"):
                            rowFiveOpen.append(splitData.group(1))
                        elif( (splitData.group(4).strip()) == "Masters"):
                            rowFiveMaster.append(splitData.group(1))
                            
                    elif ( (splitData.group(3).strip()) == "100 Mile"):
                        if( (splitData.group(4).strip()) == "Open"):
                            rowTenOpen.append(splitData.group(1))
                        elif( (splitData.group(4).strip()) == "Masters"):
                            rowTenMaster.append(splitData.group(1))   
                            
                    myList = splitData.group(2).split(",")                    
                    #print(myList[len(myList)-1])
                    myList[len(myList)-1] = myList[len(myList)-1].strip()
                    
                    if ((myList[len(myList)-1] == 'Wa"') or (myList[len(myList)-1]  == 'WA"') or 
                        (myList[len(myList)-1] == 'Washington"') or (myList[len(myList)-1]  == 'washington"')):
                        washingtonCount += 1
                        
                    elif ((myList[len(myList)-1] == 'Or"') or (myList[len(myList)-1]  == 'OR"') or 
                        (myList[len(myList)-1] == 'Oregon"') or (myList[len(myList)-1]  == 'oregon"')):
                        oregonCount += 1      
                        
                    elif ((myList[len(myList)-1] == 'Bc"') or (myList[len(myList)-1]  == 'BC"') or 
                        (myList[len(myList)-1] == 'British Columbia"') or (myList[len(myList)-1]  == 'british columbia"')):
                        britishColumbiaCount += 1  
                        
                    elif ((myList[len(myList)-1] == 'Ca"') or (myList[len(myList)-1]  == 'CA"') or 
                        (myList[len(myList)-1] == 'California"') or (myList[len(myList)-1]  == 'california"')):
                        californiaCount += 1       
                        
                    elif ((myList[len(myList)-1] == 'Id"') or (myList[len(myList)-1]  == 'ID"') or 
                        (myList[len(myList)-1] == 'Idaho"') or (myList[len(myList)-1]  == 'idaho"')):
                        idahoCount += 1       
                    
                    elif ((myList[len(myList)-1] == 'Ma"') or (myList[len(myList)-1]  == 'MA"') or 
                        (myList[len(myList)-1] == 'Maine"') or (myList[len(myList)-1]  == 'maine"')):
                        maineCount += 1     
                        
                    elif ((myList[len(myList)-1] == 'Ut"') or (myList[len(myList)-1]  == 'UT"') or 
                        (myList[len(myList)-1] == 'Utah"') or (myList[len(myList)-1]  == 'utah"')):
                        utahCount += 1                      
                    
                        
            self.raceTypeList.append(rowFiveOpen)
            self.raceTypeList.append(rowFiveMaster)
            self.raceTypeList.append(rowTenOpen)
            self.raceTypeList.append(rowTenMaster)
            
        self.countList.append("WA: " + str(washingtonCount))
        self.countList.append("OR: " + str(oregonCount))
        self.countList.append("BC: " + str(britishColumbiaCount))
        self.countList.append("CA: " + str(californiaCount))
        self.countList.append("ID: " + str(idahoCount))
        self.countList.append("MA: " + str(maineCount))
        self.countList.append("UT: " + str(utahCount))
        
        
    def __repr__(self):
        '''defualt print... not used'''
        return(splitData.group(1), splitData.group(2), splitData.group(3),  splitData.group(4), splitData.group(5))   

    def getCount(self):
        '''returns the number of times a new object is created in the loop'''
        return(self.i)
        
    def searchByType(self):
        '''no parameters... prints.... retuns nothing...'''
        i = 0
        for r in range (len(self.raceTypeList)):    
            print()
            print()
            
            for c in range (len(self.raceTypeList[r])):  
                self.raceTypeList[r].sort(key=str.lower) #only works for ASCII characters
                print(self.raceTypeList[r][c])
                i += 1
            print(str(self.i - i) + " racers in the race.")
        
        print()
            
            
    def searchByName(self):
        '''no parameters.... prints by name..... prompts user for input... prints as well'''
        holder = input("Please enter the name of the person seperated by a comma: ")
        print()        
        holder = '"' + holder.title() + '"'
        if holder in self.nameDict:    
            print(self.nameDict[holder])
        else :    
            print(holder + " not found.")
            
        print()
            
            
    def searchByLocation(self):
        ''' no parameters... returns nothing... prints by location'''
        print()
        
        for r in range(len(self.countList)):
            print(self.countList[r])        
        print()
            
            