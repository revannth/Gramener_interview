
# Gramener Interview Portfolio


## Greetings to the evaluator/gramener job aspirant. These are my solutions to the tasks and problems. Feel free to fork this repository and provide me with your valuable feedback. Now, with that out of the way, let me begin my story.


# Tasks:


## Late, but not quite! Task 2



The task was supposed to be submitted by the 5th of January 2018. Technically(considering the switch from the Julian Calendar caused us,Earthlings, to lose 3 days), the task has been submitted way before the deadline. Humour on its side, this was one of my first pitfalls of the many;this one was to write a generic algorithm for the question posed : " How many Thursdays are there between 1990 and 2000?".

Calculating this using the inbuilt functions is super simple, all one has to do it pass the years as current dates and subtract them. But, even this fails when considering the inconsistency of the Julian Calendar before 1582. Alas, a manual algorithm was the only way out. 

The algorithm I wrote, uses the 1st of Jan 1990, a Monday, as a reference to calculate the number of Thursdays present between any two given years. Though the default input is for 1990 and 2000; the algorithm was accurate for all the test cases in the Gregorian Calendar. Unlike the library based functions, this is compatible with the Julian calendar. All you have to do is change reference the date to any known date from the Julian Calendar. 

#### Solution for Task 2 : 522 Thursdays. The Code can be found here : https://github.com/revannth/Gramener_interview or click [here](https://github.com/revannth/Gramener_interview/blob/master/Task2.py) to go to the python file.

## The Set Conundrum, Task 1

This was a very simple task. We were supposed to find the common elements in two lists and also the elements present in one list and not in the other. With the inbuilt 'set' function, it is hardly a 4 lines program but this compromises your speed since it has a worst-case complexity of len(set1)\*len(set2). This can be optimised without using the builtin functions. Sorting it and then doing a binary search on it gives a much simpler and faster code(a lengthier one though).

Solution for Task 1: common elements - **b**,elements in 1st list and not second - **a,c**. Code can be found here : https://github.com/revannth/Gramener_interview or click [here](https://github.com/revannth/Gramener_interview/blob/master/Task1.py) to go to the python file.


# Use Cases

The days after I applied for the internship were one of the most challenging and strangely, elating days, the majority of which was because of this very problem. The ups and downs of finding the solutions for the problem (Much like its visuals) were nothing short of a rollercoaster ride. This happens to be my first data science project and receiving not one, but three datasets was extremely intimidating. On close inspection of the datasets, it became evident that they were more of reference sheets rather than full-fledged data sets.




Solution to Use case 2 : How do boys and girls perform across states?

I started off by removing all the irrelevant columns such as Father's occupation, Watching TV, etc and retained only the percentages,Gender and the region. I then sorted the data, firstly on the basis of Gender and then the States and then the percentages; Though this might seem as an unnecessary move, it proves to be very insightful. For example, all the unknown gender values are pushed to the bottom, giving you a clear picture of the data you wish to use. After this, I just had to remove all unknown gender values. After this, I dropped the 'NaNs' by firstly threshing out the rows that did not have atleast 4 non null values. I did this since, 4 values included a gender and a region record and approximations would be erroneous if we had less than 2 out of the 4 subjects. After this, I sorted it again for safe measure and then interpolated the values. This is where sorted values come in handy again and give more consistent data to work with. Data is cleaned, now moving to the fun part, the question clearly indicates a comparison; what better way to compare than an old-fashioned "girls are better than guys fight". Thats exactly what I did; I used a macro map from your website to plot the performances of guys and girls, region wise; It was pretty evident from this comparison that girls seemed to be taking the win.[Link to Visual]() or you could click [here-Male](https://github.com/revannth/Gramener_interview/blob/master/Male_Data.xlsm) to get the macro enabled excel sheet or [here-Female](https://github.com/revannth/Gramener_interview/blob/master/Female_Data.xlsm). But this wasnt evidence enough, hence I used the data scientist's best friend, scatterplot, to decide a proper winner. [Link to the Visual](https://sleepy-plateau-86658.herokuapp.com/boyvgirl)

![alt Boy V Girl](https://github.com/revannth/Gramener_interview/blob/master/app/static/images/BoyvsGirl.jpg?raw=true)

With girls winning in 20 regions out of the 35 total regions, the winners are pretty evident.

#### Solution to the question : Girls outperformed guys in 20 states.

### Additional usecases : 
From the two regional maps, you can clearly observe that Women outperformed boys fair and square in places like Kerala,Goa and Orrissa(being the largest margin of difference), we cannot neglect the fact that though such bright students exists, either because of parental pressure or because of the lack of facilities, girls dropout at a very high rate.

Another observation is that the South India states, 
see a fair competition between the girl and boy students; This is not because of the higher competence of South Indian boys, but because of a smaller population, when compared to the North; where in the Boy to Girl ratio is far more superior.

### Solution to Use case 3 : Do students from South Indian states really excel at Math and Science?

This is a very interesting question to pose and the answer I received initially was even more so. Before I move onto the visualisation, I would like to tell you how I cleaned the data. I firstly, removed all the columns(such as Father's occupation,Mother's education.etc) and retained only the ones which were relevant to the problem in hand(Maths %,Science %,etc).

I used one of the excel macros provided by your website to plot a graph. The difference was pretty evident from it. South India was in no comparison to the results and the performance in the North. But that didnt seem right; So I did a little more digging and found some surprising facts. Firstly, a lot of the marks obtained in several parts of North India are either forged or are given away out of leniency(or at times threats). Though this is a case in a very small percentage of schools, lack of regulation makes it easier for students to get away with mal practices, etc. Apart from this, South India is a very small portion(with a lower population density) as compared to the North, hence it would but obvious that the North score better than the South. Another factor to consider is the difficult levels of the question papers. This is something that has been debated on time and again, with the result being in the favour of the South Indians. [Link to visuals](https://sleepy-plateau-86658.herokuapp.com/)

![alt North V South](https://github.com/revannth/Gramener_interview/blob/master/app/static/images/MathvsScience.jpg?raw=true)

### Solution to the question : South Indians arent the best in Mathematics and Science,but they do have outstanding performances.



## Solution to Use case 1: What factors influence the students the most?

This was by far the most challenging questions of them all. Every variable had to be accounted for and I wouldnt be surprised if my answer had a slight deviation, but alas, the visuals dont like. Check the visuals out [here](https://sleepy-plateau-86658.herokuapp.com/Factor) and [here](https://sleepy-plateau-86658.herokuapp.com/intensefactors)

### Solution to the question :
 **The major factor was Age**, though this is a little obvious since as one ages, they get wiser and more responsible towards academics. The next two factors were nearly at a tie, but **Father's occupation,Help in Household,Watching Television and Computer Use**, were also impacting the academics.




##### The link to the git repository with all the code files(including the ipython books and the data cleaning python files) are [here](https://github.com/revannth/Gramener_interview) and the webapp is [here](https://sleepy-plateau-86658.herokuapp.com/)

