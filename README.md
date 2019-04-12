\\\\# StayWoke
Repository for Neurotech @ Berkeley (NT@B) Software Team 2019

## About Stay Woke
Stay Woke is an android application that alerts drivers when they are falling asleep. By using the [Muse](https://choosemuse.com/) Meditation Headset, we are effectively able to analyze EEG data to make predictions about drowsiness. 

## The Problem

Drowsy driving accounts for a large proportion of accidents on the road. In fact 1 in 25 drivers over the age of 18 report falling asleep at the wheel in the previous 30 days. The National Highway Traffic Safety Administration estimates that drowsy driving was responsible for 72,000 crashes, 44,000 injuries, and 800 deaths in 2013. A study by the AAA Foundation for Traffic Safety estimated the actual number to be 328,000, over three times what is reported. Drowsy driving was involved in 6\% of all crashes in which a vehicle was towed from the scene, 7\% of crashes in which a person received treatment for injuries sustained in the crash and 13\% of crashes in which a person was hospitalized. Some studies have demonstrated drowsy driving to be even more dangerous than tipsy driving. Fatigue-related crashes cost society about \$109 billion annually (property damage, health insurance, etc.) One of the biggest demographics affected by this is long haul truck drivers. Many truck drivers report having to drive while sleepy in order to make it to their destination. 

## How We Did It

### The Android Application

Our Android application runs on Java with a Python framework for our signal processing. We used the [ChaquoPy SDK](https://chaquo.com/chaquopy/) to integrate our python algorithm into our native Android Studio App. Connection to the Muse headband is handled by native Muse functions from the Muse Android SDK, which can be found [here](http://developer.choosemuse.com/sdk/android/making-your-own-application). The Muse SDK further allows us to receive Alpha and Theta waves from our headband in a Java array, updating about every 10ms. We then bundle these buffers into larger packets of data over a short period of time, which we then send to the drowsiness detection algorithm using the ChaquoPy SDK to communicate between Python and Java. The algorithm returns a boolean, again using the ChaquoPy framework, which is processed by our Java code to update our home screen. The home screen flips between two states, one which displays that the driver is alert, and another which displays that the driver is drowsy, prompting the user to pull over to the nearest rest stop. We use a simple google maps integration to display the nearest rest stop.

### The Algorithm

We read several papers and settled on one particular paper ?[Driver Drowsiness Detection Using EEG Features](https://link.springer.com/chapter/10.1007/978-3-319-92285-0_49#Fig3)  to use as inspiration for our algorithm. 

Data from Muse was sent in 1 second chunks and analyzed with the following method. 

We extracted the absolute power bands of Alpha, Beta, Delta and Theta waves, and calculated the Root Mean Square of Alpha, and the RMS of the differentiated alpha, and the BAI (Brain Activity Index) as specified in the paper. 

BAI is calculated as follows:


These were outlined as 3 different methods to test drowsiness, however we decided to implement all three methods at particular thresholds to detect drowsiness. 



## Challenges we Faced
Before arriving at our current algorithm for drowsiness detection, we tried to reproduce the processes outlined by several other papers. However, the data that these authors started with was often in a different format than the data extracted via the Muse headset so it was difficult to replicate their results. 
We also struggled to collect a wide breadth of drowsiness data on our own and therefore had to base our drowsiness thresholds off of existing data from papers we cited.
Additionally, the Muse headset may be more sensitive than traditional EEG headsets to artifacts.

## About Us

We are a 14-member software team of the student-run organization Neurotechnology @ Berkeley. We have members from all over the world as well as a variety of majors ranging from Electrical Engineering and Computer Science to Bioengineering to Molecular and Cellular Biology.
