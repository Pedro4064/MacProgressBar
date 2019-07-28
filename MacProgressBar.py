import sys

class ProgressBar:
    
    def __init__(self, **kwars):
        
        # Get the argumetns passed
        self.max = kwars.get('max')
        self.type = kwars.get('style')
        self.message = kwars.get('message')
        self.percent = kwars.get('percent')
        

        # if any of them are None, add values so it won't crash
        if self.max == None:
            self.max = 100
        
        if self.type == None:
            self.type = 'full'
        
        if self.message == None:
            self.message = ''

        
        # Diferent blocktypes that can be used
        self.blocks = {'eighth':'▏','quarter':'▍','half':'▌','five eighths':'▋','three quarters':'▊','seven eighths':'▉', 'full':'█','apple':'','ball':'•'}

        # If the type arguments doesn't belong to the self.blocks dictionary, add it to the dictionary and use it
        if self.type not in self.blocks:
            self.blocks[self.type] = self.type

        # The progress bar will have 32 blocks total, the ratio is to know how many iterations to complete the 32 block bar
        self.ratio = int(self.max)/32
        self.counter = 0
        
        # The inital bar
        self.bar = '|                                |'
    
        # Print the inital progress bar + message
        print(self.bar,self.message, end = '')
    
    def next(self,**kwars):

        # Counter for the iteration number
        self.counter+=1
        self.bar = ''

        # If a message argument is passed, update self.message
        if kwars.get('message') != None:
            self.message = kwars.get('message')
        
        # Get the numbers of blocks to print by getting the integer result from the ration between the counter(current iteration number) and the ratio
        self.numberOfBlocks = int(self.counter/self.ratio)
        
        # Add to the bar string the number of blocks
        for block in range(self.numberOfBlocks):
            self.bar = self.bar+self.blocks[self.type]
        
        # Then add the rest of the characters with white spaces
        for i in range(32-self.numberOfBlocks):
            self.bar = self.bar+' '
            
        
        # If the percent argument is True, calculate it and add to the progress bar
        if self.percent == True:
            self.percentage = self.counter*100/self.max
            # Format the bar by adding the beginning and end of the progressbar '|' plus the percentage
            self.bar = '|'+self.bar+'|'+' '+str(self.percentage)+'% '+self.message

        else:
            # Format the bar by adding the beginning and end of the progressbar '|'
            self.bar = '|'+self.bar+'|'+' '+self.message

        # If it is the last iteration, print the bar and a newline, else print just the bar
        if 32-self.numberOfBlocks == 0:
            # Clear the line, print it and flush(show)
            sys.stdout.write("\x1b[2K")
            sys.stdout.flush()
            sys.stdout.write('\r'+self.bar+'\n')
            sys.stdout.flush()

        else:
            # Clear the line, print it and flush(show)
            sys.stdout.write("\x1b[2K")
            sys.stdout.flush()
            sys.stdout.write('\r'+self.bar)
            sys.stdout.flush()