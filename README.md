# youtube-video-analytics
## Research Problems

In this project, we aim to study and explain the abstract concept of “popularity” of a Youtube video. We attempt to identify the key factors that contribute to a video’s popularity, and use that to predict the number of views or likes the video will receive. Levels will be assigned to the number of views and likes to make them class variables.

The dataset also supports the exploration of answers to a few other interesting complementary questions:

Effect of the pandemic: With people working from home we hypothesize that people are likely to display more engagement/viewership.
Differences across videos topics: Eg: Education and Sports are expected to have different consumption rates (Professional vs Leisure)

## Dataset

We plan to curate this video analytics dataset by means of the Youtube API, which provides multiple analytic points for a given video. Most key variables can be grouped into one of the following objects defined in the API spec:

* Statistics: Multiple statistics like view count, like count, share count, etc

* Snippet: High level metadata like time at which the video was published, title, description, etc

* Content Details: Contains information about the video content, including the duration, definition, indication of whether captions are available, geographical restrictions, captions, ratings, etc

* Topic Details: Includes IDs for topics that are tagged to a video


We will select a sample of videos (n to be determined based on rate-limiting of the API) from across Youtube (randomized different creators, topics, popularity, etc) and use the API to collect analytics for those videos.

## Statistical Learning Tools

We look to utilize the following tools:

* Visualization tools for EDA: Boxplots, Histograms, Pair Plot, etc
* Clustering techniques as a form of EDA to look for similarity patterns across videos
* LDA, QDA, and logistic regression for classification and interpretation
* Random Forest and AdaBoost for feature selection and variable importance
* Test set for comparing the performance of the methods
* Cross-Validation for finding the optimal varying parameters, if it’s not too computationally expensive
* Text Processing tools for usage of analysis of textual data like title, description, etc
* Whether Splines and GAM are used will be based on the results obtained above

