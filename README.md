#  MacProgressBar 
•MacProgrssBar is a python module that allows the user to easily create a progress bar on the terminal.<br/>
•Used to keep track of the progress of a python script.

## Different styles
•You may use the premade styles or pass any character/string to be used.<br/>
•The premade styles are:

|Keyword|Symbole|
|------|-------:|
|eighth|`▏`|
|quarter|`▍`|
|half|`▌`|
|three quarters|`▊`|
|seven eighths|`▉`|
|full|`█`|
|apple|``|
|ball|`•`|


#### Example:

![](https://github.com/Pedro4064/MacProgressBar/blob/master/Videos/styleExample.gif?raw=true)

### Message
•You may also display a message every time you update the progress bar, so you know which step of the process the script is executing.

![](https://github.com/Pedro4064/MacProgressBar/blob/master/Videos/message.gif?raw=true)

### Documentation

1- Create the bar object (an instance of the ProgressBar class), and set the max value, the style and initial message.<br/>
`bar = ProgressBar(max = 20,style = 'apple',message = ''`

2- Update the progress bar<br/>
`bar.next(message = '')`

___

#### max:
•The max value is the intended number of iterations.<br/>
•Default value is `100`.<br/>

#### style:
•The [character](#different-styles) used for the progress bar.<br/>
•The default value is `full`

#### message:
•The message that appears next to the preogress bar.<br/>
•The default value is `''` (an empty string).
