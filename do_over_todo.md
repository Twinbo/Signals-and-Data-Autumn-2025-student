# 2025 Do-over TODOs

## General

- [ ] Ensure poetry works for environments
- [ ] Ensure UV works for environments
- [ ] Find a solution to students using ```git reset --hard```
- [ ] Find a standard for writing tasks - should there always be explanatory text, then exercises then code, or some other way of doing things?
  - [ ] Standardize the way we write explanatory text and answers for exercises... do we use some specific font or text type? Can we do it without using bold, italic and whatnot?
    - [ ] Consider whether exercise text should be **bold** at all...
  - [ ] Look into a way we can create "standard" HTML classes that then define how explanations and such are written... so we can change variables to have the explanation style change across all notebooks...
  - [ ] How do we discern exercise 1.1, sub exercise a, b and so on?
- [ ] Find a standard for when we need them to implement or test *"x cells below"*
- [ ] the "in general for exercises" should be written a central location, not every notebook
- [ ] BIG ONE: Consider this whole concept of starting with the more advanced topics, and moving your way backwards...
- [ ] BIG ONE AGAIN: Add "You should be able to do this" before each week's exercises. 
- [ ] Consider if we need a special way of commenting on solution code, perhaps ## ANSWER
- [ ] Consider if we need a special way to indicate where code should be written # TODO? or maybe Raise NotImplementedError?

## Week 1

- [x] Longer intro text
  - [ ] Ensure that you properly introduce that images are **matrices**
- [ ] Check if Hiba uses N, M for height and width or H, W, and what she uses for channels
- [ ] Downsize the stupid vase image to a smaller one!
- [ ] Move difficult exercises to end or to own document
- [x] Ex 1.1: Add dots ... to exercises that require your text
- [ ] Ex 1.1 Add more helping code or notes to binarize with thresholding and rgb_gray_scale
- [x] Look through 3.2
- [ ] Redo explanation for color channels
  - [x]  Better text
  - [ ]  Add explanatory images 
- [x] Ex 2.2: Clearly explain where we want them to "normalize each histogram by the total numnber of values of that color"
- [ ] 3 - Consider if $I(x,y)$ as opposed to just $A_{nw}$ is good to use...
- [x] 3 - Better explanation, there should be a more clear "distinction" between the four important parts of a distance measure... Right now it looks... "*uoverskueligt"*
- [x] 3 - Break it up better, use vertical lines and whatnot to make it better
- [x] 3.1 Add intro reminding them that for disproving something, they only need to provide a case where it does not hold
- [x] 3.2 Redo explanations in solutions, they are rather verbose
- [ ] 3.2 - Perhaps redo how the "final note" is introduced
- [ ] Perhaps add exercise about adding single colored "dots", "lines" or "boxes" to images by changing values in an array
- [ ] Standardize folder structures - images should be in an 'images' folder, data in 'data', etc.
- [ ] 6 - Double-check that minkowski is valid only for $p \geq 1$ or is it $p > 1$
- [ ] FINAL: Update non-solution document

## Week 2

- [ ] Redo introduction explanation, more chill distinction between cross-correlation and convolution
- [ ] Add another gif explaining cross-correlation or convolution, perhaps one highlighting differences between the two...
- [ ] Remove the "In general for exercises"
- [ ] Ex 1.1.1: Add small explanation exercise for how the different paddings work...
- [ ] Ex 1.1.2 Standardize convolution2d with dots and whatnot
- [ ] Ex 1.1.2 Explanation cell below, should be given above, also make more newlines and whatnot
- [ ] Ex 1.1.2 Scipy comparison, fix output being given in a whack format
- [ ] Exercise 2: "Why does this kernel blur the image?" question not part of an exercise technically...
- [ ] PERHAPS: Add a "Why do we even learn these 'complete' convolutions when neural network convolutions (learned kernels) are all the rage anyways?"

## Week 3

- [ ] Add more illustrations to intro
  - [ ] Combine with more information about parameters and whatnot, relate learned kernel to convolutions from last week
- [ ] Ex 1.3 Standardize answer format with 1.2 and 1.1
- [ ] Ex 1.4 Sanity check discussion answers
- [ ] Ex 1.6 - Move to difficult exercises section, potentially remove
- [ ] CNN Code - Make a clear outline of what is needed for the boilerplate - then show them as step 1, step 2, step 3, etc.
- [ ] Redo the whole get_dim_before_first_linear to actually work, broke in the assignment previously, check if you can make do without it perhaps?
- [ ] Perhaps more properly outline what differentiates the definition of a FFNN vs a CNN code...
- [ ] Ex 2.1
  - [ ] Have solutions for all exercises
- [ ] Have the feedforward neural
- [ ] Ex 2.2
  - [ ] Add answer example to 2.3.3
- [ ] Ex 2.4
  - [ ] Note that the activations of later layers don't really make sense to examine in regards to the input image; they expect output from previous layers!

## Week 4

- [ ] Move reconstruction of signals to difficult or extra content
  - [ ] Ask Hiba about this if it is alright
- [ ] Add illustrations to illustrate different combinations of sines and cosines
- [ ] Ex 0
  - [ ] Remove option to skip exercise 0
  - [ ] Rename exercise 1
  - [ ] Plot should use fourier stalk plot, not plot plot
- [ ] Briefly explain fourier analysis? Or at least just frequency vs time domain...
- [ ]  Ex 1
  - [ ]  Separate the signals by newlines
  - [ ]  Specify in answers, that the nyquist rate requires it is ABOVE this...
  - [ ]  Have a look-over at this whole subsampling exercise 1.1.3
- [ ]  Ex 2
  - [ ]  Move to difficult section
  - [ ]  Have a do-over look at it
  - [ ]  Actually understand wtf it is, read the fucking curricullum
- [ ]  Orthonormal periodic basis functions
  - [ ]  Shorten?
  - [ ]  More illustrations!
  - [ ]  Add to another notebook? No
  - [ ]  Better and more clear distinction from "this is merely about audio signals" to "this is specifically about curriculum and orthonormal harmonic basis"
- [ ]  Ex 3.1
  - [ ]  3.1.1 - Simplify answer
    - [ ]  No need to use a for loop!
  - [ ]  3.1.2 - Should that be a question?
  - [ ]  Make question asking what the coefficients of whatever are, what do they mean?
- [ ]  Ex 4 - Energy of a signal
  - [ ]  Make question to express or ask about what the energy of a signal *actually* is
  - [ ]  Ex 4.1
    - [ ]  Ensure that people know it *is* a programming exercise (kinda)
    - [ ]  Ensure people know what the signal in question is
  - [ ]  Ex 5 - 
    - [ ]  Make sure people understand the difference between magnitude and amplitude spectrum
    - [ ]  And how this, in part, relates to the energy of a signal
    - [ ]  Elaborate on what is said about re-constructing the signal afterwards
    - [ ]  

## Week 5
- [ ] In general, be very clear about the difference between magnitude and amplitude spectrum, and when we go between the two...
- [ ] Clear difference between introduction explnation and exercises...
- [ ] Images that explain the fourier transform
- [ ] Clear up the note about just removing the positive ones
  - [ ] Really clear that up, people had no idea last year
- [ ] Also clear up the part about frequency bins
  - [ ] Images here!
- [ ] Clear up teh difference between fourier coefficients and amplitudes of the respective frequencies
- [ ] Ex 1.1
  - [ ] 1.1.3 - The exercise asks for the fourier coefficient, but the solution gives the amplitude, this is a mistake
- [ ] Ex 1.2
  - [ ] Make an easier explanation, ask only to complete a function to calculate fourier coefficients
  - [ ] Make rounding in the solution when printing
  - [ ] Print in the cell that runs the function, not the function itself!
- [ ] Ex 1.3
  - [ ] 1.3.1 Add a solution
  - [ ] 1.3.2 Add a solution
  - [ ] 1.3.3 Remove "it is obvious"
  - [ ] Add question that is like "What happened to the missing fourier coefficient?"
- [ ] Ex 2
  - [ ] Move this to the end (unimportant to test properties of the fourier transform before they know how to do the damn thing!)
  - [ ] Better explanatino for why we need both fft and fftfreq for sk_fourier_transform, perhaps a rundown on what they actually do?
- [ ] Ex 3.1
  - [ ] 3.1.2 Either incorporate directly or remove as it is marked a "difficult exercise"
- [ ] Ex 3.2 
  - [ ] Perhaps explain "signal to noise ratio"?
- [ ] Ex 4.3
  - [ ] Less memed please
  - [ ] Make the exercise about ruffians sending white or brown noise, not speech (easier to consider the whole cancelling out)
  - [ ] Redo the exercise with the jamming part, right now, it doesn't make too much sense, any good antenna would be able to discern between transmitted and recieved signals, actually consider this again, since the jamming woudl still work, dependent on if no beamforming or whatnot is being used, most antennas for transmitting are omnidirection and most recievers are omnidirectional as well
  - [ ] Ex 5
    - [ ] Have the STFT be its own thing
    - [ ] More images in explanation
    - [ ] More mathematics in explanation? Formulae?
    - [ ] Itemized list of all the things you need to implement the stft
    - [ ] Find a better way to actually show the STFT, right now it sucks balls
  - [ ] **Overall**, make a complete list of things they should know about signals, the fourier transform, and the fourier coefficients vs the amplitude spectrum and the like!

## Week 6
- [ ] Basically some things should be moved from 5 to 6, unsure what. Perhaps the whole thing on noise?
- [ ] Or perhaps they shoudl just work with the same notebook?
- [ ] Better explanation of differences in graphics for discrete and continuous filters!
- [ ] IMPORTANT: Ensure that you correctly differentiate between k and n! Need to know that y(n) is typically the output value of the signal at value n, where k is more often a "dummy variable"
  - [ ] Talk to Tommy about this, what syntax he prefers...
  - [ ] Have something that more accurately visualizes the difference between "moving the filter across the signal" and "moving the signal across the filter"
- [ ] Explanation for why you get positive and negative frequencies centered around a central frequency, and what that central frequency is...
- [ ] Better image for the impulse response (works bad in dark mode!)
- [ ] Have an example of passing the filter over the dirac delta function
  - [ ] Add exercise to this
- [ ] Check the "whole Is this cross-corr and not convolution?"
- [ ] Ensure that the first exercise corresponds correctly to the last week's first exercise!
- [ ] Ex 2.1 - Properties of the fourier transform
  - [ ] Possibly add to "difficult part of week 6"
  - [ ] Perhaps correct the scale of the resulting stem plot or the coefficients?
    - [ ] Once more tell people that the scale corresponds partly to the sample rate?
  - [ ] More description to the plots
  - [ ] Add on a combined plot (side by side!)
- [ ] Ex 3.1 - Fourier transformations using packages
  - [ ] Check how this corresponds to last week!
- [ ] Ex 5.1
  - [ ] Give a small catch up on discrete filtering formula, so they know what they're using!
  - [ ] Have be first exercises, if people did not get last week, have them look at that in a vaccuum instead
  - [ ] Visual representation of both the signal and the filter
    - [ ] Perhaps an animation? (it is obviously discrete)
    - [ ] Add New follow-up question (ex 5.2?): "Why does the filtered signal seem to increase with n when the filter is constant?"
  - [ ] Ex 5.2
    - [ ] Move explanation of butterworth filter to "difficult exercises"
    - [ ] Better explanation for why we use the butterworth filter as opposed to something just called "bandpass"
  - [ ] Ex 5.3
    - [ ] Move to difficult exercises, possibly in relation to why the butterworth is so weird
    - [ ] Implement logic to show only frequencies from one side of the spectrum
  - [ ] Ex 6
    - [ ] Move spectrogram implementation to previous week (looks better here)


## Week 7
- [ ] Overall should be a major overhaul, it does not look at all like the previous weeks, this is a problem!
- [ ] In general: Change to have the same syntax as previous weeks.
- [ ] Pictures to the introduction
- [ ] A small introduction that introduces the documents as in "how many terms go again in each document, how many words are in each document, etc."?
- [ ] Add another text that has two of the same word?
- [ ] Add an introduction showing the index of each word and each document in the corresponding doc x doc and term x term matrices (what doc is number 5 for example?)
- [ ] Another package for remove_stopwords as opposed to gensim_parsing?
- [ ] Ex 1
  - [ ] Redo text processing, perhaps remove it or add to another file?
- [ ] Redo the whole pipeline: split up into important parts: like load data, examine, remove stopwords, etc.
- [ ] Ex 4.
  - [ ] Add illustration to bag-of-words representation, or example at least
  - [ ] Add simple questions like: With these three documents, how will the bag of words look?
  - [ ] Add implementation exercise for construct_bag_of_words
- [ ] Ex 6
  - [ ] Add small explaantion for the second moment (no way students know what that is...)
  - [ ] Are we using PCA or SVD for decomposing B and C matrices? Perhaps consider this...
  - [ ] Consider if the technical note is even important to ntoe
- [ ] Ex 8.
  - [ ] Add question regarding what would happen if we left in the stop words...
- [ ] Exercise 2.
  - [ ] Fold into previous examples, right now it stands kinda for itself...
- [ ] Exercise 3.
  - [ ] Have a clear seperation from latent semantic analysis and in general word analysis and the next topic which is sentiment analysis
  - [ ] Add formulae and visualizations for sentiment analysis

## Week 8
- [ ] Perhaps have this week be dedicated to word embeddings instead of fasttext, have next week introduce fasttext
- [ ] Visualizations to the introduction

## Week 9
- [ ]
- [ ]

## Week 10
- [ ] Converse with Fabian on what can be done...