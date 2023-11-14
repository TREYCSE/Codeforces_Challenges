function findLargestIndex(theArray) {
    index = 0;
    largestVValue = theArray[0];
    for (i = 0; i < theArray.length; ++i) {
        if (theArray[i] > largestValue) {
            index = i;
            largestValue = theArray[i];
        }
    }
}

//helpful resources
//threads allow a developer to - perform tasks in parallel
//didn't even get to submit :(
//https://brainly.com/question/18567546
//https://stackoverflow.com/questions/8563469/meaning-of-in-java
//https://stackoverflow.com/questions/20504771/decrementing-elements-in-an-array-list
//to run code, right click and select run code.